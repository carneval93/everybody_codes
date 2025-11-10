name_list = open("../../input.txt").read().splitlines()[0].split(',')
instr_list = open("../../input.txt").read().splitlines()[2].split(',')


for instr in instr_list:
    index = 0
    name_one = name_list[0]

    if instr[0] == 'L':
        steps = int(instr.split('L')[1])
        index = -1 * steps % len(name_list)
    else:
        steps = int(instr.split('R')[1])
        index = steps % len(name_list)

    name_two = name_list[index]
    name_two_index = index

    name_list[0] = name_two
    name_list[name_two_index] = name_one


print(name_list[0])
