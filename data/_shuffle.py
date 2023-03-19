import csv
import sys
import random

FILENAME = (sys.argv[1] if len(sys.argv) > 1 else '') + 'train.csv'

# Open the CSV file for reading
with open(FILENAME, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Save the header row
    rows = list(reader)

# Shuffle the rows
random.shuffle(rows)

# Open the CSV file for writing
with open(FILENAME, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header row
    writer.writerows(rows)

print(FILENAME, 'successfully shuffled!')
