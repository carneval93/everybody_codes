inp = open("../../input.txt").read().splitlines()[0]

result = 0
while inp:
    first = inp[0]
    second = inp[1]
    inp = inp[2:]

    for elem in [first, second]:
        if elem == 'B':
            result += 1
        elif elem == 'C':
            result += 3
        elif elem == 'D':
            result += 5

    if (first + second).count('x') == 0:
        result += 2

print(result)