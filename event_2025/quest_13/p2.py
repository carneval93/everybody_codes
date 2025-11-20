import collections

inp = open("../../input.txt").read().splitlines()

q = collections.deque([1])
direction = 'right'
left_from_me = 0
for i in inp:
    range_list = range(int(i.split('-')[0]), int(i.split('-')[1])+1)
    if direction == 'right':
        direction = 'left'
        q.extend(list(range_list))
    else:
        direction = 'right'
        left_from_me += len(list(range_list))
        q.extendleft(list(range_list))
q.rotate(-1 * left_from_me)
q.rotate(-20252025)
print(q[0])