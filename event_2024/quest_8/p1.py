
inp = int(open("../../input.txt").read())

layer = 0
area = 0
while area <= inp:
    layer += 1
    height = layer
    area = height * height

final_width = layer * 2 - 1
print(final_width * (area - inp))
