from collections import deque

inp = open("../../input.txt").read().splitlines()

sequence = deque(['↑', '→', '↓', '←'])

grid = {}
row_ind = 0
start = ()
goal = ()
for row in inp:
    col_ind = 0
    for col in row:
        grid[(row_ind, col_ind)] = col
        if col == '@':
            start = (row_ind,col_ind)
        if col == '#':
            goal = (row_ind,col_ind)
        col_ind += 1
    row_ind +=1

step = 0
curr_pos = start
while curr_pos != goal:
    new_pos = ()
    if sequence[0] == '↑':
        new_pos = (curr_pos[0]-1, curr_pos[1])
    elif sequence[0] == '↓':
        new_pos = (curr_pos[0]+1, curr_pos[1])
    elif sequence[0] == '→':
        new_pos = (curr_pos[0], curr_pos[1]+1)
    elif sequence[0] == '←':
        new_pos = (curr_pos[0], curr_pos[1]-1)
    if grid[new_pos] == '.' or new_pos == goal:
        grid[new_pos] = '@'
        curr_pos = new_pos
        step += 1
    sequence.rotate(-1)

print(step)