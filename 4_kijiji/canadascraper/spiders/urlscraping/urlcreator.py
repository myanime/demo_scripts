



base = 'http://www.kijiji.ca/b-house-rental/gta-greater-toronto-area'
basepage = base + '/page-'
number = '/c43l1700272'
x = 400
count = 0
interval = 100
while x < 2500:
    y = x + interval
    for i in range (1, 100):
        if i == 1:
            print(base + number + "?price=" + str(x) + "__" + str(y))            
        else:
            print(basepage + str(i) + number + "?price=" + str(x) + "__" + str(y))
    x = x + interval


x = 0
y = 400
for i in range (1, 100):
    if i == 1:
        print(base + number + "?price=" + str(x) + "__" + str(y))   
    else:
        print(basepage + str(i) + number + "?price=" + str(x) + "__" + str(y))

x = 2500
y = 80000
for i in range (1, 100):
    if i == 1:
        print(base + number + "?price=" + str(x) + "__" + str(y))   
    else:
        print(basepage + str(i) + number + "?price=" + str(x) + "__" + str(y))


