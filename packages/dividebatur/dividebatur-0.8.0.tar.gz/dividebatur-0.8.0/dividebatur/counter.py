from collections import defaultdict, namedtuple
import itertools
import fractions

from .results import ElectionDistributionPerformed, \
    ExclusionDistributionPerformed, ActProvision, \
    CandidateElected, CandidatesExcluded, \
    ExclusionReason


TicketState = namedtuple("TicketState", ("Preferences", "UpTo"))


def get_preference(ticket_state):
    if ticket_state.UpTo < len(ticket_state.Preferences):
        return ticket_state.Preferences[ticket_state.UpTo]
    return None


class PapersForCount:
    """
    defines the inital state of the count; eg. the tickets and the number of papers with that ticket
    """

    def __init__(self):
        self.papers = defaultdict(int)

    def add_ticket(self, ticket, n):
        self.papers[ticket] += n

    def __iter__(self):
        return iter(self.papers.items())


class PaperBundle:
    """
    a bundle is a collection of papers, all with the same ticket, and with a transfer value they
    were distributed under
    """

    def __init__(self, ticket_state, size, transfer_value):
        self.ticket_state, self.size, self.transfer_value = ticket_state, size, transfer_value

    def get_size(self):
        return self.size

    def get_ticket_state(self):
        return self.ticket_state

    def set_ticket_state(self, ticket_state):
        self.ticket_state = ticket_state

    def get_transfer_value(self):
        return self.transfer_value


class BundleTransaction:
    """
    a group of bundles which have been transferred to a candidate
    at a common transfer value

    this is stored because we may need to know the number of votes
    contained within the bundle transfer if we later distribute it
    """

    def __init__(self, bundles):
        assert(len(bundles) > 0)
        self.bundles = bundles
        self.transfer_value = None
        # it's impossible for a transfer to occur with bundles at different
        # transfer values; so we can do a little cross-check here
        for bundle in self.bundles:
            if self.transfer_value is None:
                self.transfer_value = bundle.get_transfer_value()
            else:
                assert(self.transfer_value == bundle.get_transfer_value())
        self.votes_fraction = 0
        for bundle in self.bundles:
            self.votes_fraction += bundle.get_size() * self.transfer_value
        self.votes = int(self.votes_fraction)

    def get_transfer_value(self):
        return self.transfer_value

    def get_votes(self):
        return self.votes

    def get_votes_fraction(self):
        return self.votes_fraction

    def get_papers(self):
        return sum(bundle.get_size() for bundle in self.bundles)

    def __iter__(self):
        return iter(self.bundles)


class CandidateBundleTransactions:
    """
    describes which bundles a particular candidate is holding throughout the count
    """

    def __init__(self, candidate_ids, papers_for_count):
        """
        build initial bundles by first preference, and distribute
        """
        self.candidate_bundle_transactions = {}
        # create an entry for every candidate (even if they don't hold any papers)
        for candidate_id in candidate_ids:
            self.candidate_bundle_transactions[candidate_id] = []
        # go through each ticket and count in the papers and assign by first preference
        bundles_to_candidate = defaultdict(list)
        for ticket, count in papers_for_count:
            state = TicketState(ticket, 0)
            # first preferences, by flow
            pref = get_preference(state)
            if pref is None:
                continue
            bundles_to_candidate[pref].append(PaperBundle(state, count, fractions.Fraction(1, 1)))
        for candidate_id in bundles_to_candidate:
            self.candidate_bundle_transactions[candidate_id].append(BundleTransaction(bundles_to_candidate[candidate_id]))

    def paper_count(self, candidate_id):
        """
        returns the number of papers held by the candidate
        """
        papers = 0
        for bundle_transaction in self.candidate_bundle_transactions[candidate_id]:
            for bundle in bundle_transaction:
                papers += bundle.get_size()
        return papers

    def candidate_paper_count(self):
        return dict((candidate_id, self.paper_count(candidate_id)) for candidate_id in self.candidate_bundle_transactions)

    def get(self, candidate_id):
        return self.candidate_bundle_transactions[candidate_id].copy()

    def transfer_to(self, candidate_id, bundle):
        self.candidate_bundle_transactions[candidate_id].append(bundle)

    def transfer_from(self, candidate_id, bundle):
        self.candidate_bundle_transactions[candidate_id].remove(bundle)


