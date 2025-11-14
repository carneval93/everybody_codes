def find_words(start_node, depth, v_nodes):
    if len(v_nodes) == depth:
        found_words_set.add(str(v_nodes))
    else:
        if start_node in instr_dict:
            for adjacent in instr_dict[start_node]:
                v_nodes.append(adjacent)
                find_words(adjacent, depth, v_nodes)
                v_nodes.pop()


def check(word):
    found = True
    last_letter = word[0]
    for letter in word[1:]:
        if last_letter not in instr_dict:
            found = False
            break
        if letter not in instr_dict[last_letter]:
            found = False
            break
        last_letter = letter
    return found


name_list = open("../../input.txt").read().splitlines()[0].split(',')
instr_list = open("../../input.txt").read().splitlines()[2:]

instr_dict = {}
for i in instr_list:
    from_letter = i.split(' > ')[0]
    to_letters = i.split(' > ')[1].split(',')
    instr_dict[from_letter] = to_letters

found_words_set = set()
for name in name_list:
    if not check(name):
        continue
    for d in range(7,12):
        find_words(name[-1], d, list(name))

print(len(found_words_set))