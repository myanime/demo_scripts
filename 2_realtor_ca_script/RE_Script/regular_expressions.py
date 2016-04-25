import re
array = [line.rstrip('\n') for line in open ('./addresslist')]

for x in range (0, len(array)):
    contactInfo = array[x]
    match = re.search(r'[A-Za-z]\d[A-Za-z]\s\d[A-Za-z]\d', contactInfo)
    #print match
    if match:
        with open('addressout2', 'a') as f:
            value = match.group(0)
            f.write(value)
            f.write("\n")
    else:
        match = re.search(r'[A-Za-z]\d[A-Za-z]\d[A-Za-z]\d', contactInfo)
        if match:
            with open('addressout2', 'a') as f:
                value = match.group(0)
                f.write(value)
                f.write("\n")
        else:
            match = re.search(r'[A-Za-z]\d[A-Za-z]', contactInfo)
            if match:
                with open('addressout2', 'a') as f:
                    value = match.group(0)
                    f.write(value)
                    f.write("\n")
            else:
                with open('addressout2', 'a') as f:
                    f.write("\n")
    
