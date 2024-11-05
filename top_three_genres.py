import ast
import csv

with open('top_50_2023.csv') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    data = list(reader)

GENRES = header.index('genres')
genres_count = {}

data = [ast.literal_eval(row) for row in data]

for row in data:
    for genre in row[GENRES]:
        if genre not in genres_count:
            genres_count[genre] = 0

        genres_count[genre] += 1

top_3 = sorted(genres_count.items(), key=lambda x: x[1], reverse=True)[:3]

print(genres_count)
print(top_3)

