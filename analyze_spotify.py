import csv

with open('top_50_2023.csv', 'r') as file:
    header = next(file)
    reader = csv.reader(file)

    for i in reader:
        print(i)