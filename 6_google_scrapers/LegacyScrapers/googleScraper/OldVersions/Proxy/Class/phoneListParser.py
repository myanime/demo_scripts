# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.proxy import *
import threading
import time
import itertools
import csv
import urllib2
import socket
import random
import logging
import sys
import codecs


logging.basicConfig(level=logging.INFO, filename="googleScraper.log")

listLoad = ["1.csv", "2.csv", "3.csv", "4.csv", "5.csv", "6.csv", "7.csv", "8.csv", "9.csv", "10.csv", "11.csv", "12.csv", "13.csv", "14.csv", "15.csv", "16.csv", "17.csv", "18.csv", "19.csv", "20.csv", "21.csv", "22.csv", "23.csv", "24.csv", "25.csv"]
listSave = ["phone1.txt", "phone2.txt", "phone3.txt", "phone4.txt", "phone5.txt", "phone6.txt", "phone7.txt", "phone8.txt", "phone9.txt", "phone10.txt", "phone11.txt", "phone12.txt", "phone13.txt", "phone14.txt", "phone15.txt", "phone16.txt", "phone17.txt", "phone18.txt", "phone19.txt", "phone20.txt","phone21.txt", "phone22.txt", "phone23.txt", "phone24.txt", "phone25.txt"]
listNumber = ["Thread 1", "Thread 2", "Thread 3", "Thread 4", "Thread 5", "Thread 6", "Thread 7", "Thread 8", "Thread 9", "Thread 10", "Thread 11", "Thread 12", "Thread 13", "Thread 14", "Thread 15", "Thread 16", "Thread 17", "Thread 18", "Thread 19", "Thread 20", "Thread 21", "Thread 22", "Thread 23", "Thread 24", "Thread 25"]
threadInt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
proxyStartNumber = [416, 49, 617, 60, 80, 100, 220, 140, 160, 180]
currentRowInSearchListArray = [400, 49, 617, 42, 269, 57, 260, 494, 49, 488, 486, 179, 264, 481, 277, 683, 725, 484, 861, 488, 478, 485, 581, 467, 432]
#urrentRowInSearchListArray = [01, 20, 300, 40, 500, 600, 700, 800, 900, 100]
restartModule = [None] * 25



                


def startx():
    fullText = ""
    maxX = [None] * 25
    for number in range (0, 25):
        myFileNameLoad = "./phonenumbers/" + listSave[number]
        myFileNameSave = "./csv/" + listLoad[number]
        myThreadNumber = listNumber[number]
        iterationNumber = currentRowInSearchListArray[number]
        numberArrayX = [None] * 4000
        x = 0
        with open(myFileNameLoad, 'rb') as myList:
            myCSV = csv.reader(myList, delimiter=',', quotechar='|')
            for nameAndPostCode in itertools.islice(myCSV, iterationNumber, 10000):
                 numberArrayX[x] = int(nameAndPostCode[0])
                 
                 #print numberArrayX[x]
                 x = x + 1
        #print numberArrayX[222]
        maxX[number] = max(numberArrayX)
    for x in range (0, 25):
        print maxX[x]
        fullText = fullText + ", " + str(maxX[x] + 1)
    print fullText

def main():
    startx()


if __name__ == '__main__':
    main()

