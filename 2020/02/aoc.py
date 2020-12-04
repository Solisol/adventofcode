import sys

def readInput(filename):
    path = filename
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    converted_list = []
    for line in lines:
        converted_list.append(line.strip())
    return converted_list

def parse(line):
    parts = line.split()
    min_max = parts[0].split("-")
    key = parts[1][:1]
    password = parts[2]
    return min_max[0], min_max[1], key, password

def valid(min, max, key, password):
    occurences = password.count(key)
    # print ("Key: {}, Password: {}, Occurances: {}").format(key, password, occurences)
    if occurences >= int(min) and occurences <= int(max):
        return True
    else:
        return False

def one(path):
    filename = path + ".txt"
    lines = readInput(filename)
    nr_valid = 0
    for line in lines:
        min, max, key, password = parse(line)
        if valid(min, max, key, password) == True:
            nr_valid = nr_valid + 1
    print ("Valid passwords are: {}").format(nr_valid)

def validTwo(min, max, key, password):
    first = password[int(min) - 1:int(min)]
    second = password[int(max) - 1 :int(max)]
    if (first == key and second != key) or (first != key and second == key):
        return True
    else:
        return False

def two(path):
    filename = path + ".txt"
    lines = readInput(filename)
    nr_valid = 0
    for line in lines:
        min, max, key, password = parse(line)
        if validTwo(min, max, key, password) == True:
            nr_valid = nr_valid + 1
    print ("Valid passwords are: {}").format(nr_valid)

def main():
    # print command line arguments
    #for arg in sys.argv[1:]:
    #    print arg
    if sys.argv[1] == "1":
        one(sys.argv[2])
    elif sys.argv[1] == "2":
        two(sys.argv[2])
    else:
        print ("Unknown input: {}").format(sys.argv[1])
    

if __name__ == "__main__":
    main()