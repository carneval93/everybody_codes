import json


class Die:
    id = 0
    faces = []
    seed = 0
    pulse = 0
    face_ind = 0
    left_steps = []

    def __init__(self, id, faces, seed, face_ind, left_steps):
        self.id = id
        self.faces = faces
        self.seed = seed
        self.face_ind = face_ind
        self.pulse = seed
        self.left_steps = left_steps

    def set_face_index(self, face_ind):
        self.face_ind = face_ind

    def set_pulse(self, pulse):
        self.pulse = pulse

    def set_left_steps(self, left_steps):
        self.left_steps = left_steps

    def get_left_steps(self):
        return self.left_steps

    def get_faces(self):
        return self.faces

    def get_seed(self):
        return self.seed

    def get_pulse(self):
        return self.pulse

    def get_id(self):
        return self.id


inp = open("../../input.txt").read().split('\n\n')
inp_dies = inp[0].split('\n')
inp_order = inp[1]
dies = []

for i in inp_dies:
    id = int(i.split(':')[0])
    faces = json.loads(i.split('faces=')[1].split(' seed')[0])
    seed = int(i.split('seed=')[1])
    dies.append(Die(id, faces, seed, 0, list(map(int, list(inp_order)))))

roll_number = 1
result = []
while len(result) != len(dies):
    for d in dies:
        if len(d.get_left_steps()) == 0:
            continue
        faces = d.get_faces()
        seed = d.get_seed()
        pulse = d.get_pulse()
        spin = roll_number * pulse

        spin_tmp = spin + d.face_ind
        new_face = faces[spin_tmp % len(faces)]
        d.set_face_index(spin_tmp % len(faces))

        pulse = pulse + spin
        pulse = pulse % seed
        pulse = pulse + 1 + roll_number + seed
        d.set_pulse(pulse)

        die_steps = d.get_left_steps()
        if new_face == die_steps[0]:
            if len(die_steps) == 1:
                result.append(d.get_id())
                d.set_left_steps([])
                continue
            d.set_left_steps(die_steps[1:])
    roll_number += 1
print(str(result).replace(' ', '').replace('[', '').replace(']', ''))
