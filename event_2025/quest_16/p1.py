
inp = list(map(int, open("../../input.txt").read().split(',')))

blocks = 0

cols = 90

for i in inp:
    blocks += cols // i

print(blocks)