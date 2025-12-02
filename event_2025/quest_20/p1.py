inp = open("../../input.txt").read().splitlines()

grid_dict = {}

t_neighbours = 0

row_ind = 0
for row in inp:
    col_ind = 0
    for val in row:
        if val == '#' or val == 'T':
            grid_dict[(row_ind, col_ind)] = val
        col_ind += 1
    row_ind +=1


for pos, val in grid_dict.items():
    if grid_dict[pos] == '#':
        continue
    right = (pos[0], pos[1] + 1)
    if right not in grid_dict:
        continue
    if grid_dict[right] == val:
        t_neighbours += 1

    up = (pos[0] + 1, pos[1])
    if up not in grid_dict:
        continue

    if (pos[0] % 2 == 0 and pos[1] % 2 != 0) or (pos[0] % 2 != 0 and pos[1] % 2 == 0):
        if grid_dict[up] == val:
            t_neighbours += 1


print(t_neighbours)


