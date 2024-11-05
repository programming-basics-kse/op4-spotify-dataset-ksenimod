import csv

with open('top_50_2023.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = list(reader)

ARTIST = header.index('artist_name')
artists_count = {}

for row in data:
    artist_name = row[ARTIST]

    if artist_name not in artists_count:
        artists_count[artist_name] = 0

    artists_count[artist_name] += 1

print(max(artists_count, key=artists_count.get))