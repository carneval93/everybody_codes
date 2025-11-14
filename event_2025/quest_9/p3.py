import itertools


def breadth_search(start_nodes, v_nodes):
    breadth_nodes = start_nodes
    while breadth_nodes:
        new_breath_nodes = list()
        for b_node in breadth_nodes:
            if b_node not in parents_dict:
                continue
            for adjacent in parents_dict[b_node]:
                if adjacent in v_nodes:
                    continue
                v_nodes.append(adjacent)
                new_breath_nodes.append(adjacent)
        breadth_nodes = new_breath_nodes
    return set(map(int, v_nodes))


inp = open("../../input.txt").read().splitlines()

parents_dict = {}
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
        first_parent_id = possible_parent_pair[0].split(':')[0]
        second_parent_id = possible_parent_pair[1].split(':')[0]
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
            if first_parent_id not in parents_dict:
                parents_dict[first_parent_id] = {child_id}
            else:
                parents_dict[first_parent_id].add(child_id)

            if child_id not in parents_dict:
                parents_dict[child_id] = {first_parent_id, second_parent_id}
            else:
                parents_dict[child_id].add(first_parent_id)
                parents_dict[child_id].add(second_parent_id)

            if second_parent_id not in parents_dict:
                parents_dict[second_parent_id] = {child_id}
            else:
                parents_dict[second_parent_id].add(child_id)
            break


groups = []
for k, v in parents_dict.items():
    groups.append(breadth_search([k], [k]))

print(sum(max(groups, key=len)))