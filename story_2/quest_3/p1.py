import json


class Die:
    id = 0
    faces = []
    seed = 0
    pulse = 0
    face_ind = 0

    def __init__(self, id, faces, seed, face_ind):
        self.id = id
        self.faces = faces
        self.seed = seed
        self.face_ind = face_ind
        self.pulse = seed

    def set_face_index(self, face_ind):
        self.face_ind = face_ind

    def set_pulse(self, pulse):
        self.pulse = pulse

    def get_faces(self):
        return self.faces

    def get_seed(self):
        return self.seed

    def get_pulse(self):
        return self.pulse


inp = open("../../input.txt").read().splitlines()
dies = []

for i in inp:
    id = int(i.split(':')[0])
    faces = json.loads(i.split('faces=')[1].split(' seed')[0])
    seed = int(i.split('seed=')[1])
    dies.append(Die(id, faces, seed, 0))

roll_number = 1
result = 0
while result < 10000:
    inter_result = 0
    for d in dies:
        faces = d.get_faces()
        seed = d.get_seed()
        pulse = d.get_pulse()
        spin = roll_number * pulse

        spin_tmp = spin + d.face_ind
        new_face = faces[spin_tmp % len(faces)]
        inter_result += new_face
        d.set_face_index(spin_tmp % len(faces))

        pulse = pulse + spin
        pulse = pulse % seed
        pulse = pulse + 1 + roll_number + seed
        d.set_pulse(pulse)
    result += inter_result
    roll_number += 1
print(roll_number - 1)
