def get_neighbours(node, curr_dict):
    neighbours = 0
    for next_pos in [(1,1), (1,-1), (-1,1), (-1,-1)]:
        if (node[0] + next_pos[0], node[1] + next_pos[1]) in curr_dict and curr_dict[(node[0] + next_pos[0],node[1] + next_pos[1])] == '#':
            neighbours += 1
    return neighbours


inp = open("../../input.txt").read().splitlines()

grid_dict = {}
row_num = 0
for row in inp:
    col_num = 0
    for col in row:
        grid_dict[(row_num, col_num)] = col
        col_num += 1
    row_num += 1

result = 0

for i in range(10):
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
    grid_dict = new_grid.copy()
    result += list(grid_dict.values()).count('#')
print(result)