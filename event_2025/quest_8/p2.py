steps = list(map(int, open("../../input.txt").read().split(',')))
knots = 256
nodes = 0
last_step = steps[0]
connections = {}
for s in steps[1:]:
    start = sorted([s,last_step])[0]
    end = sorted([s,last_step])[1]
    indices = range(start+1, end)
    for i in indices:
        if i in connections:
            connected_nodes = connections[i].copy()
            for n in connected_nodes:
                if n < start or n > end:
                    nodes += 1
    if start in connections:
        connections[start].append(end)
    else:
        connections[start] = [end]
    if end in connections:
        connections[end].append(start)
    else:
        connections[end] = [start]
    last_step = s

print(nodes)
