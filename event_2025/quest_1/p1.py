name_list = open("../../input.txt").read().splitlines()[0].split(',')
instr_list = open("../../input.txt").read().splitlines()[2].split(',')

index = 0
for instr in instr_list:
    steps = int(instr[1])
    if instr[0] == 'L':
        index -= steps
    else:
        index += steps
    if index < 0:
        index = 0
    elif index >= len(name_list):
        index = len(name_list) - 1

print(name_list[index])
