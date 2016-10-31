#!/usr/bin/env python
#
# Ian Palleiko
# For Python 3.5
#
import os

def getFiles():
    # Searches through dir and creates list of names of .txt files
    textFiles = []
    counter = 0

    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            counter += 1
            textFiles.append(file)
            print("(%d) %s" % (counter, file)) # Prints list of usable files and their numbers
    return textFiles  

# The selDict function lets you select what dictionary(s) you want to use
def selDict():
    textFiles = getFiles()
    usedDicts = []
    selectionStr = input()
    selectionStr = selectionStr.replace(" ", "") # Removes white space
    selectionList = selectionStr.split(",") # Creates list from string split at commas
    selectionList = list(map(int, selectionList)) # Changes list values from str to int
    checkSel(textFiles, selectionList)

    for x in range(len(selectionList)):
        usedDicts.append(textFiles[selectionList[x] - 1])
        print(usedDicts)

# Makes sure that selection is valid
def checkSel(textFiles, selectionList):
    for x in range(len(selectionList)):
        if(selectionList[x] <= 0 or selectionList[x] > len(textFiles)):
            print("%d is not a valid selection. Please select again" % (selectionList[x]))
            selDict()
            quit()

    print(textFiles) # for debug use


print("Which password dictionary do you want to use?")
print("If you would like to use multiple dictionaries enter the numbers separated by commas in order wanted.")
print("Example: '1, 4, 2'")
selDict()
