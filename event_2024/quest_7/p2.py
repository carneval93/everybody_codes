from collections import deque
inp = open("../../input.txt").read().splitlines()

#track = '+===++-=+=-S'
track = '-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--' + '-=++==-' \
        + '--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-'[::-1] + '-=+=+=-S'

players_result = []
for player in inp:
    name = player.split(':')[0]
    segments = deque(player.split(':')[1].split(','))
    essence_list = []
    curr_essence = 10
    for i in 10*track:
        if i == '+':
            curr_essence += 1
        elif i == '-' and curr_essence > 0:
            curr_essence -= 1
        else:
            curr_segment = segments[0]
            if curr_segment == '+':
                curr_essence += 1
            elif curr_segment == '-' and curr_essence > 0:
                curr_essence -= 1
        segments.rotate(-1)
        essence_list.append(curr_essence)
    essence_sum = sum(essence_list)
    players_result.append((name, essence_sum))

players_result.sort(key=lambda tup: tup[1], reverse=True)
result = ''
for n, s in players_result:
    result += n
print(result)