class CandidateAggregates:
    """
    stores the number of votes, and the number of papers, held by each candidate at the end of a round
    the number of exhausted papers/votes and the number of votes gained/lost by fraction is also stored
    """

    def __init__(self, original_paper_count, candidate_votes, candidate_papers, exhausted_votes, exhausted_papers):
        self.candidate_votes = candidate_votes
        self.candidate_papers = candidate_papers
        self.exhausted_votes = exhausted_votes
        self.exhausted_papers = exhausted_papers
        self.gain_loss_votes = original_paper_count - sum(candidate_votes.values()) - self.exhausted_votes
        self.gain_loss_papers = original_paper_count - sum(candidate_papers.values()) - self.exhausted_papers

    def get_candidate_ids(self):
        """
        return candidate_ids of all candidates holding votes
        """
        return list(self.candidate_votes.keys())

    def get_candidate_has_papers(self, candidate_id):
        """
        does `candidate_id` hold any papers?
        """
        return self.candidate_papers[candidate_id] > 0

    def get_candidate_votes(self):
        return self.candidate_votes.copy()

    def get_paper_count(self, candidate_id):
        return self.candidate_papers[candidate_id]

    def get_vote_count(self, candidate_id):
        return self.candidate_votes[candidate_id]

    def candidate_votes_iter(self):
        return iter(self.candidate_votes.items())

    def get_exhausted_papers(self):
        return self.exhausted_papers

    def get_exhausted_votes(self):
        return self.exhausted_votes

    def get_gain_loss_papers(self):
        return self.gain_loss_papers

    def get_gain_loss_votes(self):
        return self.gain_loss_votes


