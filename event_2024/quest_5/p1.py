from collections import deque

inp = open("../../input.txt").read().splitlines()
curr_rows = []
for i in inp:
    curr_rows.append(list(map(int,i.split(' '))))
curr_clapping_index = 0
curr_cols = list(map(list, zip(*curr_rows)))
curr_col_queues = []
for c in curr_cols:
    curr_col_queues.append(deque(c))


for rnd in range(10):
    clapping_cnt = curr_col_queues[curr_clapping_index].popleft()
    curr_clapping_index += 1
    if curr_clapping_index == len(curr_col_queues):
        curr_clapping_index = 0
    curr_pos = (curr_clapping_index, -1)
    curr_side = 'left'
    move_cnt = 0
    while move_cnt != clapping_cnt:
        if curr_side == 'left':
            if curr_pos[1] == len(curr_col_queues[curr_pos[0]]) - 1:
                curr_side = 'right'
            else:
                curr_pos = (curr_pos[0], curr_pos[1] + 1)
        else:
            if curr_pos[1] == 0:
                curr_side = 'left'
            else:
                curr_pos = (curr_pos[0], curr_pos[1] - 1)
        move_cnt += 1
    if curr_side == 'left':
        curr_col_queues[curr_pos[0]].insert(curr_pos[1], clapping_cnt)
    else:
        curr_col_queues[curr_pos[0]].insert(curr_pos[1] + 1, clapping_cnt)
    r = ''
    for j in curr_col_queues:
        r += str(j[0])
    print(int(r))

result = ''
for j in curr_col_queues:
    result += str(j[0])
print(int(result))
