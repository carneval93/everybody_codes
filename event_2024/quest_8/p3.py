
inp = int(open("../../input.txt").read())

thickness = 1
priest_acolytes = 10
total_blocks = 202400000
blocks_available = total_blocks - 1
width = 1
heights = [1]
while blocks_available > 0:
    thickness = (inp * thickness) % priest_acolytes + priest_acolytes
    width += 2
    blocks_available -= width * thickness
    new_heights = []
    for h in heights:
        new_heights.append(h+thickness)
    new_heights = [thickness] + new_heights
    new_heights.append(thickness)
    heights = new_heights.copy()

leave_empty = 0
for h in heights[1:-1]:
    leave_empty += ((inp * width) * h) % priest_acolytes

print(abs(blocks_available)-leave_empty)
