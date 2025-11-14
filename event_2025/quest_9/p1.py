import math
inp = open("../../input.txt").read().splitlines()

for child in inp:
    child_dna_list = child.split(':')[1]
    similarities = set()
    similarities_count = []
    for next_parent in inp:
        parent_similarity_count = 0
        next_parent_dna_list = next_parent.split(':')[1]
        if child_dna_list == next_parent_dna_list:
            continue
        for j in range(len(child_dna_list)):
            if child_dna_list[j] == next_parent_dna_list[j]:
                similarities.add(j)
                parent_similarity_count += 1
        similarities_count.append(parent_similarity_count)
    if similarities == set(range(len(child_dna_list))):
        print(math.prod(similarities_count))
        break