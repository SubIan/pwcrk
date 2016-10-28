#!/usr/bin/env python
import os

def selDict():
    textFiles = []
    counter = 0
    print("Which password dictionary do you want to use?")
    print("If you would like to use multiple dictionaries enter the numbers seperated by commas in order wanted.")
    print("Example: '1, 4, 2'")

    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            counter += 1
            textFiles.append(file)
            print("(%d) %s" % (counter, file))
    selectionStr = input()
    selectionStr = selectionStr.replace(" ", "")
    selectionArr = selectionStr.split(",")
    print(selectionArr)
    print(textFiles)

selDict()
