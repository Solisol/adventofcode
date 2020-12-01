#!/usr/bin/python
import one
import sys



def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        print arg
    if sys.argv[1] == "1":
        one.entry(sys.argv[2])
    

if __name__ == "__main__":
    main()