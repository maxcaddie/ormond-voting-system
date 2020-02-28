from calculator import ballot_get_highest_preference, ballot_get_points


def remove_point_less_candidates(ballot_list, candidate_points):
    candiates_with_points = [candidate for (
        points, candidate) in candidate_points]

    for ballot in ballot_list:
        index_of_candidate_currently_considered = 1
        while index_of_candidate_currently_considered < len(ballot):
            current_candidate = ballot[index_of_candidate_currently_considered]
            if current_candidate not in candiates_with_points:
                ballot.remove(current_candidate)
            else:
                index_of_candidate_currently_considered += 1

    return ballot_list


def apply_transfer_factor_remove_elected_candidate(candidate_name, ballot_list, transfer_factor):

    for ballot in ballot_list:
        if ballot_get_highest_preference(ballot) == candidate_name:
            ballot[0] = ballot_get_points(ballot) * transfer_factor
        if candidate_name in ballot:
            ballot.remove(candidate_name)

    return ballot_list
