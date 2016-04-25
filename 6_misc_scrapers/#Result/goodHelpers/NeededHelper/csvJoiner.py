
import os
import csv
import itertools

SAVE_TO_DIRECTORY = '/home/myanime/Desktop/webScrapers/#Result/0/scraped/1.csv'
completeFile = '2.csv'
listLoad = [None] * 2000
'''
for x in range (0, 2000):
    listLoad[x] = str(x) + ".csv"
    
for x in range (0, 2000):
    #this loops through your renamed files
    myFileNameLoad = SAVE_TO_DIRECTORY + listLoad[x]
'''

with open(SAVE_TO_DIRECTORY, 'rb') as pageList:
    stateReader = csv.reader(pageList, delimiter='~', quotechar='^')
    #this is for the rows in your downloaded file
    start = 0
    end = 30000
    for row in itertools.islice(stateReader, start, end):
        saveRow = '~'.join(row)
        #this saves the row into the common csv file
        saveFile = open(completeFile, 'a')
        saveFile.write(saveRow)
        saveFile.write("\n")
        saveFile.close()
    print "Work in progress..."
print "Finished"
