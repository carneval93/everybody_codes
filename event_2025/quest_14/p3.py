def get_neighbours(node, curr_dict):
    neighbours = 0
    for next_pos in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if (node[0] + next_pos[0], node[1] + next_pos[1]) in curr_dict and curr_dict[(node[0] + next_pos[0],node[1] + next_pos[1])] == '#':
            neighbours += 1
    return neighbours


inp = open("../../input.txt").read().splitlines()

grid_dict = {}
row_num = 0
for row in range(34):
    col_num = 0
    for col in range(34):
        grid_dict[(row_num, col_num)] = '.'
        col_num += 1
    row_num += 1

picture_dict = {}
row_num = 13
for row in inp:
    col_num = 13
    for col in row:
        picture_dict[(row_num, col_num)] = col
        col_num += 1
    row_num += 1


pic_result = {}
cache = {}

for i in range(1,1000000001):
    values = tuple(grid_dict.values())
    if values in cache:
        result = sum(pic_result.values()) * (1000000000 // (i-cache[values]))
        for rnd, amount in pic_result.items():
            if rnd <= 1000000000 % (i-cache[values]):
                result += amount
        print(result)
        break
    cache[values] = i
    new_grid = {}
    for pos, val in grid_dict.items():
        if val == '.':
            if get_neighbours(pos, grid_dict) % 2 == 0:
                new_grid[pos] = '#'
            else:
                new_grid[pos] = '.'
        elif val == '#':
            if get_neighbours(pos, grid_dict) % 2 == 0:
                new_grid[pos] = '.'
            else:
                new_grid[pos] = '#'
    grid_dict = new_grid

    found = True
    for pos, val in picture_dict.items():
        if grid_dict[pos] != val:
            found = False

    if found:
        pic_result[i] = list(grid_dict.values()).count('#')

