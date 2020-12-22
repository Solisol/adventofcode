import sys

def readInput(filename):
    path = filename
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    converted_list = []
    for line in lines:
        converted_list.append(list(line.strip()))
    return converted_list


def slope(filename, input_down, input_right):
    lines = readInput(filename)
    right = input_right
    down = input_down
    tree_hits = 0
    input_lenght = len(lines[0])
    while (down < len(lines)):
        if lines[down][right%input_lenght] == '#':
            tree_hits = tree_hits + 1
        down = down + input_down
        right = right + input_right
    print("Trees hit for down {} and right {}: {}").format(input_down, input_right, tree_hits)
    return tree_hits

def one(filename):
    slope(filename, 1, 3)

def two(filename):
    total = slope(filename, 1, 1) * slope(filename, 1, 3) * slope(filename, 1, 5) * slope(filename, 1, 7) *slope(filename, 2, 1)
    print("Total: {}").format(total)

def main():
    if sys.argv[1] == "1":
        one(sys.argv[2])
    elif sys.argv[1] == "2":
        two(sys.argv[2])
    else:
        print ("Unknown input: {}").format(sys.argv[1])
    

if __name__ == "__main__":
    main()