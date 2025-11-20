
inp = list(map(int, open("../../input.txt").read().splitlines()))

avg = sum(inp) / len(inp)

result = 0
for i in inp:
    result += abs(i - avg)

print(result/2)