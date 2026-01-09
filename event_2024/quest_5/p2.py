from collections import deque, defaultdict

inp = open("../../input.txt").read().splitlines()
curr_rows = []
for i in inp:
    curr_rows.append(list(map(int,i.split(' '))))
curr_clapping_index = 0
curr_cols = list(map(list, zip(*curr_rows)))
curr_col_queues = []
for c in curr_cols:
    curr_col_queues.append(deque(c))

count_dict = defaultdict(int)
rnd = 1

list_len = len(curr_col_queues)
while True:
    clapping_cnt = curr_col_queues[curr_clapping_index].popleft()
    curr_clapping_index += 1
    if curr_clapping_index == list_len:
        curr_clapping_index = 0
    curr_pos = (curr_clapping_index, clapping_cnt)
    curr_col_queues[curr_pos[0]].insert(curr_pos[1]-1, curr_pos[1])
    r = ''
    for j in curr_col_queues:
        r += str(j[0])
    count_dict[int(r)] += 1
    if count_dict[int(r)] == 2024:
        print([key for key, val in count_dict.items() if val == 2024][0] * rnd)
        break
    rnd += 1
