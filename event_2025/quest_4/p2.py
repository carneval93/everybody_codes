gear_list = list(map(int, open("../../input.txt").read().splitlines()))

gear_factor = 1

last_gear_teeth = gear_list[0]
for gear in gear_list[1:]:
    gear_factor *= last_gear_teeth / gear
    last_gear_teeth = gear

print(int(10000000000000/gear_factor+1))
