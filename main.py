import csv
import fnmatch
dnimiesiaca = []
for i in range(1, 32):
    dnimiesiaca.append(i)

print(dnimiesiaca)
with open('PLANY 7-13 - grupa 7.csv', encoding='utf-8') as file:
    plan = csv.reader(file)
    daty = []
    indeksydat = []


# czytaj row
# czytaj pierwszy element row
# jeśli row[1] ma format '??.??' lub '?.??':
# dodaj index(row) do indexdat
# dodaj row do daty



