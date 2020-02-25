import csv

mock_ballots = [[1,1,2,3,4],[2,3,0,1,2],[3,4,3,2,1],[4,0,0,1,2]]
mock_styles = [["S","M","L","O"],["O","S","M","L"],["L","O","S","M"],["M","L","O","S"]]

# convert input data to output data
def standardise_ballots(ballots,styles):
    INF = 10000
    NULL = "NULL"
    standardised_ballots = []
    cand_orders = []
    
    # identify ballot style and hence specific votes
    for array in ballots:
        curr_style = styles[array[0]-1]
        std_ballot = []
        for i in range(1,len(array)):
            if array[i] == 0:
                std_ballot.append((INF,NULL))
            else:
                std_ballot.append((array[i],curr_style[i-1]))
        standardised_ballots.append(std_ballot)

    # determine preference order of candidates
    for ballot_info in standardised_ballots:
        cand_order = []
        for (pos,cand) in sorted(ballot_info):
            cand_order.append(cand)
        cand_orders.append(cand_order)

    return cand_orders

def write_ballots_to_csv(raw_ballots):
    for ballot in raw_ballots:
        for cand
standardise_ballots(mock_ballots,mock_styles)




