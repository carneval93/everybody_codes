def get_pythagoras_result(Xv, Yv, Xc, Yc):
    return (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc)


def get_all_neighbours(pos):
    neighbours = []
    neighbours.append((pos[0], pos[1]+1))
    neighbours.append((pos[0], pos[1]-1))
    neighbours.append((pos[0]+1, pos[1]))
    neighbours.append((pos[0]-1, pos[1]))
    return neighbours


def dijkstra(start_node, m_time):
    visited = {}
    queue = [(start_node, 0)]
    while queue:
        queue.sort(key=lambda x: x[1])
        node_to_check, node_cost = queue.pop(0)
        for neighbour in get_all_neighbours(node_to_check):
            if neighbour not in grid_dict:
                continue
            cost = grid_dict[neighbour]
            if (cost + node_cost) >= m_time:
                continue
            if neighbour in visited.keys() and (cost + node_cost) >= visited[neighbour]:
                continue
            visited[neighbour] = (cost + node_cost)
            queue.append((neighbour, node_cost + cost))
    return visited


inp = open("../../input.txt").read().splitlines()

left_middle_border = set()
down_middle_border = set()
right_middle_border = set()
grid_dict = {}
start = ()
middle = ()

row_ind = 0
for row in inp:
    col_ind = 0
    for val in row:
        if val == '@':
            middle = (row_ind, col_ind)
        elif val == 'S':
            start = (row_ind, col_ind)
            grid_dict[(row_ind, col_ind)] = 0
        else:
            if row_ind == int(len(inp) / 2):
                if col_ind < int(len(inp[0]) / 2):
                    left_middle_border.add((row_ind, col_ind))
                elif col_ind > int(len(inp[0]) / 2):
                    right_middle_border.add((row_ind, col_ind))
            if col_ind == int(len(inp[0]) / 2):
                if row_ind > int(len(inp) / 2):
                    down_middle_border.add((row_ind, col_ind))
            grid_dict[(row_ind, col_ind)] = int(val)
        col_ind += 1
    row_ind += 1

max_radius = int(len(inp[0])/2)

diff_dict = {}

max_time = 0

for radius in range(max_radius+1):
    result = []
    found = False
    c1 = 0
    c2 = 0
    c3 = 0
    t1 = max_time
    t2 = max_time
    t3 = max_time
    d_start = dijkstra(start, max_time)
    for ml in left_middle_border & d_start.keys():
        c1 = d_start[ml]
        t1 = max_time - d_start[ml]
        d_ml = dijkstra(ml, t1)
        for dm in down_middle_border & d_ml.keys():
            c2 = d_ml[dm]
            t2 = t1 - d_ml[dm]
            d_dm = dijkstra(dm, t2)
            for rm in right_middle_border & d_dm.keys():
                c3 = d_dm[rm]
                t3 = t2 - d_dm[rm]
                d_start_back = d_start[rm] - grid_dict[rm]
                if d_start_back < t3:
                    result.append((c1+c2+c3+d_start_back, radius-1))
                    found = True
    max_time += 30
    new_dict = grid_dict.copy()
    for pos, value in grid_dict.items():
        if get_pythagoras_result(middle[0], middle[1], pos[0], pos[1]) <= radius * radius:
            del (new_dict[pos])
            if pos in left_middle_border:
                left_middle_border.remove(pos)
            if pos in down_middle_border:
                down_middle_border.remove(pos)
            if pos in right_middle_border:
                right_middle_border.remove(pos)
    grid_dict = new_dict.copy()

    if found:
        result = sorted(
            result,
            key=lambda x: x[0]
        )
        print(result[0][0]*result[0][1])
        break