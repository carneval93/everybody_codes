import math
inp = open("../../input.txt").read().splitlines()

dragon_positions = set()
sheep_positions = set()
grid = {}
row_ind = 0
for row in inp:
    col_ind = 0
    for col in row:
        grid[(row_ind, col_ind)] = col
        if col == 'D':
            dragon_positions.add((row_ind,col_ind))
        if col == 'S':
            sheep_positions.add((row_ind,col_ind))
        col_ind += 1
    row_ind +=1

new_dragon_positions = dragon_positions.copy()
for i in range(4):
    for d in dragon_positions:
        new_pos = (d[0] + 2, d[1] + 1)
        if new_pos in grid:
            new_dragon_positions.add(new_pos)
        new_pos = (d[0] + 2, d[1] - 1)
        if new_pos in grid:
            new_dragon_positions.add(new_pos)
        new_pos = (d[0] - 2, d[1] + 1)
        if new_pos in grid:
            new_dragon_positions.add(new_pos)
        new_pos = (d[0] - 2, d[1] - 1)
        if new_pos in grid:
            new_dragon_positions.add(new_pos)
        new_pos = (d[0] + 1, d[1] + 2)
        if new_pos in grid:
            new_dragon_positions.add(new_pos)
        new_pos = (d[0] + 1, d[1] - 2)
        if new_pos in grid:
            new_dragon_positions.add(new_pos)
        new_pos = (d[0] - 1, d[1] + 2)
        if new_pos in grid:
            new_dragon_positions.add(new_pos)
        new_pos = (d[0] - 1, d[1] - 2)
        if new_pos in grid:
            new_dragon_positions.add(new_pos)
    dragon_positions = new_dragon_positions.copy()


print(len(dragon_positions & sheep_positions))
