#!/usr/bin/env python
import os

# The selDict function lets you select what dictionary(s) you want to use
def selDict():
    textFiles = []
    counter = 0
    
    # Searches through dir and creates list of names of .txt files
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            counter += 1
            textFiles.append(file)
            print("(%d) %s" % (counter, file)) # Prints list of usable files and their numbers
            

    selectionStr = input()
    selectionStr = selectionStr.replace(" ", "") # Removes white space
    selectionList = selectionStr.split(",") # Creates list from string split at commas
    selectionList = list(map(int, selectionList)) # Changes list values from str to int

    # Makes sure that selection is valid
    for pos in selectionList:
        if(pos > len(textFiles) or pos < 1):
            print("%d is not a valid file. Please select again" % (selectionList[pos]))
            selDict()

    selFiles = []
    sel = 0
    #for x in textFiles:
    #    if(x == selectionList[sel]):
    #        selFiles.append(textFiles[pos - 1]
            #sel += 1
    # print(selFiles)
    # print(selectionList) # for debug use
    print(textFiles) # for debug use


print("Which password dictionary do you want to use?")
print("If you would like to use multiple dictionaries enter the numbers seperated by commas in order wanted.")
print("Example: '1, 4, 2'")
selDict()
