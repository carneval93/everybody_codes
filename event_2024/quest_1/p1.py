inp = open("../../input.txt").read().splitlines()[0]

result = 0
for i in inp:
    if i == 'B':
        result += 1
    elif i == 'C':
        result += 3
print(result)