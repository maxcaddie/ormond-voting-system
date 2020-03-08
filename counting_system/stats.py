from calculator import calculate_percentage_of_eligable, calculate_percentage_of_ineligable_votes


def percentage_of_votes(number_of_eligible_voters, ballot_collection):
    number_of_votes = len(ballot_collection)
    return calculate_percentage_of_eligable(number_of_eligible_voters, number_of_votes)


def inelgibable_calcualtions(number_of_ineligible, ballot_collection):
    number_of_votes = len(ballot_collection)
    return calculate_percentage_of_ineligable_votes(number_of_ineligible, number_of_votes)


def points_of_lowest_elected(points_at_time_elimination, elected_list):
    points_now = points_at_time_elimination.copy()
    points_now.sort()
    for point_tuple in points_now:
        if point_tuple[1] in elected_list:
            return point_tuple[0]


def print_results(eliminated_candidate_list, elected_candidate_list, voter_turnout, formality_of_votes):
    print(eliminated_candidate_list)
    print("The turnout percentage was "+str(voter_turnout)+"%")
    print("The formality was "+str(formality_of_votes)+"%")

    print(elected_candidate_list)
