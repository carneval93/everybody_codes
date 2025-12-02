
test_cases = open("../../input.txt").read().split('\n\n\n')[1].split('\n')
inp = open("../../input.txt").read().split('\n\n\n')[0].split('\n\n')
result = []

for test_num in range(len(test_cases)):
    test = test_cases[test_num].split(' ')
    energy_dict = {}
    incoming_energy = 0
    for i in inp:
        sub_lines = i.split('\n')
        plant_num = int(sub_lines[0].split('Plant ')[1].split(' with')[0])
        thickness = int(sub_lines[0].split('thickness ')[1].split(':')[0])
        incoming_energy = 0
        for s in sub_lines[1:]:
            if 'free' in s:
                sub_test = int(test.pop(0))
                if sub_test == 1:
                    incoming_energy += thickness
                break
            to_plant = int(s.split('to Plant ')[1].split(' with')[0])
            to_thickness = int(s.split('thickness ')[1])
            incoming_energy += energy_dict[to_plant] * to_thickness
        if incoming_energy < thickness:
            incoming_energy = 0
        energy_dict[plant_num] = incoming_energy
    result.append(incoming_energy)

print(sum(result))
