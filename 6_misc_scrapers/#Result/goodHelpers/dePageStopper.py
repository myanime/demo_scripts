import os
import csv
import itertools

output = 'clean.csv'
inputName = "completeFile.csv"

def printStuff(row, x):
    with open(output, "a") as outfile:
        outfile.write(row[x].replace('\n', ", "))
        outfile.write(";")


with open(inputName, 'rb') as pageList:
    stateReader = csv.reader(pageList, delimiter=';', quotechar='*')
    #this is for the rows in your downloaded file
    start = 0
    end = 1000000
    y = 0

    for row in itertools.islice(stateReader, start, end):
        #print row[0]
        with open(output, "a") as outfile:
            
            printStuff(row, 0)
            printStuff(row, 1)
            printStuff(row, 2)
            printStuff(row, 3)
            printStuff(row, 4)
            printStuff(row, 5)
            printStuff(row, 6)
            printStuff(row, 7)
            printStuff(row, 8)
            printStuff(row, 9)
            printStuff(row, 10)
            printStuff(row, 11)
            printStuff(row, 12)
            printStuff(row, 13)
            printStuff(row, 14)
            printStuff(row, 15)
            printStuff(row, 16)
            printStuff(row, 17)
            printStuff(row, 18)
            outfile.write("\n")
            
