inp = list(map(int, open("../../input.txt").read().splitlines()))

rnd = 0
move = True
while move:
    move = False
    for step in range(len(inp)-1):
        first_in_step = step
        second_in_step = step + 1
        if inp[second_in_step] < inp[first_in_step]:
            move = True
            inp[first_in_step] -= 1
            inp[second_in_step] += 1
    rnd += 1


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