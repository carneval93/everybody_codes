set_list = list(map(int,open("../../input.txt").read().split(',')))
set_list_set_sum = sum(set(sorted(set_list)))
print(set_list_set_sum)