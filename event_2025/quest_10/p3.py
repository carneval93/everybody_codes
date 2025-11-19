def get_dragon_next_steps(d):
    ret = []
    ret.append((d[0] + 2, d[1] + 1))
    ret.append((d[0] + 2, d[1] - 1))
    ret.append((d[0] - 2, d[1] + 1))
    ret.append((d[0] - 2, d[1] - 1))
    ret.append((d[0] + 1, d[1] + 2))
    ret.append((d[0] + 1, d[1] - 2))
    ret.append((d[0] - 1, d[1] + 2))
    ret.append((d[0] - 1, d[1] - 2))
    return ret


def get_sheep_next_step(curr_s_pos):
    ret = []
    for pos in curr_s_pos:
        ret.append((pos, (pos[0] + 1, pos[1])))
    return ret


def next_turn(curr_turn, curr_dragon_position, curr_sheep_positions):
    key = (curr_turn, curr_dragon_position, tuple(sorted(curr_sheep_positions)))
    result = 0
    if key in visited_setup:
        return visited_setup[key]
    if len(curr_sheep_positions) == 0:
        visited_setup[key] = 1
        return 1
    else:
        if curr_turn == 'sheep':
            skip = 0
            for old_sheep_pos, next_possible_sheep_pos in get_sheep_next_step(curr_sheep_positions):
                next_possible_sheep_pos_set = curr_sheep_positions.copy()
                if next_possible_sheep_pos not in grid:
                    continue
                if next_possible_sheep_pos == curr_dragon_position and grid[next_possible_sheep_pos] != '#':
                    skip += 1
                    continue
                next_possible_sheep_pos_set.remove(old_sheep_pos)
                next_possible_sheep_pos_set.append(next_possible_sheep_pos)
                result += next_turn('dragon', curr_dragon_position, next_possible_sheep_pos_set.copy())
            if skip == len(curr_sheep_positions):
                result += next_turn('dragon', curr_dragon_position, curr_sheep_positions.copy())
        elif curr_turn == 'dragon':
            for next_possible_dragon_pos in get_dragon_next_steps(curr_dragon_position):
                if next_possible_dragon_pos not in grid:
                    continue
                next_sheep_pos = curr_sheep_positions.copy()
                if next_possible_dragon_pos in next_sheep_pos and grid[next_possible_dragon_pos] != '#':
                    next_sheep_pos.remove(next_possible_dragon_pos)
                result += next_turn('sheep', next_possible_dragon_pos, next_sheep_pos.copy())

    visited_setup[key] = result
    return result


inp = open("../../input.txt").read().splitlines()
dragon_position = 0
sheep_positions = []
unique_won = set()
visited_setup = {}
grid = {}
row_ind = 0
for row in inp:
    col_ind = 0
    for col in row:
        grid[(row_ind, col_ind)] = col
        if col == 'D':
            dragon_position = (row_ind,col_ind)
        if col == 'S':
            sheep_positions.append((row_ind,col_ind))
        col_ind += 1
    row_ind +=1

print(next_turn('sheep', dragon_position, sheep_positions))