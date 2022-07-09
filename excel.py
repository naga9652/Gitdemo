import openpyxl
book = openpyxl.load_workbook("C:\\Users\\Hi\\Documents\\excelsheet1.xlsx")
sheet = book.active
cell = sheet.cell(row=1, column=2)
print(cell.value)