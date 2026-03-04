
inp = int(open("../../input.txt").read())

thickness = 1
priest_acolytes = 1111
blocks_available = 20240000 - 1
width = 1
while blocks_available > 0:
    thickness = (inp * thickness) % priest_acolytes
    width += 2
    blocks_available -= width * thickness

print(abs(blocks_available) * width)
