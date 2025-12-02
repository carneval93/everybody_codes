inp = list(map(int, open("../../input.txt").read().split(',')))
max_len = len(inp) - 1
period_result = []

for period in range(1, max_len):
    new_inp = inp.copy()
    violation = False
    for i in range(period-1, max_len+1, period):
        if inp[i] == 0:
            violation = True
            break
        new_inp[i] -= 1
    if not violation:
        period_result.append(period)
        inp = new_inp.copy()

blocks = 202520252025000

len_to_try = []

for i in range(4,15):
    len_to_try.append(pow(10,i))

result_dict = {}

col_num = 4875 #tried
tmp_blocks = min(len_to_try) + 10

for l in len_to_try:
    col_num = col_num * 10
    tmp_blocks = l + 50
    while tmp_blocks > l:
        col_num -= 1
        tmp_blocks = 0

        for p in period_result:
            tmp_blocks += col_num // p
    result_dict[tmp_blocks] = col_num

l = blocks

col_num = int(col_num * (blocks/max(len_to_try)))
tmp_blocks = l + 50
while tmp_blocks > l:
    col_num -= 1
    tmp_blocks = 0

    for p in period_result:
        tmp_blocks += col_num // p

print(col_num)
