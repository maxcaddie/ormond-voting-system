# US7


def clean_row_turn_into_array(row):
    cleaned_row = row.rstrip('\n')
    array_row = cleaned_row.split(',')
    return array_row


def load_in_ballot_data(csv_of_ballots_path):
    ballots = []
    # US7.1 read in CSV of ballots US7.3 add 1000 to start
    ballot_csv = open(csv_of_ballots_path, 'r')
    for row in ballot_csv:
        a_ballot = clean_row_turn_into_array(row)
        a_ballot.insert(0, 1000)
        ballots.append(a_ballot)
    return ballots


def load_in_number_of_vacancies():
    while True:
        try:
            vacancies = int(input("Enter the number of vacancies: "))
        except ValueError:
            print("Not an integer please re-enter a number")
            continue
        else:
            return vacancies

# US14 Stats


print(load_in_number_of_vacancies())
