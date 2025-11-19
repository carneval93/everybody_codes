import sys
sys.setrecursionlimit(1500)


def get_neighbours(node):
    neighbours = [(node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])]
    return neighbours


def depth_search(start_node, v_nodes):
    global temp_cache
    for adjacent in get_neighbours(start_node):
        if adjacent in v_nodes or adjacent not in grid_dict or int(grid_dict[adjacent]) > int(grid_dict[start_node]):
            continue
        v_nodes.add(adjacent)
        if adjacent in temp_cache:
            v_nodes |= temp_cache[adjacent]
        else:
            v_nodes |= depth_search(adjacent, v_nodes.copy())
    return v_nodes


inp = open("../../input.txt").read().splitlines()

grid_dict = {}

row_ind = 0
for row in inp:
    col_ind = 0
    for val in row:
        grid_dict[(row_ind, col_ind)] = int(val)
        col_ind += 1
    row_ind += 1


result = set()

for i in range(3):
    temp_result = set()
    temp_cache = {}
    next_chain = set(grid_dict.keys()).difference(set(result))
    for pos in next_chain:
        tmp_visited = depth_search(pos, result | {pos})
        temp_cache[pos] = tmp_visited.copy()
        if len(tmp_visited) > len(temp_result):
            temp_result = tmp_visited.copy()
    result = temp_result.copy()

print(len(result))
