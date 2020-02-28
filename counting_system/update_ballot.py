# US12 - remove pointless canidates
def remove_pointless_candidates(ballot_list, candidate_points):
    candiates_with_points = [cand for (pts,cand) in candidate_points]

    for ballot in ballot_list:
        index = 1
        while index < len(ballot)):
            current_candidate = ballot[index]
            if current_candidate not in candiates_with_points:
                ballot.remove(current_candidate)
            else:
                index += 1

    return ballot_list        

# US15 - apply transfer factor then remove elected candidate
def apply_TF_remove_elected_candidate(candidate_name, ballot_list, transfer_factor):

    for ballot in ballot_list:
        if ballot[1] == candidate_name:
            ballot[0] = ballot[0] * transfer_factor
        if candidate_name in ballot:
            ballot.remove(candidate_name)
        
    return ballot_list
    