def get_all_neighbours(pos):
    neighbours = []
    neighbours.append(((pos[0], pos[1]+1), 1))
    neighbours.append(((pos[0], pos[1]-1), 1))
    neighbours.append(((pos[0]+1, pos[1]), 1))
    neighbours.append(((pos[0]-1, pos[1]), 1))
    return neighbours


def dijkstra(start_node, end_node):
    visited = {}
    queue = [(start_node, 0)]
    while end_node not in visited.keys():
        queue.sort(key=lambda x: x[1])
        node_to_check, node_cost = queue.pop(0)
        for neighbour in get_all_neighbours(node_to_check):
            if (neighbour[0] in visited.keys() and (neighbour[1] + node_cost) >= visited[neighbour[0]]) or neighbour[0] in walls:
                continue
            visited[neighbour[0]] = (neighbour[1] + node_cost)
            queue.append((neighbour[0], node_cost + neighbour[1]))
    return visited[end_node]


def move(h, amt, curr_pos):
    next_walls = list()
    if h == 'right':
        for i in range(1, amt+1):
            next_walls.append((curr_pos[0] + i, curr_pos[1]))
    elif h == 'down':
        for i in range(1, amt+1):
            next_walls.append((curr_pos[0], curr_pos[1] + i))
    elif h == 'left':
        for i in range(1, amt+1):
            next_walls.append((curr_pos[0] - i, curr_pos[1]))
    elif h == 'up':
        for i in range(1, amt+1):
            next_walls.append((curr_pos[0], curr_pos[1] - i))
    return set(next_walls), next_walls[-1]


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
walls = set()
curr_pos = S

for step in inp:
    amount = 0
    direction = ''
    if 'R' in step:
        direction = 'R'
        amount = int(step.split('R')[1])
    elif 'L' in step:
        direction = 'L'
        amount = int(step.split('L')[1])
    next_heading = get_heading(curr_heading, direction)
    new_walls, curr_pos = move(next_heading, amount, curr_pos)
    walls |= new_walls
    curr_heading = next_heading

E = curr_pos
walls.remove(E)

max_costs = (abs(S[0]-E[0]) + abs(S[1]-E[1]))*3
print(dijkstra(S,E))
