import csv
from datetime import datetime

with open('top_50_2023.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = list(reader)

DATE = header.index('album_release_date')
years_count = {}

for row in data:
    year = datetime.strptime(row[DATE], '%Y-%m-%d').year

    if year not in years_count:
        years_count[year] = 0

    years_count[year] += 1

print(max(years_count, key=years_count.get))
