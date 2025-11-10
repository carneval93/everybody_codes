set_list = list(map(int,open("../../input.txt").read().split(',')))
set_list_set_first_20 = list(set(sorted(set_list)))[:20]
print(sum(set_list_set_first_20))