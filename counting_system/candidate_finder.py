# US9
def calculate_candidate_points(ballots):
    list_of_candidates_and_their_points = []
    # US9.1: build a points list [(point_value, "name")] for every candidate

    # US9.2: function to parse ballots to accumulate points for each 1st pref candidate and update points list
    return list_of_candidates_and_their_points

# US10


def elect_a_candidate(candidate_point_list, quota):
    highest_candidate_tuple = None
    # US10.1: sort candidate point list

    # US10.2: if highest person achieves quota, return their name, otherwise, return None

    return highest_candidate_tuple

# US13


def find_lowest_point_candidate(candidate_point_list):
    candidate_point_list.sort()
    lowest_points_candidate = candidate_point_list[0]

    return lowest_points_candidate

# US16


def calculate_exhausted_points(candidate_name, ballots):
    number_of_points_with_only_candidate = 0

    return number_of_points_with_only_candidate
