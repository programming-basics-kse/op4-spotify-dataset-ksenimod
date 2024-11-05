import csv

with open('top_50_2023.csv', 'r') as file:
    header = next(csv.reader(file))
    data = list(csv.reader(file))

DANCEABILITY = header.index('danceability')

print(sum(float(row[DANCEABILITY]) for row in data) / len(data))
