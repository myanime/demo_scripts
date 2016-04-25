# -*- coding: utf-8 -*-
import re

array = [line.rstrip('\n') for line in open ('./addresslist')]

for x in range (0, len(array)):
    contactInfo = array[x]
    match = re.search(r'\d[A-Za-z][A-Za-z] [A-Za-z]', contactInfo)
    #print match
    if match:
        with open('addressout2', 'a') as f:
            try:
                with open('addressout2', 'a') as f:
                    position = match.start(0) + 3
                    value = contactInfo[:position] + "\t" + contactInfo[position:]
                    f.write(value)
                    f.write("\n")
            except:
                #print "ERROR@"
                with open('addressout2', 'a') as f:
                    f.write("\n")
                pass
    else:
        #print "ERROR@"
        with open('addressout2', 'a') as f:
            f.write("\n")

