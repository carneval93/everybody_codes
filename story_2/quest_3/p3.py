import json


def get_neighbours(node):
    neighbours = [(node[0], node[1]), (node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])]
    return neighbours


def breadth_search(die, field_nums, start_node):
    breadth_nodes = list()
    breadth_nodes.append(start_node)
    field_nums_index = 0
    die.add_visited_numbers((start_node, field_nums_index))
    while breadth_nodes:
        new_breath_nodes = list()
        for b_node in breadth_nodes:
            for adjacent in get_neighbours(b_node):
                if (adjacent, field_nums_index) in die.get_visited_numbers():
                    continue
                if adjacent not in grid_dict or int(grid_dict[adjacent]) != field_nums[field_nums_index]:
                    continue
                die.add_visited_numbers((adjacent, field_nums_index))
                new_breath_nodes.append(adjacent)
        breadth_nodes = new_breath_nodes
        field_nums_index += 1


class Die:
    id = 0
    faces = []
    seed = 0
    pulse = 0
    face_ind = 0
    field_numbers = []
    visited_numbers = set()

    def __init__(self, id, faces, seed, face_ind):
        self.id = id
        self.faces = faces
        self.seed = seed
        self.face_ind = face_ind
        self.pulse = seed
        self.field_numbers = []
        self.visited_numbers = set()

    def set_face_index(self, face_ind):
        self.face_ind = face_ind

    def set_pulse(self, pulse):
        self.pulse = pulse

    def append_field_number(self, num):
        self.field_numbers.append(num)

    def add_visited_numbers(self, v_number):
        self.visited_numbers.add(v_number)

    def get_visited_numbers(self):
        return self.visited_numbers

    def get_field_numbers(self):
        return self.field_numbers

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
inp_grid = inp[1].splitlines()
dies = []
len_fields = len(inp_grid) * len(inp_grid[0])

for i in inp_dies:
    id = int(i.split(':')[0])
    faces = json.loads(i.split('faces=')[1].split(' seed')[0])
    seed = int(i.split('seed=')[1])
    dies.append(Die(id, faces, seed, 0))

roll_number = 1
while roll_number < len_fields:
    for d in dies:
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
        d.append_field_number(new_face)

    roll_number += 1

grid_dict = {}
row_num = 0
for row in inp_grid:
    col_num = 0
    for col in row:
        grid_dict[(row_num, col_num)] = col
        col_num += 1
    row_num += 1

for pos, val in grid_dict.items():
    for d in dies:
        field_numbers = d.get_field_numbers()
        if field_numbers[0] == int(val):
            breadth_search(d, field_numbers[1:], pos)

visited_grid = set()
for d in dies:
    for elem in d.get_visited_numbers():
        visited_grid.add(elem[0])

print(len(visited_grid))
