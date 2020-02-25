import openpyxl


def read_in_excel(excel_path):
    vote_excel_spreadsheet = openpyxl.load_workbook(excel_path)
    sheet_names = vote_excel_spreadsheet.sheetnames

    vote_sheet_name = sheet_names[0]
    style_sheet_name = sheet_names[1]

    votes = read_in_votes(vote_excel_spreadsheet, vote_sheet_name)
    styles = read_in_styles(vote_excel_spreadsheet, style_sheet_name)

    print("\nVotes")
    print(votes)
    print("\nStyles")
    print(styles)


def read_in_votes(vote_excel_spreadsheet, vote_sheet_name):
    vote_sheet = vote_excel_spreadsheet[vote_sheet_name]

    columns_with_ballots = list(vote_sheet.columns)[1:]

    array_of_ballots = []

    for column in columns_with_ballots:
        ballot = []
        for cell in column:
            ballot.append(cell.value)
        array_of_ballots.append(ballot)
    return array_of_ballots


def read_in_styles(vote_excel_spreadsheet, style_sheet_name):
    style_sheet = vote_excel_spreadsheet[style_sheet_name]

    rows_with_styles = list(style_sheet.rows)[1:]

    styles = []
    for row in rows_with_styles:
        style = []
        for cell in row:
            style.append(cell.value)
        styles.append(style)
    return styles


read_in_excel("./test_data.xlsx")
