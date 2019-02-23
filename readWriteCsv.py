# Read from a csv and write few rows to another csv
# Not special once you do it but great for a beginner
import csv
import timeit

INPUT_FILENAME = "Water 4 tags 1yr.csv"
OUTPUT_FILENAME = "Water 4 tags 1yr SMALL.csv"
ROW_COUNT = 500024
VERBOSE = False

def readCSV(filename, verbose = False):
    header = []
    rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        # extract field names through first row
        header = next(csvreader)

        # extract data one row at a time
        for row in csvreader:
            rows.append(row)
        if verbose: print("Total no. of rows: {0}".format(csvreader.line_num))

    if verbose: print('Field names are:' + ', '.join(field for field in header))
    if verbose:
        print('\nFirst 5 rows are:\n')
        for row in rows[:5]:
            # parsing each column of a row
            for col in row:
                print("%10s" % col),
            print('\n')
    return header, rows


def writeCSV(filename, headerRow, dataRows, rowCount, verbose = False):
    if rowCount%4 != 0: # 4 = number of unique tags
        rowCount = rowCount//4

    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # write the fields
        csvwriter.writerow(headerRow)

        # write the data rows
        csvwriter.writerows(dataRows[:rowCount])


def main():
    verbose = VERBOSE
    fields, rows = readCSV(INPUT_FILENAME, verbose)
    writeCSV(OUTPUT_FILENAME, fields, rows, ROW_COUNT, verbose)


start_time = timeit.default_timer()

if __name__ == "__main__":
    main()

elapsed = timeit.default_timer() - start_time
print(elapsed)
