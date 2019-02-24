# Read csv file, rearrange data, save as a new csv
# Each column should be one tag (signal in Seeq jargon)
import csv
import numpy as np
import timeit

INPUT_FILENAME = "Water 4 tags 1yr SMALL.csv"
OUTPUT_FILENAME = "FourTagsOneYear.csv"
VERBOSE = False


def extractCSV(filename, verbose = False):
    """
    :param filename:
    :param verbose:
    :return:
    """
    # count number of rows in csv file
    with open(filename, 'r') as f:
        z = csv.reader(f)
        row_count = len(list(z))

    fields = []
    rows = [None] * (row_count - 1)

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        # extract field names through first row
        fields = next(csvreader)

        # extract each data row one by one
        for n,row in enumerate(csvreader):
            rows[n] = row
        if verbose: print("Total no. of rows: {0}".format(csvreader.line_num))

    if verbose: print('Field names are:' + ', '.join(field for field in fields))
    return fields, rows


def rearrange(rows, verbose = False):
    """
    :param rows:
    :return:
    """
    # DATA REARRANGE SECTION
    dataArray = np.array(rows)

    tagNamesAll = dataArray[:, 0]
    if verbose: print(tagNamesAll[:5])
    tagNamesUnique = np.unique(tagNamesAll)
    if verbose: print(tagNamesUnique)

    for tag in tagNamesUnique:
        tagIndex = tagNamesAll == tag
        tagDataAll = dataArray[tagIndex]  # mark the rows that have the same tag name
        tagValues = tagDataAll[:, 1:3]  # 1:3 reads just DateTime and Value
        if verbose: print(tag)
        if verbose: print(tagValues[:5])
        if tag == "ACWC_BoosterPump_1.Flow":  # get the 'justData' started. Could not initialize it
            justData = tagValues
        else:
            justData = np.append(justData, tagValues, axis=1)
    # 'justData' has 2 columns for each tag: DateTime & Value
    if verbose: print(justData.shape)
    if verbose: print(justData[:5])
    if verbose: print(type(justData))
    return justData


def checkTimestamps(justData, verbose = False):
    """
    :param justData:
    :return:
    """
    # Check if time stamps match between the 1st two tags
    if verbose: print(justData[:, 0] == justData[:, 2])
    if 0 in (justData[:, 0] == justData[:, 2]):
        if verbose: print('Time stamp mismatch')
    else:
        if verbose: print('Time stamps match')


def consolidate(justData, verbose = False):
    """
    :param justData:
    :return:
    """
    return  np.insert(np.delete(justData, np.s_[::2], 1), 0, justData[:, 0], axis=1)


def saveFile(data, filename, verbose = False):
    """
    :param data:
    :param filename:
    :return:
    """
    if verbose: print(data)
    fmt = ('%16s', '%16s', '%16s', '%16s', '%16s') # Parameterize this based on # cols
    delimiter = ","
    np.savetxt(filename, data, delimiter = delimiter, fmt = fmt)


def main():
    """
    :return:
    """
    # Add another function to open file browser and grab CSV, replace INPUT_FILENAME
    # Or use INPUT_FILENAME as default if nothing selected
    verbose = VERBOSE
    fields, rows = extractCSV(INPUT_FILENAME, verbose)
    justData = rearrange(rows, verbose)
    checkTimestamps(justData, verbose)
    data = consolidate(justData, verbose)
    saveFile(data, OUTPUT_FILENAME, verbose)


start_time = timeit.default_timer()

if __name__ == "__main__":
    main()

elapsed = timeit.default_timer() - start_time
print(elapsed)
