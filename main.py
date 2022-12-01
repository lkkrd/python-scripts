import csv
import fnmatch


with open('PLANY 7-13 - grupa 7.csv', encoding='utf-8') as file:
    datatype = ['??.??.', '?.??.']
    plan = csv.reader(file)
    daty = []
    for row in plan:
        for element in row:
            if fnmatch.filter(element, '??.??.') != []:
                print(fnmatch.filter(element, '??.??'))
            if element in datatype:
                daty.append(element)
            if element == '':
                continue
            else: print(element)
print(daty)

tab = ['chcesz', 'louda']
print(fnmatch.filter(tab, 'lou?aa'))
print(type(tab))


# czytaj row
# czytaj pierwszy element row
# jeśli row[1] ma format '??.??' lub '?.??':
# dodaj index(row) do indexdat
# dodaj row do daty



