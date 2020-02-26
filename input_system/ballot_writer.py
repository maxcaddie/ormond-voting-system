import csv

def write_raw_ballots_to_csv(raw_ballots, csv_filename):
    FILE = open(csv_filename, 'w')
    writer = csv.writer(FILE)
    for row in raw_ballots:
        writer.writerow(row)
    FILE.close()

