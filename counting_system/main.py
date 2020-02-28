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
