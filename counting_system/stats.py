from calculator import calculate_percentage_of_eligable, calculate_percentage_of_ineligable_votes, calculate_performance_percentage


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
    


def print_results(eliminated_candidate_list, elected_candidate_list, voter_turnout, formality_of_votes, point_list_when_eliminated):
    print("The turnout percentage was "+str(voter_turnout)+"%")
    print("The formality was "+str(formality_of_votes)+"%")

    print("The elected candidates are: "+str(elected_candidate_list))

    print("The performance_percentage")

    for candidate in eliminated_candidate_list:
        candidate_name = candidate[1]
        candidate_points = candidate[0]
        for record_of_points in point_list_when_eliminated:
            if record_of_points[0] == candidate_name:
                points_at_time_elimated = record_of_points[1]
                break

        lowest_elected = points_of_lowest_elected(
            points_at_time_elimated, elected_candidate_list)

        print(candidate_name, calculate_performance_percentage(
            candidate_points, lowest_elected))


def record_current_points(eliminated_candidate, current_point_list):
    list_to_return = []
    list_to_return.append(eliminated_candidate[1])
    list_to_return.append(current_point_list)
    return list_to_return
