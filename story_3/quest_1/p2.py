def get_binary(word):
    bin_word = word.replace('g', '0').replace('G', '1').replace('r', '0').replace('R', '1').replace('b', '0').replace('B', '1').replace('s', '0').replace('S', '1')
    return int(bin_word, 2)


inp = open("../../input.txt").read().splitlines()

shine_pairs = []
for i in inp:
    num = int(i.split(':')[0])
    red = i.split(':')[1].split(' ')[0]
    green = i.split(':')[1].split(' ')[1]
    blue = i.split(':')[1].split(' ')[2]
    shine = i.split(':')[1].split(' ')[3]
    shine_pairs.append((shine, sum([get_binary(red), get_binary(green), get_binary(blue)]), num))

sorted_shine_pairs = sorted(shine_pairs, key=lambda tup: (tup[0], tup[1]))
print(sorted_shine_pairs[0][2])