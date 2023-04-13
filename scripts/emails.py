import csv
import re

with open("./inputs/emails.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    with open("./outputs/emails.csv", "w") as out_file:
        for [_, email] in csv_reader:
            new_email = re.sub("(@gmail\.com)", "@mlh.io\n", email)
            out_file.write(new_email)
