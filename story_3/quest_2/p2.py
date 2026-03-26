from collections import deque


def get_all_neighbours(node):
    neighbours = [(node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])]
    return neighbours


def breadth_search(start_node, v_nodes, obs_search):
    allowed = ['@', '#'] if not obs_search else ['@']
    breadth_nodes = list()
    breadth_nodes.append(start_node)
    while breadth_nodes:
        new_breath_nodes = list()
        for b_node in breadth_nodes:
            for adjacent in get_all_neighbours(b_node):
                if adjacent not in grid:
                    return set()
                if adjacent in v_nodes or grid[adjacent] in allowed:
                    continue
                v_nodes.add(adjacent)
                new_breath_nodes.append(adjacent)
        breadth_nodes = new_breath_nodes
    return v_nodes


def flood_obstacles(obs):
    f_points = set()
    found = True
    for o in obs:
        new_points = breadth_search(o, {o} | f_points, True)
        if not new_points:
            found = False
            break
        f_points |= new_points
    return found


def get_flooded_points(pos):
    to_test = [(pos[0]-1, pos[1]), (pos[0], pos[1]-1), (pos[0]+1, pos[1]), (pos[0], pos[1]+1)]
    flood_points = []
    for t in to_test:
        if grid[t] == '@' or grid[t] == '#':
            continue
        found = 0
        for right in range(t[1]+1,max_col):
            if grid[(t[0], right)] in ['@', '#']:
                found += 1
                break
        for left in list(reversed(range(min_col,t[1]))):
            if grid[(t[0], left)] in ['@', '#']:
                found += 1
                break
        for down in range(t[0]+1,max_row):
            if grid[(down, t[1])] in ['@', '#']:
                found += 1
                break
        for up in list(reversed(range(min_row, t[0]))):
            if grid[(up, t[1])] in ['@', '#']:
                found += 1
                break
        if found < 4:
            continue
        new_flood_points = breadth_search(t, {t}, False)
        if new_flood_points:
            flood_points += new_flood_points
    return flood_points


inp = open("../../input.txt").read().splitlines()

sequence = deque(['↑', '→', '↓', '←'])

grid = {}
col_ind = 0
row_ind = 0
start = ()
obstacles = set()
for row in inp:
    col_ind = 0
    for col in row:
        grid[(row_ind, col_ind)] = col
        if col == '@':
            start = (row_ind, col_ind)
        if col == '#':
            obstacles.add((row_ind, col_ind))
        col_ind += 1
    row_ind += 1

max_row = row_ind+20
max_col = col_ind+20
min_row = -20
min_col = -20

for row_ind in range(min_row,max_row):
    for col_ind in range(min_col,max_col):
        if (row_ind, col_ind) not in grid:
            grid[(row_ind, col_ind)] = '.'


step = 0
curr_pos = start
while True:
    new_pos = ()
    if sequence[0] == '↑':
        new_pos = (curr_pos[0] - 1, curr_pos[1])
    elif sequence[0] == '↓':
        new_pos = (curr_pos[0] + 1, curr_pos[1])
    elif sequence[0] == '→':
        new_pos = (curr_pos[0], curr_pos[1] + 1)
    elif sequence[0] == '←':
        new_pos = (curr_pos[0], curr_pos[1] - 1)
    if grid[new_pos] == '.':
        step += 1
        grid[new_pos] = '@'
        curr_pos = new_pos
        flooded_points = get_flooded_points(curr_pos)
        for i in flooded_points:
            grid[i] = '@'
        cnt = 0
        if flood_obstacles(obstacles):
            break
    sequence.rotate(-1)
print(step)
