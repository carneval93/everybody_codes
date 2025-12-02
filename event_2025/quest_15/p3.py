from collections import defaultdict


def ranges_intersect(t1, t2):
    #return min(t2[0]) <= min(t1[0]) <= max(t2[0]) and min(t2[1]) <= min(t1[1]) <= max(t2[1])

    (x1_min, y1_min), (x1_max, y1_max) = t1
    (x2_min, y2_min), (x2_max, y2_max) = t2

    x1_min, x1_max = min(x1_min, x1_max), max(x1_min, x1_max)
    y1_min, y1_max = min(y1_min, y1_max), max(y1_min, y1_max)
    x2_min, x2_max = min(x2_min, x2_max), max(x2_min, x2_max)
    y2_min, y2_max = min(y2_min, y2_max), max(y2_min, y2_max)

    x_overlap = x1_min <= x2_max and x2_min <= x1_max
    y_overlap = y1_min <= y2_max and y2_min <= y1_max

    return x_overlap and y_overlap


def get_all_neighbours(pos):
    return neighbours[pos]


def dijkstra(start_node, end_node):
    visited = {}
    queue = [(start_node, 0)]
    while end_node not in visited.keys():
        queue.sort(key=lambda x: x[1])
        node_to_check, node_cost = queue.pop(0)
        for neighbour in get_all_neighbours(node_to_check):
            if neighbour[0] in visited.keys() and (neighbour[1] + node_cost) >= visited[neighbour[0]]:
                continue
            visited[neighbour[0]] = (neighbour[1] + node_cost)
            queue.append((neighbour[0], node_cost + neighbour[1]))
    return visited[end_node]


def move(h, amt, pos):
    new_pos = ()
    if h == 'right':
        new_pos = (pos[0], pos[1] + amt)
    elif h == 'down':
        new_pos = (pos[0] + amt, pos[1])
    elif h == 'left':
        new_pos = (pos[0], pos[1] - amt)
    elif h == 'up':
        new_pos = (pos[0] - amt, pos[1])
    return new_pos


def get_heading(c_heading, d):
    if c_heading == 'right':
        if d == 'R':
            return 'down'
        elif d == 'L':
            return 'up'
    elif c_heading == 'down':
        if d == 'R':
            return 'left'
        elif d == 'L':
            return 'right'
    elif c_heading == 'left':
        if d == 'R':
            return 'up'
        elif d == 'L':
            return 'down'
    elif c_heading == 'up':
        if d == 'R':
            return 'right'
        elif d == 'L':
            return 'left'


inp = open("../../input.txt").read().split(',')

S = (0,0)
curr_heading = 'up'
walls = []
grid_rows = set()
grid_cols = set()
curr_pos = S

cnt = 0
for step in inp:
    cnt += 1
    amount = 0
    direction = ''
    if 'R' in step:
        direction = 'R'
        amount = int(step.split('R')[1])
    elif 'L' in step:
        direction = 'L'
        amount = int(step.split('L')[1])
    if cnt == len(inp):
        amount -= 1
    next_heading = get_heading(curr_heading, direction)
    n_pos = move(next_heading, amount, curr_pos)
    if curr_pos == S:
        if 'R' in step:
            curr_pos = (0,1)
        else:
            curr_pos = (0,-1)

    grid_rows.add(n_pos[0] + 1)
    grid_rows.add(n_pos[0] - 1)
    grid_cols.add(n_pos[1] + 1)
    grid_cols.add(n_pos[1] - 1)
    walls.append((curr_pos, n_pos))
    curr_pos = n_pos
    curr_heading = next_heading

curr_pos = move(curr_heading, 1, curr_pos)

E = (curr_pos[0], curr_pos[1])

grid_rows.add(0)
grid_cols.add(0)
grid_rows.add(E[0])
grid_cols.add(E[1])

grid_nodes = set()
for v1 in grid_rows:
    for v2 in grid_cols:
        grid_nodes.add((v1,v2))

neighbours = defaultdict(set)

checked = set()
cnt = 0
for from_nodes in grid_nodes:
    print(f'{cnt} of {len(grid_nodes)}')
    cnt += 1
    for to_nodes in grid_nodes:
        if from_nodes == to_nodes or tuple({from_nodes, to_nodes}) in checked:
            continue
        checked.add(tuple({from_nodes, to_nodes}))
        node_pair = (from_nodes, to_nodes)
        intersection = False
        for wall_start, wall_end in walls:
            wall_pair = (wall_start, wall_end)
            if ranges_intersect(node_pair, wall_pair):
                intersection = True
                break
        if intersection:
            continue
        diff_costs = abs(to_nodes[0] - from_nodes[0]) + abs(to_nodes[1] - from_nodes[1])
        neighbours[from_nodes].add((to_nodes, diff_costs))
        neighbours[to_nodes].add((from_nodes, diff_costs))


print(dijkstra(S, E))
