input = 12
sum = 0
for x in range(61, 0, -2):
    max = x * x
    if max == 1:
        print sum
        break
    if max <= input:
        y = x - 2
        ran = max - y * y
        line = ran /4
        print line
        first = max
        second = max - line
        third = max - line*2
        fourth = max - line *3
        print first, second, third, fourth
        if input == fourth:
            sum = sum + 2
        elif input == third:
            sum = sum + 2
        elif input == second:
            sum = sum + 2
        elif input == first:
            sum = sum + 2
        else:
            sum = sum +1

