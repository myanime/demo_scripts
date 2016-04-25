
import csv
a = [];
i=0;
b='';

csvReader = csv.reader(open('/home/myanime/realtor_ca/realtor_ca/spiders/mainurl2.csv', 'rb'), delimiter=' ', quotechar='|');
for row in csvReader:
    a.append(row);
	
for i in range(0, len(a)):
    print a[i];
    
print a
