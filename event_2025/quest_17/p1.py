def get_pythagoras_result(Xv, Yv, Xc, Yc):
    return (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc)


inp = open("../../input.txt").read().splitlines()

max_radius = 10
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

result = 0
for pos, value in grid_dict.items():
    if get_pythagoras_result(start[0], start[1], pos[0], pos[1]) <= max_radius * max_radius:
        result += value

print(result)