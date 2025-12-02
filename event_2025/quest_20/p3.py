import math


def rotate_point(pos):
    new_col = pos[1] + pos[0]
    new_row = pos[0]
    rotated_row = len(inp[0]) - 1 - new_col
    rotated_col = new_row
    if rotated_row % 2 != 0:
        rotated_col = rotated_col * 2 + 1
        rotated_row = math.ceil(rotated_row / 2) - 1
    else:
        rotated_col = rotated_col * 2
        rotated_row = math.ceil(rotated_row / 2)
    rotated_col += rotated_row
    return rotated_row, rotated_col


def get_neighbours(pos, c_grid):
    value = 'T'
    pos_neighbours = []
    right = (pos[0], pos[1] + 1)
    if right in c_grid and c_grid[right] == value:
        pos_neighbours.append((right, 1))

    left = (pos[0], pos[1] - 1)
    if left in c_grid and c_grid[left] == value:
        pos_neighbours.append((left, 1))

    up = (pos[0] + 1, pos[1])
    down = (pos[0] - 1, pos[1])

    if (pos[0] % 2 == 0 and pos[1] % 2 != 0) or (pos[0] % 2 != 0 and pos[1] % 2 == 0):
        if up in c_grid and c_grid[up] == value:
            pos_neighbours.append((up, 1))
    else:
        if down in c_grid and c_grid[down] == value:
            pos_neighbours.append((down, 1))
    return pos_neighbours


def dijkstra(start_node, end_node):
    visited = {}
    queue = [(start_node, 0)]
    while end_node not in visited.keys():
        queue.sort(key=lambda x: x[1])
        possible_node_to_check, node_cost = queue.pop(0)
        node_to_check = rotate_point(possible_node_to_check)
        for neighbour in get_neighbours(node_to_check, grid_dict) + [(node_to_check,1)]:
            if grid_dict[neighbour[0]] == '#':
                continue
            if neighbour[0] in visited.keys() and (neighbour[1] + node_cost) >= visited[neighbour[0]]:
                continue
            visited[neighbour[0]] = (neighbour[1] + node_cost)
            queue.append((neighbour[0], node_cost + neighbour[1]))
    return visited[end_node]


inp = open("../../input.txt").read().splitlines()

grid_dict = {}

t_neighbours = 0

start = ()
end = ()

row_ind = 0
for row in inp:
    col_ind = 0
    for val in row:
        if val == '#' or val == 'T':
            grid_dict[(row_ind, col_ind)] = val
        elif val == 'S':
            start = (row_ind, col_ind)
            grid_dict[(row_ind, col_ind)] = 'T'
        elif val == 'E':
            end = (row_ind, col_ind)
            grid_dict[(row_ind, col_ind)] = 'T'
        col_ind += 1
    row_ind += 1

start_grid = 0

print(dijkstra(start, end))


