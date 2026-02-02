from collections import deque
from itertools import permutations, starmap


def execute_race(comb, oppo_result=0):
    better_ret = 0
    cnt = 0
    players_result_ret = []
    for player in comb:
        name = player.split(':')[0]
        segments = deque(player.split(':')[1].split(','))
        cnt += 1
        essence_list = []
        curr_essence = 10
        # Shortcut: only consider first 11 laps
        for i in len(segments) * track:
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
        if essence_sum > oppo_result:
            better_ret += 1
        players_result_ret.append((name, essence_sum))
    return players_result_ret, better_ret


def get_neighbours(node):
    neighbours = [(node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])]
    return neighbours


def depth_search(start_node, v_nodes):
    if path_dict[start_node] == 'S':
        return v_nodes
    for adjacent in get_neighbours(start_node):
        if adjacent in v_nodes or adjacent not in path_dict or path_dict[adjacent] == ' ':
            continue
        v_nodes.append(adjacent)
        ret = depth_search(adjacent, v_nodes)
        if ret:
            race_track_pos.append(ret.copy())
        v_nodes.pop()
    return []


path = open("racetrack.txt").read().splitlines()
path_dict = {}
row_ind = 0
for row in path:
    col_ind = 0
    for val in row:
        path_dict[(row_ind, col_ind)] = val
        col_ind += 1
    row_ind += 1

inp = open("../../input.txt").read().splitlines()
race_track_pos = []

depth_search((0, 1), [(0, 1)])

track = ''
for t_pos in race_track_pos[1]:
    track += path_dict[t_pos]

players_result, _ = execute_race(inp)

opponents_result = players_result[0][1]

symbols = ['+'] * 5 + ['-'] * 3 + ['='] * 3

combinations = list(permutations(symbols, 11))
combinations_full = set(['A:' + ','.join(x) for x in combinations])

_, better = execute_race(combinations_full, opponents_result)

print(better)
