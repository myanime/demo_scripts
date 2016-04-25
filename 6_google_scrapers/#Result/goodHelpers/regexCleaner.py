#Put this file in the same directory as the file whose commas you want to remove
#write name without .csv


infileName = "clean.csv"

import csv
import fileinput
import time
        
seen = set() # set for fast O(1) amortized lookup
for line in fileinput.FileInput(infileName, inplace=1):
    #print line
    if line in seen: continue
    line2 = line.replace('Karte anzeigen | Route berechnen', "")
    line3 = line2.replace(', Telefaxnummer:', ';')
    line4 = line3.replace('Telefonnummer:', "")
    line5 = line4.replace(', E-Mail-Adresse anzeigen', "")
    #print line5
    #time.sleep(10)
    #if line in seen: continue # skip duplicate
    
    
    seen.add(line5)
    print line5, # standard output is now redirected to the file
'''    
with open(infileName + ".csv") as infile, open(infileName + "NC.csv", "w") as outfile:
    for line in infile:
        #outfile.write(line.replace('*', ""))
        outfile.write(line.replace('Karte anzeigen | Route berechnen', ""))
        #outfile.write(line.replace(', Telefaxnummer:', ';'))
        #outfile.write(line.replace('Telefonnummer:', ""))
        
        
'''
