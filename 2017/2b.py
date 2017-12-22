file = open("inputs/2a.input", 'r')
input = [ map(int,line.split('\t')) for line in file ]
sum = 0
for x in input:
    for y in range(0, len(x)):
        current = x[y]
        for z in range(y +1, len(x)):
            if x[y] % x[z] == 0:
                sum = sum + (x[y] / x[z])
                break
            elif x[z] % x[y] == 0:
                sum = sum + (x[z] / x[y])
                break
print sum