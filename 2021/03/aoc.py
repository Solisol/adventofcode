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
        converted_list.append(list(clean_line))
    return converted_list

def one():
    # print command line arguments
    print ("This is one")
    # get input
    input = readInput()
    sum_of_sums = []
    for x in input[0]:
        sum_of_sums.append(0)
    gamma = ""
    epsilon = ""
    max = len(input)
    for line in input:
        for x in range(len(line)):
            sum_of_sums[x] += int(line[x])
    for x in sum_of_sums:
        if x > (max/2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    power_consumption = int(gamma,2) * int(epsilon,2)
    print ("Gamma: {} and Epsilon: {}, with power consumption {}".format(gamma, epsilon, power_consumption))
    return
                

def ox(input):
    ret_list = input.copy()
    for x in range(len(input[0])):
        sum = 0
        dom = ""
        for line in ret_list:
            if line[x] == "1":
               sum += 1 
        if sum >= (len(ret_list)/2):
            dom = "1"
        else:
            dom = "0"
        print ("Most common: {}".format(dom))
        temp_list = ret_list.copy()
        for line in ret_list:
            if line[x] != dom:
                temp_list.remove(line)
            if len(temp_list) == 1:
                return temp_list[0]
        ret_list = temp_list

def co(input):
    ret_list = input.copy()
    for x in range(len(input[0])):
        sum = 0
        dom = ""
        for line in ret_list:
            if line[x] == "1":
               sum += 1 
        if sum >= (len(ret_list)/2):
            dom = "0"
        else:
            dom = "1"
        print ("Least common: {}".format(dom))
        temp_list = ret_list.copy()
        for line in ret_list:
            if line[x] != dom:
                temp_list.remove(line)
            if len(temp_list) == 1:
                return temp_list[0]
        ret_list = temp_list

def two():
    print ("This is two")
    input = readInput()
    ox_list = ox(input)
    co_list = co(input)
    oxy = int("".join(ox_list), 2)
    co2 = int("".join(co_list), 2)
    print ("{} and {}, multi: {}".format(oxy, co2, (oxy *co2))) 


def main():
    #one()
    two()
    

if __name__ == "__main__":
    main()


