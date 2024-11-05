import csv

with open('top_50_2023.csv', 'r') as file:
    reader = csv.reader(file)

    header = next(reader)
    data = list(reader)

EXPlICIT = header.index('is_explicit')

print(sum(1 for row in data if row[EXPlICIT] == 'True'))
