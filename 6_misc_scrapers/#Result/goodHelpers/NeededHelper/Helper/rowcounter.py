x = 0
print "start"
file = '/home/myanime/Desktop/webScrapers/#Result/0/scraped/Thread_0_0-5000scrapedList.csv'

with open(file,'r') as out_file:
    for line in out_file:
        
        x = x + 1
    print "done"
    print x
