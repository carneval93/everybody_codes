import math
import itertools
inp = open("../../input.txt").read().splitlines()

result = 0
for child in inp:
    child_id = child.split(':')[0]
    child_dna_list = child.split(':')[1]
    possible_parents = inp.copy()
    possible_parents.remove(child)
    for possible_parent_pair in list(itertools.combinations(possible_parents, 2)):
        first_parent_dna_list = possible_parent_pair[0].split(':')[1]
        second_parent_dna_list = possible_parent_pair[1].split(':')[1]
        first_parent_similarity_cnt = 0
        second_parent_similarity_cnt = 0
        found = True
        for pair_index in range(len(child_dna_list)):
            if child_dna_list[pair_index] != first_parent_dna_list[pair_index] and child_dna_list[pair_index] != second_parent_dna_list[pair_index]:
                found = False
                break
            if child_dna_list[pair_index] == first_parent_dna_list[pair_index]:
                first_parent_similarity_cnt += 1
            if child_dna_list[pair_index] == second_parent_dna_list[pair_index]:
                second_parent_similarity_cnt += 1
        if found:
            result += first_parent_similarity_cnt * second_parent_similarity_cnt
            break

print(result)