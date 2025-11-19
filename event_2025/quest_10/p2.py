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

sheep_eaten = 0

turn = 'dragon'
for i in range(40):
    if turn == 'dragon':
        turn = 'sheep'
        new_dragon_positions = set()
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
    elif turn == 'sheep':
        turn = 'dragon'
        new_sheep_positions = set()
        for s in sheep_positions:
            new_pos = (s[0] + 1, s[1])
            if new_pos in grid:
                new_sheep_positions.add(new_pos)
        sheep_positions = new_sheep_positions.copy()

    possible_eating_positions = dragon_positions & sheep_positions
    for p in possible_eating_positions:
        if grid[p] != '#':
            sheep_positions.remove(p)
            sheep_eaten += 1

print(sheep_eaten)