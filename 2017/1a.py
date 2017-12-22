file = open("inputs/1a.input")
incoming = file.read()
split = list(incoming)
split = map(int, split)
sum = 0
for x in range(0, len(split)):
    if x == len(split) -1:
        if split[x] == split[0]:
            sum = sum + split[x]
    else:
        if split[x] == split[x+1]:
            sum = sum + split[x]
print sum
