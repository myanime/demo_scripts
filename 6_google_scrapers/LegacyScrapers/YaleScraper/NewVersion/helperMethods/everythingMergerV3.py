import fileinput
import os
import csv
import itertools
#change the state number and the name and the savetodirectory list

stateNumber = 50

#this info is for the helper methods
stateName = '/OregonMassachusettsDCTennessee.csv'
completeFile = "/Users/shuzhang/Dropbox/2_SummerPaper/Data/myScraper/selectedState/" + str(stateNumber) + stateName
numberOfDirectories = myEndPage - myStartPage

def helperRename():
    for directory in range (0, numberOfDirectories):    
        for x in range (0, 600):
            try:
                docName = str(x)
                os.chdir(directoryArray[directory])
                files = filter(os.path.isfile, os.listdir(directoryArray[directory]))
                files = [os.path.join(directoryArray[directory], f) for f in files] # add path to each file
                files.sort(key=lambda x: os.path.getmtime(x))
                newest_file = files[x]
                os.rename(newest_file, docName+".csv")
            except:
                print "Finished Renaming"
                traceback.print_exc()
        print "Done Renaming"
        
def helperJoin():
    listLoad = [None] * 1000
        for x in range (0, 1000):
            listLoad[x] = str(x) + ".csv"
    for directory in range (0, numberOfDirectories):
        for renamedfile in range (0, 600):
            try:
                print listLoad[renamedfile]
                myFileNameLoad = directoryArray[directory] +'/' + listLoad[renamedfile]
                
                #this loops through your renamed files
                

                with open(myFileNameLoad, 'rb') as pageList:
                    stateReader = csv.reader(pageList, delimiter=',', quotechar='|')
                    #this is for the rows in your downloaded file
                    start = 1
                    end = 1000
                    for row in itertools.islice(stateReader, start, end):
                        saveRow = ', '.join(row)
                        #this saves the row into the common csv file
                        saveFile = open(completeFile, 'a')
                        saveFile.write(saveRow)
                        saveFile.write("\n")
                        saveFile.close()
                    print myFileNameLoad
                    print "Work in progress..."
            except:
                traceback.print_exc()
                pass
                
        print "Finished"

def helperDuplicateRemover():       
    seen = set() # set for fast O(1) amortized lookup
    for line in fileinput.FileInput(completeFile, inplace=1):
        if line in seen: continue # skip duplicate
        seen.add(line)
        print line, # standard output is now redirected to the file
        
def helperCommaRemover():
    with open(completeFile) as infile, open(completeFile + "NoCommas.csv", "w") as outfile:
        for line in infile:
            outfile.write(line.replace('"', ''))

def helperCounter():
    x = 0
    print "start"
    with open('completeFile','r') as out_file:
    for line in out_file:
        x = x + 1
    print "NumberOfLines"
    print x
    

    
