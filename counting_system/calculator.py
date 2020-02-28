POINTS_PER_BALLOT = 1000

# US8 - calculate quota
def calculate_quota(ballot_list, vacancies):
    formal_votes = len(ballot_list)
    return int(formal_votes*POINTS_PER_BALLOT/(vacancies + 1) + 1)

# US11 - calculate TF
def calculate_tranfer_factor(ballot_list, candidate_tuple, quota):
    achieved_points = candidate_tuple[0]
    candidate_exhuausted_points = calculate_exhausted_points(candidate_tuple, ballot_list)
    return (achieved_points - quota)/(achieved_points - candidate_exhuausted_points)    

# US16 - calculate exhuausted points
def calculate_exhausted_points(candidate_tuple, ballot_list):
    exhuausted_points = 0
    for ballot in ballot_list:
        if len(ballot) == 2 and ballot[1] == candidate_tuple[1]:
            exhuausted_points += ballot[0]
    return exhuausted_points
