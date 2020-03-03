from calculator import calculate_percentage_of_eligable, calculate_percentage_of_ineligable_votes


def percentage_of_votes(number_of_eligible_voters, ballot_collection):
    number_of_votes = len(ballot_collection)
    return calculate_percentage_of_eligable(number_of_eligible_voters, number_of_votes)


def inelgibable_calcualtions(number_of_ineligible, ballot_collection):
    number_of_votes = len(ballot_collection)
    return calculate_percentage_of_ineligable_votes(number_of_ineligible, number_of_votes)
