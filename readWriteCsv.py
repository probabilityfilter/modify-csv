# Read from a csv and write few rows to another csv
# Not special once you do it but great for a beginner
import csv
import timeit

start_time = timeit.default_timer()

# READ SECTION
filename = "Water 4 tags 1yr.csv"

# initialize column names/titles and rows list
fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # extract field names through first row
    fields = next(csvreader)

    # extract data one row at a time
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))

print('Field names are:' + ', '.join(field for field in fields))
print('\nFirst 5 rows are:\n')

for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col),
    print('\n')

# WRITE SECTION
filename2 = "test_data.csv"

with open(filename2, 'w', newline='') as csvfile2:
    csvwriter = csv.writer(csvfile2)

    # write the fields
    csvwriter.writerow(fields)

    # write the data rows
    csvwriter.writerows(rows[:124])  # only multiples of 4 since there are 4 tags

elapsed = timeit.default_timer() - start_time
print(elapsed)