from data_loader import load_in_ballot_data, load_in_csv_path, load_in_integer_with_message
from calculator import calculate_quota, calculate_tranfer_factor
from candidate_finder import calculate_candidate_points, elect_a_candidate, find_lowest_point_candidate
from update_ballot import remove_point_less_candidates, apply_transfer_factor_remove_candidate
from stats import percentage_of_votes, inelgibable_calcualtions, print_results, record_current_points

# US17

# variable format definitions:
#
# ballot_collection = [[pts, "cand_name"], etc]
# quota = integer
# elected_candidates = ["elected_1", "elected_2", etc]
# number_vacancies = integer
# candidate_points = [(pts, "cand_name"), etc]
# elected

if __name__ == "__main__":
    csv_path = load_in_csv_path()
    ballot_collection = load_in_ballot_data(csv_path)

    # Stats
    number_of_eligable_voters = load_in_integer_with_message(
        "Enter the number of eligable voters: ")
    number_of_informal_votes = load_in_integer_with_message(
        "Enter the number of informal votes: ")
    voter_turnout = percentage_of_votes(
        number_of_eligable_voters, ballot_collection)
    formality_of_votes = inelgibable_calcualtions(
        number_of_informal_votes, ballot_collection)

    number_of_vacancies = load_in_integer_with_message(
        "Enter the number of vacancies: ")
    quota = calculate_quota(ballot_collection, number_of_vacancies)

    elected_candidate_list = []
    eliminated_candidate_list = []
    point_list_when_eliminated = []
    number_elected = 0
    points_of_last_elected = 0
    while number_elected < number_of_vacancies:
        candidate_point_list = calculate_candidate_points(ballot_collection)
        # Elects everyone who has reached the quota
        while True:
            elected = elect_a_candidate(candidate_point_list, quota)
            if elected == None:
                if number_of_vacancies <= number_elected:
                    candidate_point_list.append((points_of_last_elected, elected_candidate_list[-1]))
                    for candidate in candidate_point_list:
                        if candidate[1] not in elected_candidate_list:
                            point_list_when_eliminated.append(record_current_points(
                                candidate, candidate_point_list))
                            eliminated_candidate_list.append(candidate)
                    print_results(eliminated_candidate_list, elected_candidate_list,
                                  voter_turnout, formality_of_votes, point_list_when_eliminated)
                    quit()
                candidate_point_list = calculate_candidate_points(
                    ballot_collection)
                elected = elect_a_candidate(candidate_point_list, quota)
                if elected == None:
                    break
            elected_candidate_list.append(elected[1])
            points_of_last_elected = elected[0]
            candidate_point_list.remove(elected)
            number_elected += 1
            transfer_factor = calculate_tranfer_factor(
                ballot_collection, elected, quota)
            ballot_collection = apply_transfer_factor_remove_candidate(
                elected[1], ballot_collection, transfer_factor)

        candidate_point_list = calculate_candidate_points(ballot_collection)
        ballot_collection = remove_point_less_candidates(
            ballot_collection, candidate_point_list)
        lowest_point_candidate = find_lowest_point_candidate(
            candidate_point_list)
        ballot_collection = apply_transfer_factor_remove_candidate(
            lowest_point_candidate[1], ballot_collection, 1)
        point_list_when_eliminated.append(record_current_points(
            lowest_point_candidate, candidate_point_list))
        eliminated_candidate_list.append(lowest_point_candidate)

    print_results(eliminated_candidate_list, elected_candidate_list,
                  voter_turnout, formality_of_votes, point_list_when_eliminated)
