def get_all_neighbours(pos):
    neighbours = []
    neighbours.append(((pos[0] + 1, pos[1] + 1), 1))
    neighbours.append(((pos[0] + 1, pos[1] - 1), 0))
    return neighbours


def dijkstra(start_node, end_col):
    global hole
    visited = {}
    queue = [(start_node, 0)]
    while end_col not in [x[0] for x in visited.keys()]:
        queue.sort(key=lambda x: x[1])
        node_to_check, node_cost = queue.pop(0)
        for neighbour_h_range, neighbour_distance in hole[transitions[node_to_check[0]]]:
            for hole_pos_height in range(neighbour_h_range[0], neighbour_h_range[1]+1):
                hole_pos = (neighbour_distance, hole_pos_height)
                if hole_pos[0] - node_to_check[0] < hole_pos[1] - node_to_check[1]:
                    continue
                if hole_pos[0] - node_to_check[0] < node_to_check[1] - hole_pos[1]:
                    continue
                if ((hole_pos[0] - node_to_check[0]) + (hole_pos[1] - node_to_check[1])) % 2 > 0:
                    continue
                curr_costs = int(((hole_pos[0] - node_to_check[0]) + (hole_pos[1] - node_to_check[1])) / 2)
                if (hole_pos[0], hole_pos[1]) in visited.keys() and (curr_costs + node_cost) >= visited[(hole_pos[0], hole_pos[1])]:
                    continue
                visited[(hole_pos[0], hole_pos[1])] = (curr_costs + node_cost)
                queue.append(((hole_pos[0], hole_pos[1]), node_cost + curr_costs))
    candidates = [t for t in visited.keys() if t[0] == end_col]
    candidates_costs = []
    for c in candidates:
        candidates_costs.append(visited[c])
    return min(candidates_costs)


inp = open("../../input.txt").read().splitlines()

start = (0,0)

transitions = {}
curr_c = 0
for segment in inp:
    segment_list = list(map(int, segment.split(',')))
    if segment_list[0] not in transitions:
        transitions[curr_c] = segment_list[0]
        curr_c = segment_list[0]


holes = set()
last_col = 0
hole = {}
for segment in inp:
    segment_list = list(map(int, segment.split(',')))
    if segment_list[0] in hole:
        hole[segment_list[0]].append(((segment_list[1], segment_list[1] + segment_list[2] - 1), segment_list[0]))
    else:
        hole[segment_list[0]] = [((segment_list[1], segment_list[1] + segment_list[2] - 1), segment_list[0])]


print(dijkstra(start,segment_list[0]))





