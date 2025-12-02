def dijkstra(start_node, end_node):
    visited = {}
    queue = [(start_node, 0)]
    while end_node not in visited.keys():
        queue.sort(key=lambda x: x[1])
        node_to_check, node_cost = queue.pop(0)
        for neighbour in neighbours[node_to_check]:
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
    row_ind +=1

neighbours = {}

for pos, val in grid_dict.items():
    if val == '#':
        continue
    pos_neighbours = []
    right = (pos[0], pos[1] + 1)
    if right in grid_dict and grid_dict[right] == val:
        pos_neighbours.append((right, 1))

    left = (pos[0], pos[1] - 1)
    if left in grid_dict and grid_dict[left] == val:
        pos_neighbours.append((left, 1))

    up = (pos[0] + 1, pos[1])
    down = (pos[0] - 1, pos[1])

    if (pos[0] % 2 == 0 and pos[1] % 2 != 0) or (pos[0] % 2 != 0 and pos[1] % 2 == 0):
        if up in grid_dict and grid_dict[up] == val:
            pos_neighbours.append((up, 1))
    else:
        if down in grid_dict and grid_dict[down] == val:
            pos_neighbours.append((down, 1))
    neighbours[pos] = pos_neighbours

print(dijkstra(start, end))


