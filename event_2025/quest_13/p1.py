import collections

inp = list(map(int, open("../../input.txt").read().splitlines()))

q = collections.deque([1])
direction = 'right'
left_from_me = 0
for i in inp:
    if direction == 'right':
        direction = 'left'
        q.append(i)
    else:
        direction = 'right'
        left_from_me += 1
        q.insert(0, i)
q.rotate(-1 * left_from_me)
q.rotate(-2025)
print(q[0])