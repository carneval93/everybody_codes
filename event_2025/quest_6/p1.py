cat_list = list(open("../../input.txt").read())
mentors = 0
pairs = 0
for cat in cat_list:
    if cat == 'A':
        mentors += 1
    elif cat == 'a':
        pairs += mentors

print(pairs)