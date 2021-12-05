#!/usr/bin/python
from os import close
import sys

def readInput():
    path = "input.txt"
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    converted_list = []
    for line in lines:
        converted_list.append(int(line.strip()))
    return converted_list

def calcInc(daList):
    increased = 0
    # print (input)
    for x in range(1, len(daList)):
        if daList[x] > daList[x-1]:
            increased += 1
    return increased

def one():
    # print command line arguments
    print ("This is one")
    # get input
    input = readInput()
    increased = calcInc(input)
    print ("Incread {} times".format(increased))
    return 

def triClone(input):
    clone = []
    x = 2
    while x < len(input):
        clone.append(input[x - 2] + input[x - 1] + input[x])
        x += 1
    return clone

def two():
    # print command line arguments
    print ("This is two")
    # get input
    input = readInput()
    clone = triClone(input)
    increased = calcInc(clone)
    print ("Incread {} times".format(increased))
    return

def main():
    #one()
    two()
    

if __name__ == "__main__":
    main()


