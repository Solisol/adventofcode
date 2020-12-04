#!/usr/bin/python
import sys

def readInput(filename):
    path = filename
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    converted_list = []
    for line in lines:
        converted_list.append(int(line.strip()))
    return converted_list

def one(part):
    # print command line arguments
    print ("This is one")
    # get input
    filename = part + ".txt"
    input = readInput(filename)
    # print (input)
    for a in input:
        for b in input:
            if a + b == 2020:
                print ("{} and {} equals 2020").format(a,b)
                print (a * b)
                return

def two(part):
    # print command line arguments
    print ("This is one")
    # get input
    filename = part + ".txt"
    input = readInput(filename)
    # print (input)
    for a in input:
        for b in input:
            for c in input:
                if a + b + c == 2020:
                    print ("{} and {} and {} equals 2020").format(a,b,c)
                    print (a * b * c)
                    return

def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        print arg
    if sys.argv[1] == "1":
        one(sys.argv[2])
    elif sys.argv[1] == "2":
        two(sys.argv[2])
    else:
        print ("Unknown input: {}").format(sys.argv[1])
    

if __name__ == "__main__":
    main()


