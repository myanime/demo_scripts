#Put this file in the same directory as the file whose commas you want to remove
#write name without .csv
infileName = "1"

import csv

with open(infileName + ".csv") as infile, open(infileName + "NC.csv", "w") as outfile:
    for line in infile:
        print line
        outfile.write(line.replace('*', "'"))
