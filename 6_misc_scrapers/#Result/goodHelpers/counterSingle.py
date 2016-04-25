
import os
import csv
import itertools

output = '25000.csv'
#output2 = '35000.csv'
output2 = None
error = 'error.log'

completeFile = 'scrapedcompleteFile.csv'
x = 0
with open(output, 'rb') as pageList:
    stateReader = csv.reader(pageList, delimiter='~', quotechar='*')
    #this is for the rows in your downloaded file
    start = 0
    end = 30000
    y = 0
    for row in itertools.islice(stateReader, start, end):     
        x = x + 1
        y = y + 1
    print output
    print y
    
with open(error, 'rb') as pageList:
    stateReader = csv.reader(pageList, delimiter='~', quotechar='*')
    #this is for the rows in your downloaded file
    start = 0
    y = 0
    end = 30000
    for row in itertools.islice(stateReader, start, end):     
        x = x + 1
        y = y + 1
    print error
    print y
if output2 != None:
    with open(output2, 'rb') as pageList:
        stateReader = csv.reader(pageList, delimiter='~', quotechar='*')
        #this is for the rows in your downloaded file
        start = 0
        end = 30000
        y = 0
        for row in itertools.islice(stateReader, start, end):     
            x = x + 1
            y = y + 1
        print output2
        print y
        
print "Finished"
print x
print x/2
