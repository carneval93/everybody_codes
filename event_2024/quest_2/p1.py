inp = open("../../input.txt").read().split('\n\n')

words = inp[0].split('WORDS:')[1].split(',')

str_to_observe = inp[1].splitlines()

cnt = 0
for s in str_to_observe:
    for w in words:
        cnt += s.count(w)
print(cnt)