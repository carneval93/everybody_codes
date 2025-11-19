def get_neighbours(node):
    neighbours = [(node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])]
    return neighbours


def breadth_search(start_node, v_nodes):
    breadth_nodes = list()
    breadth_nodes.append(start_node)
    while breadth_nodes:
        new_breath_nodes = list()
        for b_node in breadth_nodes:
            for adjacent in get_neighbours(b_node):
                if adjacent in v_nodes or adjacent not in grid_dict or int(grid_dict[adjacent]) > int(grid_dict[b_node]):
                    continue
                v_nodes.append(adjacent)
                new_breath_nodes.append(adjacent)
        breadth_nodes = new_breath_nodes
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

print(len(breadth_search((0,0),[(0,0)])))