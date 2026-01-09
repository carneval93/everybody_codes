inp = list(map(int, open("../../input.txt").read().splitlines()))

result = []
sorted_inp = sorted(inp)
for s in sorted_inp:
    s_result = 0
    min_nail = s
    for i in inp:
        s_result += abs(i - min_nail)
    result.append(s_result)

print(min(result))
