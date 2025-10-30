inp = open("../../input.txt").read().split('\n\n')

words = inp[0].split('WORDS:')[1].split(',')

str_to_observe = inp[1].splitlines()

cnt = 0
for s in str_to_observe:
    symbols_in_line = set()
    for w in words:
        for i in range(len(s)):
            if s.startswith(w, i):
                for c in range(len(w)):
                    symbols_in_line.add(i + c)
            if s.startswith(w[::-1], i):
                for c in range(len(w)):
                    symbols_in_line.add(i + c)
    cnt += len(symbols_in_line)

print(cnt)
