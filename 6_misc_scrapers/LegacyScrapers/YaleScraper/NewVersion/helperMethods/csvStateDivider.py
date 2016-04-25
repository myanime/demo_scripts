import os
import csv
import itertools
import time
completeFile = "/home/myanime/Desktop/0/fin/completeFile.csv"
listLoad = [None] * 2000
for x in range (0, 2000):
    listLoad[x] = str(x) + ".csv"
    

myFileNameLoad = completeFile
count = 0
with open(myFileNameLoad, 'rb') as pageList:
    stateReader = csv.reader(pageList, delimiter=',', quotechar='"')
    #this is for the rows in your downloaded file
    start = 1
    end = 300000
    for row in itertools.islice(stateReader, start, end):
        count = count + 1
        saveRow = ', '.join(row)
        #this saves the row into the common csv file
        if row[9] == ' AL':
            saveFile = open("AL.csv", 'a')
            saveFile.write(saveRow)
            saveFile.write("\n")
            saveFile.close()
        elif row[9] == ' AK':
            saveFile = open("AK.csv", 'a')
            saveFile.write(saveRow)
            saveFile.write("\n")
            saveFile.close()
        elif row[9] == " AZ":
            saveFile = open("AZ.csv", 'a')
            saveFile.write(saveRow)
            saveFile.write("\n")
            saveFile.close()
        elif row[9] == " AR":
            saveFile = open("AR.csv", 'a')
            saveFile.write(saveRow)
            saveFile.write("\n")
            saveFile.close()
        else:
            saveFile = open("other.csv", 'a')
            saveFile.write(saveRow)
            saveFile.write("\n")
            saveFile.close()
            
        #print count
print "Finished"
