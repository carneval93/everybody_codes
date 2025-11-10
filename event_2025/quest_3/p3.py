from collections import Counter
set_list = list(map(int,open("../../input.txt").read().split(',')))
print(max(Counter(set_list).values()))