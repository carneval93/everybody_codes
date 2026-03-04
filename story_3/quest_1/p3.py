from collections import defaultdict


def get_binary(word):
    bin_word = word.replace('g', '0').replace('G', '1').replace('r', '0').replace('R', '1').replace('b', '0').replace('B', '1').replace('s', '0').replace('S', '1')
    return int(bin_word, 2)


inp = open("../../input.txt").read().splitlines()

shine_list = []
for i in inp:
    num = int(i.split(':')[0])
    red = i.split(':')[1].split(' ')[0]
    green = i.split(':')[1].split(' ')[1]
    blue = i.split(':')[1].split(' ')[2]
    shine = i.split(':')[1].split(' ')[3]
    shine_val = get_binary(shine)
    color_list = [(get_binary(red), 'red'), (get_binary(green), 'green'), (get_binary(blue), 'blue')]
    sorted_color_list = sorted(color_list, key=lambda tup: tup[0], reverse=True)
    if sorted_color_list[0][0] == sorted_color_list[1][0] or shine_val in [31,32]:
        continue
    dominant_color = sorted_color_list[0][1]
    shine_category = 'matte' if shine_val <= 30 else 'shiny'
    shine_list.append((num, dominant_color + '-' + shine_category))

d = defaultdict(int)

for num_val, category in shine_list:
    d[category] += num_val

print(max(d.values()))