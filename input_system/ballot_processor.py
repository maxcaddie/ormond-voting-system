import csv

mock_ballots = [[1,1,2,3,4],[2,3,0,1,2],[3,4,3,2,1],[4,0,0,1,2]]
mock_styles = [["S","M","L","O"],["O","S","M","L"],["L","O","S","M"],["M","L","O","S"]]

NOT_PREFERENCED = 0

# convert all ballots to the same style, remove unpreferenced votes and replace with names
def standardise_ballot_styles(vote_ballots,ballot_styles):
    standardised_ballots_in_same_style = standardise_ballots(vote_ballots, ballot_styles)
    ballots_with_names_in_order = determine_preference_order_of_candidiates(standardised_ballots_in_same_style)

    return ballots_with_names_in_order

def standardise_ballots(vote_ballots, ballot_styles):
    standardised_ballots = []
    for ballot in vote_ballots:
        this_ballot_style = get_style_from_a_ballot(ballot, ballot_styles)
        standardised_ballot = convert_ballot_to_standard_ballot(ballot, this_ballot_style)
        standardised_ballots.append(standardised_ballot)
    return standardised_ballots

def convert_ballot_to_standard_ballot(ballot, ballot_style):
    standardised_ballot = []
    for i in range(1,len(ballot)):
        if ballot[i] != NOT_PREFERENCED:
            standardised_ballot.append((ballot[i],ballot_style[i-1]))
    return standardised_ballot

def get_style_from_a_ballot(ballot,ballot_styles):
    return ballot_styles[get_style_number_from_a_ballot(ballot)]

def get_style_number_from_a_ballot(ballot):
    return ballot[0]-1

def determine_preference_order_of_candidiates(standardised_ballots):
    ballots_with_names_in_order = []
    for ballot in standardised_ballots:
        candiates_ordered = []
        for (pos,cand) in sorted(ballot):
            candiates_ordered.append(cand)
        ballots_with_names_in_order.append(candiates_ordered)
    return ballots_with_names_in_order

print(standardise_ballot_styles(mock_ballots,mock_styles))
