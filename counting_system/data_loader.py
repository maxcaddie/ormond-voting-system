
def clean_row_turn_into_array(row):
    cleaned_row = row.rstrip('\n')
    array_row = cleaned_row.split(',')
    return array_row


def load_in_ballot_data(csv_of_ballots_path):
    ballot_list = []
    ballot_csv = open(csv_of_ballots_path, 'r')

    for row in ballot_csv:
        a_ballot = clean_row_turn_into_array(row)
        a_ballot.insert(0, 1000)
        ballot_list.append(a_ballot)
        
    return ballot_list


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
