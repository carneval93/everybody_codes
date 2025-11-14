cat_list = list(open("../../input.txt").read())
a_mentors = 0
b_mentors = 0
c_mentors = 0
pairs = 0
for cat in cat_list:
    if cat == 'A':
        a_mentors += 1
    elif cat == 'B':
        b_mentors += 1
    elif cat == 'C':
        c_mentors += 1
    elif cat == 'a':
        pairs += a_mentors
    elif cat == 'b':
        pairs += b_mentors
    elif cat == 'c':
        pairs += c_mentors

print(pairs)