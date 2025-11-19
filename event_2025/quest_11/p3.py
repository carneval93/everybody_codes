#in progress

inp = list(map(int, open("../../input.txt").read().splitlines()))

step = len(inp)-1
while step > 0:
    to_distribute = inp[step]
    if inp[step-1]
    step -= 1




move = True
while move:
    move = False
    for step in range(len(inp)-1):
        first_in_step = step
        second_in_step = step + 1
        if inp[second_in_step] > inp[first_in_step]:
            move = True
            inp[second_in_step] -= 1
            inp[first_in_step] += 1
    rnd += 1

print(rnd - 2)