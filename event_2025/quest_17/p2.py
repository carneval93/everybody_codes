def get_pythagoras_result(Xv, Yv, Xc, Yc):
    return (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc)


inp = open("../../input.txt").read().splitlines()


grid_dict = {}
start = ()

row_ind = 0
for row in inp:
    col_ind = 0
    for val in row:
        if val == '@':
            start = (row_ind, col_ind)
        else:
            grid_dict[(row_ind, col_ind)] = int(val)
        col_ind += 1
    row_ind += 1

max_radius = int(len(inp[0])/2)

diff_dict = {}

for radius in range(1, max_radius+1):
    result = 0
    for pos, value in grid_dict.items():
        if get_pythagoras_result(start[0], start[1], pos[0], pos[1]) <= radius * radius:
            grid_dict[pos] = 0
            result += value
    diff_dict[result] = radius

print(diff_dict[max(diff_dict.keys())] * max(diff_dict.keys()))