import xlsxwriter

from main_repo import get_arr

def writer(array):
    book = xlsxwriter.Workbook(r'C:\Users\dovsy\Desktop\file11.xlsx')
    page=book.add_worksheet('item')

    row=0
    column=0

    page.set_column('A:A', 45)
    page.set_column('B:B', 45)
    page.set_column('C:C', 45)
    page.set_column('D:D', 45)

    for itm in array():
        page.write(row, column, itm[0])
        page.write(row, column+1, itm[1])
        page.write(row, column+2, itm[2])
        page.write(row, column + 3, itm[3])
        row +=1

    book.close()


writer(get_arr)