name_list = open("../../input.txt").read().splitlines()[0].split(',')
instr_list = open("../../input.txt").read().splitlines()[2].split(',')

index = 0
for instr in instr_list:

    if instr[0] == 'L':
        steps = int(instr.split('L')[1])
        index = (index - steps) % len(name_list)
    else:
        steps = int(instr.split('R')[1])
        index = (index + steps) % len(name_list)

print(name_list[index])
