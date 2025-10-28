inp = open("../../input.txt").read().splitlines()[0]

result = 0
while inp:
    first = inp[0]
    second = inp[1]
    third = inp[2]
    inp = inp[3:]

    for elem in [first, second, third]:
        if elem == 'B':
            result += 1
        elif elem == 'C':
            result += 3
        elif elem == 'D':
            result += 5

    if (first + second + third).count('x') == 0:
        result += 6
    elif (first + second + third).count('x') == 1:
        result += 2

print(result)