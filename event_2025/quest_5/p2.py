num_list_grid = open("../../input.txt").read().splitlines()

res_list = []
for num in num_list_grid:
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

    res_list.append(int("".join(map(str, [x[1] for x in spine_list]))))

print(max(res_list) - min(res_list))