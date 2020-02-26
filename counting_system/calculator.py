# US8 - calculate quota
# US11 - calculate TF

# confirm below US16 with max
# US16 - calculate exhuausted points
POINTS_PER_BALLOT = 1000

def calculate_quota(ballot_list, vacancies):
    formal_votes = len(ballot_list)
    return int(formal_votes*POINTS_PER_BALLOT/(vacancies + 1) + 1)

# takes in: candidate name, points array, quota
# spits out: transfer factor

def calculate_exhausted_points(candidate, ballot_list):
    exhuausted_points = 0
    for ballot in ballot_list:
        if len(ballot) == 2 and ballot[1] == candidate:
            exhuausted_points += ballot[0]
    
    return exhuausted_points



def calculate_tranfer_factor(ballot_list, candidate_name, candidate_points, quota):
    achieved_points = 0
    candidate_exhuausted_points = calculate_exhausted_points(candidate_name, ballot_list)

    # If we can change output of US10 and pass a tuple (pts,'name') in place of candidate_name
    # then this loop can be removed :)
    for (points,name) in candidate_points:
        if name == candidate_name:
            achieved_points = points

    return (achieved_points - quota)/(achieved_points - candidate_exhuausted_points)    
