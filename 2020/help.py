
def readInput(filename):
    path = "inputs/" + filename
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    converted_list = []
    for line in lines:
        converted_list.append(int(line.strip()))
    return converted_list