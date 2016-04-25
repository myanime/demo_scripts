#Put this file in the same directory as the file whose commas you want to remove
#write name without .csv
infileName = "washington"

import csv

with open(infileName + ".csv") as infile, open(infileName + "NoCommas.csv", "w") as outfile:
    for line in infile:
        outfile.write(line.replace('"', ''))
