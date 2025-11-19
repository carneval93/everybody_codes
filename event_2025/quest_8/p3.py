import itertools

steps = list(map(int, open("../../input.txt").read().split(',')))
knots = 256
last_step = steps[0]
connections = {}
for s in steps[1:]:
    start = sorted([s, last_step])[0]
    end = sorted([s, last_step])[1]
    if start in connections:
        connections[start].append(end)
    else:
        connections[start] = [end]
    if end in connections:
        connections[end].append(start)
    else:
        connections[end] = [start]
    last_step = s

max_nodes = 0
for cut_pair in list(itertools.combinations(range(1, knots + 1), 2)):
    cut_pair_nodes = 0
    start = sorted([cut_pair[0], cut_pair[1]])[0]
    end = sorted([cut_pair[0], cut_pair[1]])[1]
    indices = range(start + 1, end)
    for i in indices:
        if i in connections:
            connected_nodes = connections[i].copy()
            for n in connected_nodes:
                if n < start or n > end:
                    cut_pair_nodes += 1
    if cut_pair_nodes > max_nodes:
        max_nodes = cut_pair_nodes
print(max_nodes)
