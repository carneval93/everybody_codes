def get_binary(word):
    bin_word = word.replace('g', '0').replace('G', '1').replace('r', '0').replace('R', '1').replace('b', '0').replace('B', '1')
    return int(bin_word, 2)


inp = open("../../input.txt").read().splitlines()

res = 0
for i in inp:
    num = int(i.split(':')[0])
    red = i.split(':')[1].split(' ')[0]
    green = i.split(':')[1].split(' ')[1]
    blue = i.split(':')[1].split(' ')[2]
    if get_binary(green) > get_binary(red) and get_binary(green) > get_binary(blue):
        res += num

print(res)