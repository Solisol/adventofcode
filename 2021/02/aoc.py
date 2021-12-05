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
        clean_line = line.strip()
        converted_list.append(tuple(clean_line.split(" ")))
    return converted_list

def one():
    # print command line arguments
    print ("This is one")
    # get input
    input = readInput()
    forward = 0
    depth = 0
    for x in range(len(input)):
        direction, length = input[x]
        if direction == "forward":
            forward += int(length)
        elif direction == "down":
            depth += int(length)
        elif direction == "up":
            depth -= int(length)
    print ("Forward {} and depth {}, multiple of {}".format(forward, depth, (forward * depth)))
    return 

def two():
    # print command line arguments
    print ("This is two")
    # get input
    input = readInput()
    forward = 0
    depth = 0
    aim = 0
    for x in range(len(input)):
        direction, length = input[x]
        if direction == "forward":
            forward += int(length)
            depth += (int(length) * aim)
        elif direction == "down":
            aim += int(length)
        elif direction == "up":
            aim -= int(length)
    print ("Forward {} and depth {}, multiple of {}".format(forward, depth, (forward * depth)))
    return 


def main():
    #one()
    two()
    

if __name__ == "__main__":
    main()