class SenateCounter:
    """
    Implementation of the Australian Senate version of an STV ballot, as defined
    by the Commonwealth Electoral Act (1918)
    """

    def __init__(self, results, vacancies, papers_for_count, candidate_ids, candidate_order_fn, disable_bulk_exclusions):
        """
        results: an instance of a subclass of BaseResults
        vacancies: the number of vacancies to be filled in this senate elected
        papers_for_count: an instance of PapersForCount
        candidate_ids: an integer ID for each candidate (must be unique)
        candidate_order_fn: a function which can be called as a key function to [candidate_id, ...].sort(..)
        disable_bulk_exclusions: if True, no bulk exclusions will be performed
        """
        self.results = results
        self.vacancies = vacancies
        self.papers_for_count = papers_for_count
        self.candidate_ids = candidate_ids
        self.candidate_order_fn = candidate_order_fn
        self.disable_bulk_exclusions = disable_bulk_exclusions
        self.next_automated = 0
        # senators elected; candidates excluded from the count; neither of these are
        # eligible to have papers distributed to them
        self.candidates_elected = {}
        self.candidates_excluded = {}
        # we maintain queues of distributions pending; for exclusions and elections. all exclusions
        # must be processed before any elections are processed, even if a part-completed distribution
        # leads to an election
        self.exclusion_distributions_pending = []
        self.election_distributions_pending = []
        self.has_run = False
        self.set_election_order_callback(None)
        self.set_candidate_tie_callback(None)

    def set_election_order_callback(self, cb):
        """
        function `cb` will be called whenever input from the AEO would be required
        to choose an election order from a set of possibilities. the function will
        be passed a list of lists of candidate IDs, and should return the index
        of the option to choose.
        """
        self.election_order_callback = cb

    def set_candidate_tie_callback(self, cb):
        """
        function `cb` will be called whenever input from the AEO would be required
        to choose a candidate to perform an action upon, from a list of possible
        candidates. action could be election or exclusion. the function will be
        be passed a list of lists of candidate IDs, and should return the index
        of the option to choose.
        """
        self.candidate_tie_callback = cb

    def run(self):
        assert(self.has_run is False)
        self.has_run = True
        # determine quota
        self.determine_quota()
        # initial assignment of tickets
        self.candidate_bundle_transactions = CandidateBundleTransactions(self.candidate_ids, self.papers_for_count)
        # execute the count
        self.results.started(self.vacancies, self.total_papers, self.quota)
        self.count()

    def determine_election_order(self, candidate_permutations):
        """
        call the automation callback set with `set_election_order_callback`,
        to break the tie.
        """
        return self.election_order_callback(candidate_permutations)

    def externally_determine_candidate_tie(self, candidates):
        """
        call the automation function (set with `set_candidate_tie_callback`)
        to resolve a tie between candidates
        """
        sorted_candidate_ids = list(sorted(candidates, key=self.candidate_order_fn))
        return sorted_candidate_ids[self.candidate_tie_callback(candidates)]

    def determine_quota(self):
        self.total_papers = sum(count for _, count in self.papers_for_count)
        self.quota = int(self.total_papers / (self.vacancies + 1)) + 1

    def determine_elected_candidates_in_order(self, candidate_votes):
        """
        determine all candidates with at least a quota of votes in `candidate_votes'. returns results in
        order of decreasing vote count. Any ties are resolved within this method.
        """
        eligible_by_vote = defaultdict(list)
        for candidate_id, votes in candidate_votes.candidate_votes_iter():
            if candidate_id in self.candidates_elected:
                continue
            if votes < self.quota:
                continue
            eligible_by_vote[votes].append(candidate_id)

        elected = []
        for votes in reversed(sorted(eligible_by_vote)):
            candidate_ids = eligible_by_vote[votes]
            # we sort here to ensure stability, so external callers can hard-coded their response
            candidate_ids.sort(key=self.candidate_order_fn)
            if len(candidate_ids) == 1:
                elected.append(candidate_ids[0])
            else:
                tie_breaker_round = self.find_tie_breaker(candidate_ids)
                if tie_breaker_round is not None:
                    self.results.provision_used(
                        ActProvision("Multiple candidates elected with %d votes. Tie broken from previous totals." % (votes)))
                    for candidate_id in reversed(sorted(candidate_ids, key=tie_breaker_round.get_vote_count)):
                        elected.append(candidate_id)
                else:
                    self.results.provision_used(
                        ActProvision("Multiple candidates elected with %d votes. Input required from Australian Electoral Officer." % (votes)))
                    permutations = list(itertools.permutations(candidate_ids))
                    permutations.sort()
                    choice = self.determine_election_order(permutations)
                    for candidate_id in permutations[choice]:
                        elected.append(candidate_id)
        return elected

    def get_initial_totals(self):
        "determine the initial total for each candidate. only call this at the start of round 1"
        candidate_votes = {}
        # initialise to zero for every individual candidate
        for candidate_id in self.candidate_ids:
            candidate_votes[candidate_id] = 0
        for candidate_id in self.candidate_ids:
            candidate_votes[candidate_id] = self.candidate_bundle_transactions.paper_count(candidate_id)
        for candidate_id in candidate_votes:
            candidate_votes[candidate_id] = int(candidate_votes[candidate_id])
        return candidate_votes, 0, 0

    def bundle_to_next_candidate(self, bundle):
        """
        returns the next candidate_it of the next preference expressed in the ticket
        for this bundle, and the next ticket_state after preferences are moved along
        if the vote exhausts, candidate_id will be None
        """
        ticket_state = bundle.get_ticket_state()
        while True:
            ticket_state = TicketState(ticket_state.Preferences, ticket_state.UpTo + 1)
            candidate_id = get_preference(ticket_state)
            # if the preference passes through an elected or excluded candidate, we
            # skip over it
            if candidate_id in self.candidates_elected or candidate_id in self.candidates_excluded:
                continue
            return candidate_id, ticket_state

    def distribute_bundle_transactions(self, candidate_votes, bundle_transactions_to_distribute, transfer_value):
        "bundle_transactions_to_distribute is an array of tuples, [(CandidateFrom, BundleTransactions)]"

        # figure out how many net votes, and which ticket_tpls, go where
        incoming_tickets = defaultdict(list)
        exhausted_papers = 0

        # remaining aware of split tickets, determine how many papers go to
        # each candidate; effectively we unpack each bundle into preference flows,
        # split as needed, and then repack into new bundles
        for from_candidate_id, bundle_transactions in bundle_transactions_to_distribute:
            for bundle_transaction in bundle_transactions:
                # take the bundle away from the candidate
                candidate_votes[from_candidate_id] -= bundle_transaction.get_votes()
                self.candidate_bundle_transactions.transfer_from(from_candidate_id, bundle_transaction)

                for bundle in bundle_transaction:
                    # determine the candidate(s) that this bundle of papers flows to
                    to_candidate, next_ticket_state = self.bundle_to_next_candidate(bundle)
                    if to_candidate is None:
                        exhausted_papers += bundle.get_size()
                        continue
                    incoming_tickets[to_candidate].append((next_ticket_state, bundle.get_size()))

        for candidate_id in sorted(incoming_tickets, key=self.candidate_order_fn):
            bundles_moving = []
            for ticket, new_count in incoming_tickets[candidate_id]:
                bundles_moving.append(PaperBundle(ticket, new_count, transfer_value))
            bundle_transaction = BundleTransaction(bundles_moving)
            self.candidate_bundle_transactions.transfer_to(candidate_id, bundle_transaction)
            candidate_votes[candidate_id] += bundle_transaction.get_votes()

        exhausted_votes = int(exhausted_papers * transfer_value)
        return exhausted_votes, exhausted_papers

    def elect(self, candidate_aggregates, candidate_id):
        """
        Elect a candidate, updating internal state to track this.
        Calculate the paper count to be transferred on to other candidates,
        and if required schedule a distribution fo papers.
        """

        # somewhat paranoid cross-check, but we've had this bug before..
        assert(candidate_id not in self.candidates_elected)

        elected_no = len(self.candidates_elected) + 1
        self.candidates_elected[candidate_id] = True

        transfer_value = 0
        excess_votes = paper_count = None
        if len(self.candidates_elected) != self.vacancies:
            excess_votes = max(candidate_aggregates.get_vote_count(candidate_id) - self.quota, 0)
            assert(excess_votes >= 0)
            paper_count = self.candidate_bundle_transactions.paper_count(candidate_id)
            if paper_count > 0:
                transfer_value = fractions.Fraction(excess_votes, paper_count)
            assert(transfer_value >= 0)
            self.election_distributions_pending.append((candidate_id, transfer_value, excess_votes))
        self.results.candidate_elected(
            CandidateElected(
                candidate_id=candidate_id,
                order=elected_no,
                excess_votes=excess_votes,
                paper_count=paper_count,
                transfer_value=transfer_value))

    def exclude_candidates(self, candidates, reason):
        """
        mark one or more candidates as excluded from the count
        candidates: list of candidate_ids to exclude
        reason: the reason for the exclusion
        """

        # put some paranoia around exclusion: we want to make sure that
        # `candidates` is unique, and that none of these candidates have
        # been previously excluded
        for candidate_id in candidates:
            assert(candidate_id not in self.candidates_excluded)
        assert(len(set(candidates)) == len(candidates))

        # determine the paper transfers to be run, and the candidates
        # holding papers which are distributed in each transfer
        transfers_applicable = defaultdict(set)
        for candidate_id in candidates:
            self.candidates_excluded[candidate_id] = True
            for bundle_transaction in self.candidate_bundle_transactions.get(candidate_id):
                value = bundle_transaction.get_transfer_value()
                transfers_applicable[value].add(candidate_id)

        transfer_values = list(reversed(sorted(transfers_applicable)))
        self.results.candidates_excluded(
            CandidatesExcluded(
                candidates=candidates,
                transfer_values=transfer_values,
                reason=reason))

        for transfer_value in transfer_values:
            self.exclusion_distributions_pending.append((list(transfers_applicable[transfer_value]), transfer_value))

    def process_election(self, distribution, last_candidate_aggregates):
        distributed_candidate_id, transfer_value, excess_votes = distribution
        self.results.election_distribution_performed(
            ElectionDistributionPerformed(
                candidate_id=distributed_candidate_id,
                transfer_value=transfer_value))

        candidate_votes = last_candidate_aggregates.get_candidate_votes()
        bundle_transactions_to_distribute = [(distributed_candidate_id, self.candidate_bundle_transactions.get(distributed_candidate_id))]
        exhausted_votes, exhausted_papers = self.distribute_bundle_transactions(
            candidate_votes,
            bundle_transactions_to_distribute,
            transfer_value)
        candidate_votes[distributed_candidate_id] = self.quota
        return distributed_candidate_id, candidate_votes, exhausted_votes, exhausted_papers

    def process_exclusion(self, distribution, last_candidate_aggregates):
        distributed_candidates, transfer_value = distribution

        self.results.exclusion_distribution_performed(
            ExclusionDistributionPerformed(
                candidates=distributed_candidates,
                transfer_value=transfer_value))
        candidate_votes = last_candidate_aggregates.get_candidate_votes()
        total_exhausted_votes, total_exhausted_papers = 0, 0
        bundle_transactions_to_distribute = []
        for candidate_id in distributed_candidates:
            bundle_transactions = [t for t in self.candidate_bundle_transactions.get(candidate_id) if t.get_transfer_value() == transfer_value]
            bundle_transactions_to_distribute.append((candidate_id, bundle_transactions))

        exhausted_votes, exhausted_papers = self.distribute_bundle_transactions(
            candidate_votes,
            bundle_transactions_to_distribute,
            transfer_value)
        total_exhausted_votes += exhausted_votes
        total_exhausted_papers += exhausted_papers

        return distributed_candidates, candidate_votes, total_exhausted_votes, total_exhausted_papers

    def have_pending_exclusion_distribution(self):
        return len(self.exclusion_distributions_pending) > 0

    def process_exclusion_distribution(self, last_candidate_aggregates):
        distribution, *self.exclusion_distributions_pending = self.exclusion_distributions_pending
        return self.process_exclusion(distribution, last_candidate_aggregates)

    def have_pending_election_distribution(self):
        return len(self.election_distributions_pending) > 0

    def process_election_distribution(self, last_candidate_aggregates):
        distribution, *self.election_distributions_pending = self.election_distributions_pending
        return self.process_election(distribution, last_candidate_aggregates)

    def find_tie_breaker(self, candidate_ids):
        """
        finds a round in the count history in which the candidate_ids each had different vote counts
        if no such round exists, returns None
        """
        for candidate_aggregates in reversed(self.round_candidate_aggregates):
            candidates_on_vote = defaultdict(int)
            for candidate_id in candidate_ids:
                votes = candidate_aggregates.get_vote_count(candidate_id)
                candidates_on_vote[votes] += 1
            if max(candidates_on_vote.values()) == 1:
                return candidate_aggregates

    def candidate_to_exclude(self, candidate_aggregates):
        def eligible(candidate_id):
            return candidate_id not in self.candidates_elected and candidate_id not in self.candidates_excluded

        candidate_ids = [t for t in self.candidate_ids if eligible(t)]
        min_votes = min(candidate_aggregates.get_vote_count(t) for t in candidate_ids)

        candidates_for_exclusion = []
        for candidate_id in candidate_ids:
            if candidate_aggregates.get_vote_count(candidate_id) == min_votes:
                candidates_for_exclusion.append(candidate_id)

        next_to_min_votes = None
        candidates_next_excluded = None
        if len(candidates_for_exclusion) > 1:
            tie_breaker_round = self.find_tie_breaker(candidates_for_exclusion)
            if tie_breaker_round is not None:
                excluded_votes = dict((tie_breaker_round.get_vote_count(candidate_id), candidate_id) for candidate_id in candidates_for_exclusion)
                self.results.provision_used(
                    ActProvision("Multiple candidates for exclusion holding %d votes. Tie broken from previous totals." % (min_votes)))
                lowest_vote = min(excluded_votes)
                excluded_candidate_id = excluded_votes[lowest_vote]
            else:
                self.results.provision_used(
                    ActProvision("Multiple candidates for exclusion holding %d votes. Input required from Australian Electoral Officer." % (min_votes)))
                excluded_candidate_id = self.externally_determine_candidate_tie(candidates_for_exclusion)
        else:
            excluded_candidate_id = candidates_for_exclusion[0]
            candidates_with_more_than_min = [candidate_aggregates.get_vote_count(t) for t in candidate_ids if candidate_aggregates.get_vote_count(t) > min_votes]
            if len(candidates_with_more_than_min) > 0:
                next_to_min_votes = min(candidate_aggregates.get_vote_count(t) for t in candidate_ids if candidate_aggregates.get_vote_count(t) > min_votes)
                candidates_next_excluded = [t for t in candidate_ids if candidate_aggregates.get_vote_count(t) == next_to_min_votes]

        margin = None
        if next_to_min_votes is not None:
            margin = next_to_min_votes - min_votes
        return excluded_candidate_id, ExclusionReason("exclusion", {
            'next_to_min_votes': next_to_min_votes,
            'min_votes': min_votes,
            'margin': margin or 0,
            'candidates_next_excluded': candidates_next_excluded
        })

    def get_votes_to_candidates(self, candidates, candidate_aggregates):
        candidate_votes = candidate_aggregates.get_candidate_votes()
        by_votes = defaultdict(list)
        for candidate_id in candidates:
            votes = candidate_votes[candidate_id]
            by_votes[votes].append(candidate_id)
        return by_votes

    def get_candidate_notional_votes(self, candidate_aggregates, adjustment):
        "aggregate of vote received by each candidate, and the votes received by any candidate lower in the poll"
        continuing = self.get_continuing_candidates(candidate_aggregates)
        candidates_notional = {}
        by_votes = self.get_votes_to_candidates(continuing, candidate_aggregates)
        total = adjustment
        for votes, candidates in sorted(by_votes.items(), key=lambda x: x[0]):
            for candidate_id in candidates:
                candidates_notional[candidate_id] = total + votes
            total += votes * len(candidates)
        return candidates_notional

    def get_leading_and_vacancy_shortfall(self, candidate_aggregates):
        continuing = self.get_continuing_candidates(candidate_aggregates)
        candidate_votes = candidate_aggregates.get_candidate_votes()
        shortfalls = []
        for candidate_id in continuing:
            shortfall = self.quota - candidate_votes[candidate_id]
            assert(shortfall > 0)
            shortfalls.append(shortfall)
        shortfalls.sort()
        spots_left = self.vacancies - len(self.candidates_elected)
        return shortfalls[0], sum(shortfalls[:spots_left])

    def determine_bulk_exclusions(self, candidate_aggregates):
        "determine candidates who may be bulk excluded, under 273(13)"
        # adjustment as under (13C) - seems to only apply if more than one candidate was elected in a round
        continuing = self.get_continuing_candidates(candidate_aggregates)
        candidate_votes = candidate_aggregates.get_candidate_votes()
        by_votes = self.get_votes_to_candidates(continuing, candidate_aggregates)
        adjustment = sum(excess_votes for _, _, excess_votes in self.election_distributions_pending)
        candidate_notional_votes = self.get_candidate_notional_votes(candidate_aggregates, adjustment)
        leading_shortfall, vacancy_shortfall = self.get_leading_and_vacancy_shortfall(candidate_aggregates)

        def determine_candidate_A():
            # notional votes >= vacancy shortfall
            eligible = [candidate_id for candidate_id, notional in candidate_notional_votes.items() if notional >= vacancy_shortfall]
            if len(eligible) == 0:
                return None
            # lowest in the poll: tie is irrelevant
            eligible.sort(key=lambda candidate_id: candidate_votes[candidate_id])
            return eligible[0]

        sorted_votes = list(sorted(by_votes.keys()))

        def notional_lower_than_higher(candidate_id):
            "check notional votes of candidate is lower than the number of votes of the candidate standing immediately higher"
            votes = candidate_votes[candidate_id]
            votes_idx = sorted_votes.index(votes)
            # no higher candidate
            if votes_idx == len(sorted_votes) - 1:
                return False
            # legislation ambiguous, but if there's a tie above us let's check all the candidates on that count
            notional = candidate_notional_votes[candidate_id]
            higher_votes = sorted_votes[votes_idx + 1]
            acceptable = all(notional < candidate_votes[t] for t in by_votes[higher_votes])
            return acceptable

        def highest(eligible):
            "return the highest ranked candidate in candidates, by vote. if a tie, or list empty, return None"
            if not eligible:
                return
            binned = self.get_votes_to_candidates(eligible, candidate_aggregates)
            possible = binned[max(binned)]
            if len(possible) == 1:
                return possible[0]

        def determine_candidate_B(candidate_A):
            if candidate_A is not None:
                A_votes = candidate_votes[candidate_A]
                eligible = [candidate_id for candidate_id in continuing if candidate_votes[candidate_id] < A_votes]
            else:
                eligible = [candidate_id for candidate_id in continuing if candidate_notional_votes[candidate_id] < vacancy_shortfall]
            eligible = [candidate_id for candidate_id in eligible if notional_lower_than_higher(candidate_id)]
            return highest(eligible)

        def determine_candidate_C():
            eligible = [candidate_id for candidate_id in continuing if candidate_notional_votes[candidate_id] < leading_shortfall]
            # the candidate of those eligible which stands highest in the poll
            eligible.sort(key=lambda candidate_id: candidate_votes[candidate_id])
            return highest(eligible)

        def candidates_lte(candidate_id):
            votes = candidate_votes[candidate_id]
            lower_votes = [t for t in by_votes.keys() if t < votes]
            to_exclude = [candidate_id]
            for vote in lower_votes:
                to_exclude += [candidate_id for candidate_id in by_votes[vote] if candidate_id in continuing]
            return to_exclude

        # candidate A, B, C as under (13A)(a)
        to_exclude = None
        candidate_A = determine_candidate_A()
        candidate_B = determine_candidate_B(candidate_A)
        candidate_C = None
        if candidate_B:
            candidate_B_votes = candidate_votes[candidate_B]
            if candidate_B_votes < leading_shortfall:
                to_exclude = candidates_lte(candidate_B)
            else:
                candidate_C = determine_candidate_C()
                if candidate_C:
                    to_exclude = candidates_lte(candidate_C)
        if to_exclude and len(to_exclude) == 1:
            to_exclude = None
        return to_exclude, ExclusionReason("bulk", {
            "candidate_A": candidate_A,
            "candidate_B": candidate_B,
            "candidate_C": candidate_C
        })

    def get_continuing_candidates(self, candidate_aggregates):
        return list(set(self.candidate_ids) - set(self.candidates_elected) - set(self.candidates_excluded))

    def process_round(self):
        first_round = False
        if len(self.round_candidate_aggregates) > 0:
            last_candidate_aggregates = self.round_candidate_aggregates[-1]
            exhausted_votes = last_candidate_aggregates.get_exhausted_votes()
            exhausted_papers = last_candidate_aggregates.get_exhausted_papers()
        else:
            first_round = True
            last_candidate_aggregates = None
            exhausted_votes = 0
            exhausted_papers = 0

        # we will always have something to do in each round.
        # we maintain two queues - a queue of exclusion distributions,
        # a queue of election distributions. the exclusion distribution
        # queue takes precedence.
        if first_round:
            candidate_votes, votes_exhausted_in_round, papers_exhausted_in_round = self.get_initial_totals()
        elif self.have_pending_exclusion_distribution():
            distributed_candidates, candidate_votes, votes_exhausted_in_round, papers_exhausted_in_round = \
                self.process_exclusion_distribution(last_candidate_aggregates)
        elif len(self.election_distributions_pending) > 0:
            candidate_id, candidate_votes, votes_exhausted_in_round, papers_exhausted_in_round = \
                self.process_election_distribution(last_candidate_aggregates)
        else:
            raise Exception("No distribution or exclusion this round. Nothing to do - unreachable.")

        # determine new candidate aggregates, after application of actions
        candidate_aggregates = CandidateAggregates(
            self.total_papers,
            candidate_votes,
            self.candidate_bundle_transactions.candidate_paper_count(),
            exhausted_votes + votes_exhausted_in_round,
            exhausted_papers + papers_exhausted_in_round)

        # logging
        self.round_candidate_aggregates.append(candidate_aggregates)
        self.results.candidate_aggregates(candidate_aggregates)

        try:
            # determine actions for this round (if any)
            #
            # if anyone has a quota, elect them; otherwise, if we're not distributing an over-quota,
            # and we're not distributing the result of an exclusion, find someone to exclude (or
            # go with various end-state catch-alls)
            #
            elected = self.determine_elected_candidates_in_order(candidate_aggregates)
            if len(elected) > 0:
                for candidate_id in elected:
                    self.elect(candidate_aggregates, candidate_id)
                    if len(self.candidates_elected) == self.vacancies:
                        return False
                return True

            if not self.have_pending_election_distribution() and not self.have_pending_exclusion_distribution():
                in_the_running = self.get_continuing_candidates(candidate_aggregates)
                still_to_elect = self.vacancies - len(self.candidates_elected)
                # section 273(18); if we're down to N candidates in the running, with N vacancies, the remaining candidates are elected
                if len(in_the_running) == still_to_elect:
                    self.results.provision_used(
                        ActProvision("Final %d vacancies filled from last candidates standing, "
                                     "in accordance with section 273(18)." % (still_to_elect)))
                    for candidate_id in reversed(sorted(in_the_running, key=lambda c: candidate_aggregates.get_vote_count(c))):
                        self.elect(candidate_aggregates, candidate_id)
                    return False
                # section 273(17); if we're down to two candidates in the running, the candidate with the highest number of votes wins - even
                # if they don't have a quota
                if len(in_the_running) == 2:
                    candidate_a = in_the_running[0]
                    candidate_b = in_the_running[1]
                    candidate_a_votes = candidate_aggregates.get_vote_count(candidate_a)
                    candidate_b_votes = candidate_aggregates.get_vote_count(candidate_b)
                    if candidate_a_votes == candidate_b_votes:
                        self.results.provision_used(
                            ActProvision("Final two candidates lack a quota and are tied. Australian Electoral Officer "
                                         "must decide the final election."))
                        candidate_id = self.externally_determine_candidate_tie(in_the_running)
                        self.elect(candidate_aggregates, candidate_id)
                    else:
                        self.results.provision_used(
                            ActProvision("Two candidates remain, with no candidate holding a quota. "
                                         "In accordance with 273(17), candidate with highest total is elected."))
                        if candidate_a_votes > candidate_b_votes:
                            self.elect(candidate_aggregates, candidate_a)
                        elif candidate_b_votes > candidate_a_votes:
                            self.elect(candidate_aggregates, candidate_b)
                    return False

            if not self.have_pending_election_distribution() and not self.have_pending_exclusion_distribution():
                # # FIXME: I believe we can do a bulk exclusion, even if there is an overquota distribution pending
                if not self.disable_bulk_exclusions:
                    bulk_exclude, reason = self.determine_bulk_exclusions(candidate_aggregates)
                    if bulk_exclude:
                        self.exclude_candidates(bulk_exclude, reason)

                # if we exclude a candidate with no papers, there may not be a distribution of
                # preferences - which would leave the next round of the count with nothing to do
                # hence, we loop until there's an exclusion round to process
                #
                # note subtle: if bulk exclusion above didn't trigger a distribution, this code
                # will cascade through
                while not self.have_pending_exclusion_distribution():
                    excluded_candidate, reason = self.candidate_to_exclude(candidate_aggregates)
                    self.exclude_candidates([excluded_candidate], reason)
        finally:
            self.results.round_complete()
        # keep going
        return True

    def count(self):
        self.round_candidate_aggregates = []
        # this is the definitive data structure recording which votes go to which candidate
        # and how many votes that candidate has. it is mutated each round.
        for round_number in itertools.count(1):
            self.results.round_begin(round_number)
            if not self.process_round():
                break
        self.results.finished()
