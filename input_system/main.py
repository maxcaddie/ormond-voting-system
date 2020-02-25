# bring together all the input functionality

from read_in_csv import *
from ballot_processor import *
from ballot_writer import *

excel_path = input("Please enter ballot data excel filename exactly: \n")

if (excel_path[-5:] != '.xlsx'):
    excel_path = excel_path + ".xlsx"

input_ballots = read_in_votes(excel_path)
styles = read_in_styles(excel_path)
output_ballots = standardise_ballot_styles(input_ballots, styles)
write_raw_ballots_to_csv(output_ballots,"raw_ballots.csv")