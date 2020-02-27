# US7


def clean_row_turn_into_array(row):
    cleaned_row = row.rstrip('\n')
    array_row = cleaned_row.split(',')
    return array_row


def load_in_data(csv_of_ballots_path):
    ballots = []
    # US7.1 read in CSV of ballots
    ballot_csv = open(csv_of_ballots_path, 'r')
    for row in ballot_csv:
        a_ballot = clean_row_turn_into_array(row)

    # US7.2 Read in by input # vacancices

    # US7.3 Make 1000 first element of every ballot

    return ballots
# US14 Stats


print(load_in_data("./out4.csv"))
