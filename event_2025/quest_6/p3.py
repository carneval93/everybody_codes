inp = open("../../input.txt").read()
cat_list = list(3 * inp)
a_mentors = set()
b_mentors = set()
c_mentors = set()
i = 0
for cat in cat_list:
    if cat == 'A':
        a_mentors.add(i)
    elif cat == 'B':
        b_mentors.add(i)
    elif cat == 'C':
        c_mentors.add(i)
    i += 1

i = 0
part_pairs = []
for part in range(3):
    pairs = 0
    for cat in inp:
        if cat in ['a', 'b', 'c']:
            start = i - 1000
            end = i + 1000
            if cat == 'a':
                pairs += len(set(range(start, end + 1)).intersection(a_mentors))
            elif cat == 'b':
                pairs += len(set(range(start, end + 1)).intersection(b_mentors))
            elif cat == 'c':
                pairs += len(set(range(start, end + 1)).intersection(c_mentors))
        i += 1
    part_pairs.append(pairs)

print(part_pairs[0] + 998*part_pairs[1] + part_pairs[2])