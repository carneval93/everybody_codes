steps = list(map(int, open("../../input.txt").read().split(',')))

passed_middle = 0
last_step = steps[0]
for s in steps[1:]:
    if abs(s - last_step) == 16:
        passed_middle += 1
    last_step = s

print(passed_middle)