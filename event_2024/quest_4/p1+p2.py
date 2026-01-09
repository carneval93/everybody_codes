inp = list(map(int, open("../../input.txt").read().splitlines()))

min_nail = min(inp)

result = 0

for i in inp:
    result += i - min_nail

print(result)

