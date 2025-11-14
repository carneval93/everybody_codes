def check(word):
    found = True
    last_letter = word[0]
    for letter in word[1:]:
        if last_letter not in instr_dict:
            found = False
            break
        if letter not in instr_dict[last_letter]:
            found = False
            break
        last_letter = letter
    return found


name_list = open("../../input.txt").read().splitlines()[0].split(',')
instr_list = open("../../input.txt").read().splitlines()[2:]

instr_dict = {}
for i in instr_list:
    from_letter = i.split(' > ')[0]
    to_letters = i.split(' > ')[1].split(',')
    instr_dict[from_letter] = to_letters

for name in name_list:
    if check(name):
        print(name)
        break

