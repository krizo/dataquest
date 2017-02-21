import csv
import datetime

file = open("data_sets/askreddit_2015.csv")
posts_with_header = list(csv.reader(file))
posts = posts_with_header[1:]
posts_per_month = {}
for row in posts:
    time_str = float(row[2])
    time = datetime.datetime.fromtimestamp(time_str)
    row[2] = time
    if time.month in posts_per_month:
        posts_per_month[time.month] += 1
    else:
        posts_per_month[time.month] = 1
print(posts_per_month)
