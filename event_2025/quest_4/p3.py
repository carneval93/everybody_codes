gear_list = open("../../input.txt").read().splitlines()

gear_factor = 1

last_gear_teeth = int(gear_list[0])
for gear in gear_list[1:-1]:
    first_in_pair = int(gear.split('|')[0])
    second_in_pair = int(gear.split('|')[1])
    gear_factor *= last_gear_teeth / first_in_pair
    last_gear_teeth = second_in_pair
gear_factor *= last_gear_teeth / int(gear_list[-1])
print(int(gear_factor*100))
