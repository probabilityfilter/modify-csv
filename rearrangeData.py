# Read csv file, rearrange data, save as a new csv
# Each column should be one tag (signal in Seeq jargon)
import csv
import numpy as np

# READ SECTION
filename = "test_data.csv"

# initialize column names/titles and rows list
fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # extract field names through first row
    fields = next(csvreader)

    # extract each data row one by one
    for row in csvreader:
        rows.append(row)
    #print("Total no. of rows: %d" % (csvreader.line_num))
    print("Total no. of rows: {0}".format(csvreader.line_num))

print('Field names are:' + ', '.join(field for field in fields))

# DATA REARRANGE SECTION
dataArray = np.array(rows)
tagNamesAll = dataArray[:, 0]
print(tagNamesAll[:5])
tagNamesUnique = np.unique(tagNamesAll)
print(tagNamesUnique)

for tag in tagNamesUnique:
    tagIndex = tagNamesAll == tag
    tagDataAll = dataArray[tagIndex]  # mark the rows that have the same tag name
    tagValues = tagDataAll[:, 1:3]  # 1:3 reads just DateTime and Value
    print(tag)
    print(tagValues[:5])
    if tag == "ACWC_BoosterPump_1.Flow":  # get the 'justData' started. Could not initialize it
        justData = tagValues
    else:
        justData = np.append(justData, tagValues, axis=1)
# 'justData' has 2 columns for each tag: DateTime & Value

print(justData.shape)
print(justData[:5])
print(type(justData))

# Check if time stamps match between the 1st two tags
print(justData[:, 0] == justData[:, 2])
if 0 in (justData[:, 0] == justData[:, 2]):
    print('Time stamp mismatch')
else:
    print('Time stamps match')

# Remove time stamp column from all tags except hte first one so that Seeq can use it
# print(np.delete(justData, np.s_[::2], 1))
# print(np.insert(np.delete(justData, np.s_[::2], 1), 0, justData[:, 0], axis=1))

SeeqTagValues = np.insert(np.delete(justData, np.s_[::2], 1), 0, justData[:, 0], axis=1)
print(SeeqTagValues[:5])
np.savetxt("foo.csv", SeeqTagValues, delimiter=",", fmt=('%16s', '%16s', '%16s', '%16s', '%16s'))
