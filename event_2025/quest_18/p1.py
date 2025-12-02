
inp = open("../../input.txt").read().split('\n\n')

energy_dict = {}
incoming_energy = 0
for i in inp:
    sub_lines = i.split('\n')
    plant_num = int(sub_lines[0].split('Plant ')[1].split(' with')[0])
    thickness = int(sub_lines[0].split('thickness ')[1].split(':')[0])
    incoming_energy = 0
    for s in sub_lines[1:]:
        if 'free' in s:
            incoming_energy += thickness
            break
        to_plant = int(s.split('to Plant ')[1].split(' with')[0])
        to_thickness = int(s.split('thickness ')[1])
        incoming_energy += energy_dict[to_plant] * to_thickness
        if incoming_energy < thickness:
            incoming_energy = 0
        energy_dict[plant_num] = incoming_energy

print(incoming_energy)



