import openpyxl

TEST_DATA_PATH = "./test_data.xlsx"


def read_in_votes(excel_path):
    vote_sheet = get_sheet_by_number(excel_path, 0)
    columns_with_ballots = list(vote_sheet.columns)[1:]
    array_of_ballots = []

    for column in columns_with_ballots:
        ballot = []
        for cell in column:
            ballot.append(cell.value)
        array_of_ballots.append(ballot)
    return array_of_ballots


def read_in_styles(excel_path):
    style_sheet = get_sheet_by_number(excel_path, 1)
    rows_with_styles = list(style_sheet.rows)[1:]
    styles = []

    for row in rows_with_styles:
        style = []
        for cell in row:
            style.append(cell.value)
        styles.append(style)
    return styles


def get_sheet_by_number(excel_path, number):
    vote_excel_spreadsheet = openpyxl.load_workbook(excel_path)
    sheet_names = vote_excel_spreadsheet.sheetnames
    sheet_name = sheet_names[number]

    return vote_excel_spreadsheet[sheet_name]


if __name__ == "__main__":
    print()
