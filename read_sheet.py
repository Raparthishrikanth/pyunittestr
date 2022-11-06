from xlrd import open_workbook
from openpyxl import *

book = open_workbook("test_sheet_YN.xls")
sheet = book.sheet_by_index(0)

first_row = []
for col in range(sheet.ncols):
    first_row.append(sheet.cell_value(0, col))

data = []
for row in range(1, sheet.nrows):
    data_dict = {}
    for col in range(sheet.ncols):
        data_dict[first_row[col]] = sheet.cell_value(row, col)
    data.append(data_dict)