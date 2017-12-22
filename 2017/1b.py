file = open("inputs/1a.input")
incoming = file.read()
split = list(incoming)
split = map(int, split)
steps = len(split) / 2
sum = 0
for x in range(0, len(split)):
    if split[x] == split[(x + steps) % len(split)]:
        sum = sum + split[x]
print sum
