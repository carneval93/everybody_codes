from collections import defaultdict


def depth_search(start_node, v_nodes):
    if start_node == '@':
        return v_nodes
    for adjacent in tree_dict[start_node]:
        if adjacent in v_nodes:
            continue
        v_nodes.append(adjacent)
        ret = depth_search(adjacent, v_nodes)
        if ret:
            global_nodes.append(ret.copy())
        v_nodes.pop()
    return []


inp = open("../../input.txt").read().splitlines()
tree_dict = defaultdict(list)

for node in inp:
    origin = node.split(':')[0]
    targets = node.split(':')[1].split(',')
    tree_dict[origin] = targets

global_nodes = []
depth_search('RR', ['RR'])
len_count_dict = defaultdict(int)
for i in global_nodes:
    len_count_dict[len(i)] += 1
unique_len = [k for k, v in len_count_dict.items() if v == 1][0]
for j in global_nodes:
    if len(j) == unique_len:
        first_letters_only = ''
        for ch in j:
            first_letters_only += ch[0]
        print(first_letters_only)