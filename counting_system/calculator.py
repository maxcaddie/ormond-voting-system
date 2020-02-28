MAX_BALLOT_POINTS = 1000
CANDIDATE_TUPLE_NAME = 1


def calculate_quota(ballot_list, vacancies):
    formal_votes = len(ballot_list)
    # Constitution 68.2 gives this formula
    return int(formal_votes*MAX_BALLOT_POINTS/(vacancies + 1) + 1)


def calculate_tranfer_factor(ballot_list, candidate_tuple, quota):
    candidate_tuple.sort(reverse=True)
    achieved_points = candidate_tuple[0]
    candidate_exhuausted_points = calculate_exhausted_points(
        candidate_tuple, ballot_list)
    # 68.5.a gives this formula
    return (achieved_points - quota)/(achieved_points - candidate_exhuausted_points)


def calculate_exhausted_points(candidate_tuple, ballot_list):
    exhuausted_points = 0
    for ballot in ballot_list:
        if len(ballot) == 2 and ballot_get_highest_preference(ballot) == candidate_tuple[CANDIDATE_TUPLE_NAME]:
            exhuausted_points += ballot_get_points(ballot)
    return exhuausted_points


def ballot_get_highest_preference(ballot):
    return ballot[1]


def ballot_get_points(ballot):
    return ballot[0]
