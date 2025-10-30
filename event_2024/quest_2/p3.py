def get_word_lit_pos(wrd, pos):
    ret_pos = set()
    for action in ['up', 'down', 'right', 'left']:
        curr_row = pos[0]
        curr_col = pos[1]
        tmp_pos = set()
        tmp_pos.add(pos)
        for lit in wrd:
            if action == 'up':
                curr_row -= 1
            elif action == 'down':
                curr_row += 1
            elif action == 'right':
                curr_col += 1
            else:
                curr_col -= 1
            if curr_col == len(grid[0]):
                curr_col = 0
            elif curr_col == -1:
                curr_col = len(grid[0]) - 1
            if (curr_row, curr_col) in grid_dict and lit == grid_dict[(curr_row, curr_col)]:
                tmp_pos.add((curr_row, curr_col))
            else:
                tmp_pos = set()
                break
        ret_pos = {*ret_pos, *tmp_pos}
    return ret_pos


inp = open("../../input.txt").read().split('\n\n')

words = inp[0].split('WORDS:')[1].split(',')

grid = inp[1].splitlines()
grid_dict = {}

row_ind = 0
for row in grid:
    col_ind = 0
    for val in row:
        grid_dict[(row_ind, col_ind)] = val
        col_ind += 1
    row_ind += 1

res_pos = set()
for w in words:
    for p, v in grid_dict.items():
        if w[0] == v:
            res_pos = {*res_pos, *get_word_lit_pos(w[1:], p)}

print(len(res_pos))
