inp = open("../../input.txt").read().splitlines()

grid_dict = {}

row_ind = 0
for row in inp:
    col_ind = 0
    for val in row:
        if val == '.':
            grid_dict[(row_ind, col_ind)] = 0
        else:
            grid_dict[(row_ind, col_ind)] = val
        col_ind += 1
    row_ind += 1

total_dig_count = 0
while True:
    cnt_round = 0
    for pos, height in grid_dict.items():
        if height == 0:
            continue
        if height == '#':
            grid_dict[pos] = 1
            cnt_round += 1
        else:
            pass_pos = False
            for neighbour in [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]:
                if neighbour not in grid_dict or grid_dict[neighbour] < height:
                    pass_pos = True
            if not pass_pos:
                grid_dict[pos] += 1
                cnt_round += 1
    if cnt_round == 0:
        break
    total_dig_count += cnt_round
print(total_dig_count)