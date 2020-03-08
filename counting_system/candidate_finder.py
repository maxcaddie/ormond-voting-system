from calculator import ballot_get_highest_preference, ballot_get_points


def add_points_to_candidate(candidate_name, points_to_add, candidate_point_list):
    for (i, (current_points, current_name)) in enumerate(candidate_point_list, 0):
        if current_name == candidate_name:
            candidate_point_list[i] = (
                current_points+points_to_add, candidate_name)
            return candidate_point_list

    candidate_point_list.append((points_to_add, candidate_name))
    return candidate_point_list


def calculate_candidate_points(ballot_list):
    candidate_point_list = []

    for ballot in ballot_list:
        ballot_points = ballot_get_points(ballot)
        ballot_first_preference = ballot_get_highest_preference(ballot)
        candidate_point_list = add_points_to_candidate(
            ballot_first_preference, ballot_points, candidate_point_list)

    return candidate_point_list


def elect_a_candidate(candidate_point_list, quota):
    if len(candidate_point_list) == 0:
        return None
    candidate_point_list.sort(reverse=True)
    # Equals sign worth discussing
    highest_candidate_tuple = candidate_point_list[0]
    if (highest_candidate_tuple[0] >= quota):
        return highest_candidate_tuple

    return None


def find_lowest_point_candidate(candidate_point_list):
    candidate_point_list.sort()
    lowest_points_candidate = candidate_point_list[0]

    return lowest_points_candidate


def get_a_candidates_points(name_of_candidate, candidate_point_list):
    print("a")
    return 0


if __name__ == "__main__":
    print(get_a_candidates_points(
        "Sam", [(1000, "max"), (932, "Sam"), (8432, "Luke")]))
    print(get_a_candidates_points(
        "Max", [(100, "max"), (932, "Sam"), (8432, "Luke")]))
    print(get_a_candidates_points(
        "Max", [(1000, "max"), (932, "Sam"), (8432, "Luke")]))
    print(get_a_candidates_points("Max", [(1000, "max")]))
