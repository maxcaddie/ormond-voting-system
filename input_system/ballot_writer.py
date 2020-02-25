import csv

mock_write_data = [['S', 'M', 'L', 'O'], ['M', 'L', 'O'], ['M', 'S', 'O', 'L'], ['O', 'S']]


def write_raw_ballots_to_csv(raw_ballots, csv_filename):
    FILE = open(csv_filename, 'w')
    writer = csv.writer(FILE)
    for row in mock_write_data:
        writer.writerow(row)
    FILE.close()

write_raw_ballots_to_csv(mock_write_data, "raw_data_csv.csv")