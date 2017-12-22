file = open("inputs/2a.input", 'r')
input = [ map(int,line.split('\t')) for line in file ]
sum = 0
for x in input:
    min = x[0]
    max = x[0]
    for y in range(1, len(x)):
        if x[y] > max:
            max = x[y]
        if x[y] < min:
            min = x[y]
    sum = sum + (max - min)
print sum