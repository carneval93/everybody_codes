def get_all_neighbours(pos):
    neighbours = []
    neighbours.append(((pos[0] + 1, pos[1] + 1), 1))
    neighbours.append(((pos[0] + 1, pos[1] - 1), 0))
    return neighbours


def dijkstra(start_node, end_col):
    visited = {}
    queue = [(start_node, 0)]
    while end_col not in [x[0] for x in visited.keys()]:
        queue.sort(key=lambda x: x[1])
        node_to_check, node_cost = queue.pop(0)
        for neighbour in get_all_neighbours(node_to_check):
            if (neighbour[0] in visited.keys() and (neighbour[1] + node_cost) >= visited[neighbour[0]]) or neighbour[0] in wall or neighbour[0][1] < 0:
                continue
            visited[neighbour[0]] = (neighbour[1] + node_cost)
            queue.append((neighbour[0], node_cost + neighbour[1]))
    return visited[tuple(sorted(visited.keys(), key=lambda x: x[0])[-1])]

inp = open("../../input.txt").read().splitlines()

start = (0,0)
wall = set()
for segment in inp:
    segment_list = list(map(int, segment.split(',')))
    for i in range(segment_list[1]):
        wall.add((segment_list[0], i))
    for i in range(segment_list[1] + segment_list[2], 100):
        wall.add((segment_list[0], i))


print(dijkstra(start,segment_list[0]))





