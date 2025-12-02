import math
inp = list(map(int, open("../../input.txt").read().split(',')))
max_len = len(inp) - 1
period_result = []

for period in range(1,max_len):
    i = 0
    new_inp = inp.copy()
    violation = False
    for i in range(period-1, max_len+1, period):
        if inp[i] == 0:
            violation = True
            break
        new_inp[i] -= 1
    if not violation:
        period_result.append(period)
        inp = new_inp.copy()

print(math.prod(period_result))
