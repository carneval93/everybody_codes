num_list_grid = open("../../input.txt").read().splitlines()

res_list = []
for num in num_list_grid:
    sword_id = int(num.split(':')[0])
    num_sub_level = ''
    num_list = list(map(int, num.split(':')[1].split(',')))

    spine_right_neighbours = {}
    spine_left_neighbours = {}
    spine_list = []
    rnd = 1
    for i in num_list:
        found = False
        for spine_tuple in spine_list:
            spine = spine_tuple[1]
            if spine_tuple not in spine_left_neighbours and i < spine:
                spine_left_neighbours[spine_tuple] = i
                found = True
                break
            elif spine_tuple not in spine_right_neighbours and i > spine:
                spine_right_neighbours[spine_tuple] = i
                found = True
                break
        if not found:
            spine_list.append((rnd, i))
        rnd += 1

    for s in spine_list:
        spine_sub_level = ''
        if s in spine_left_neighbours:
            spine_sub_level += str(spine_left_neighbours[s])
        spine_sub_level += str(s[1])
        if s in spine_right_neighbours:
            spine_sub_level += str(spine_right_neighbours[s])
        num_sub_level += "{:03d}".format(int(spine_sub_level))
    res_list.append((sword_id, int("".join(map(str, [x[1] for x in spine_list]))), num_sub_level))

res_list = sorted(
    res_list,
    key=lambda x: (x[1], x[2], x[0]),
    reverse=True
)

result = 0
i = 1
for r in res_list:
    result += i * r[0]
    i += 1

print(result)