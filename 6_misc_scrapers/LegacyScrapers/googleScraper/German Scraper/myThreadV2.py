import threading
import FarmerClass
import time

listLoad = ["1.csv", "2.csv", "3.csv", "4.csv", "5.csv", "6.csv", "7.csv", "8.csv", "9.csv", "10.csv", "11.csv", "12.csv", "13.csv", "14.csv", "15.csv", "16.csv", "17.csv", "18.csv", "19.csv", "20.csv"]
listSave = ["phone1.txt", "phone2.txt", "phone3.txt", "phone4.txt", "phone5.txt", "phone6.txt", "phone7.txt", "phone8.txt", "phone9.txt", "phone10.txt", "phone11.txt", "phone12.txt", "phone13.txt", "phone14.txt", "phone15.txt", "phone16.txt", "phone17.txt", "phone18.txt", "phone19.txt", "phone20.txt"]
listNumber = ["Thread 1", "Thread 2", "Thread 3", "Thread 4", "Thread 5", "Thread 6", "Thread 7", "Thread 8", "Thread 9", "Thread 10", "Thread 11", "Thread 12", "Thread 13", "Thread 14", "Thread 15", "Thread 16", "Thread 17", "Thread 18", "Thread 19", "Thread 20"]

def myFarmer(myFileName, myFileNameLoad, threadNumber):
    farmThread = FarmerClass.Farmer(myFileName, myFileNameLoad, threadNumber)
    farmThread.goFarm()

for number in range (0, 1):
    try:
        myFileNameSave = listSave[number]
        myFileNameLoad = listLoad[number]
        myThreadNumber = listNumber[number]
        t = threading.Thread(target=myFarmer, args = (myFileNameSave, myFileNameLoad, myThreadNumber))
        t.start()
        time.sleep(15)
    except:
        print "Error"
