from data_loader import *
from calculator import *
from candidate_finder import *
from update_ballot import *

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
    number_of_vacancies = load_in_number_of_vacancies()
    quota = calculate_quota(ballot_collection, number_of_vacancies)
    elected_candidate_list = []
    number_elected = 0
    while number_elected < number_of_vacancies:
        candidate_point_list = calculate_candidate_points(ballot_collection)
        # Elects everyone who has reached the quota
        while True:
            elected = elect_a_candidate(candidate_point_list, quota)
            if elected == None:
                candidate_point_list = calculate_candidate_points(
                    ballot_collection)
                elected = elect_a_candidate(candidate_point_list, quota)
                if elected == None:
                    break
            elected_candidate_list.append(elected[1])
            candidate_point_list.remove(elected)
            number_elected += 1
            transfer_factor = calculate_tranfer_factor(
                ballot_collection, elected, quota)
            ballot_collection = apply_transfer_factor_remove_elected_candidate(
                elected[1], ballot_collection, transfer_factor)

        candidate_point_list = calculate_candidate_points(ballot_collection)
        ballot_collection = remove_point_less_candidates(
            ballot_collection, candidate_point_list)
        lowest_point_candidate = find_lowest_point_candidate(
            candidate_point_list)
        ballot_collection = apply_transfer_factor_remove_elected_candidate(
            lowest_point_candidate[1], ballot_collection, 1)

    print(elected_candidate_list)
