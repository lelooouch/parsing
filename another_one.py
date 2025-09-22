import xlsxwriter
from script import array

def writer(parametr):

    book = xlsxwriter.Workbook(r"base1.xlsx")
    page = book.add_worksheet('цитата')

    row = 0
    col = 0

    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)
    page.set_column('D:D', 50)

    for item in parametr():
        page.write(row, col, item[0])
        page.write(row, col+1, item[1])
        page.write(row, col+2, item[2])
        page.write(row, col+3, item[3])
        row += 1

    book.close()

writer(array)
