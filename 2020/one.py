import sys
from help import readInput

def one(part):
    # print command line arguments
    print ("This is one")
    # get input
    filename = "1." + part + ".txt"
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
    filename = "1." + part + ".txt"
    input = readInput(filename)
    # print (input)
    for a in input:
        for b in input:
            for c in input:
                if a + b + c == 2020:
                    print ("{} and {} and {} equals 2020").format(a,b,c)
                    print (a * b * c)
                    return

def entry(part):
    if part == "1" or part == "example1":
        one(part)
    elif part == "2" or part == "example2":
        two(part)
    else:
        print ("unknown part")
