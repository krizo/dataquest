import csv
import re

file = open("data_sets/askreddit_2015.csv")
posts_with_header = list(csv.reader(file))
posts = posts_with_header[1:]

of_reddit_count_old = 0
of_reddit_count = 0
serious_count = 0
for row in posts:
    if re.search("of Reddit", row[0]) is not None:
        of_reddit_count_old += 1
    if re.search("of [Rr]eddit", row[0]) is not None:
        of_reddit_count += 1
    # Handling: "(serious)", "(Serious)", "[Serious]", "[serious]"
    # at the beginning of the line
    if re.search("^[\(\[Ss]erious[\]\)]", row[0]) is not None:
        serious_count += 1
    re.sub("[\[\(][Ss]erious[\]\)]", "[Serious]", row[0])
