class Node:
    id = 0
    plug = ''
    leftSocket = ''
    rightSocket = ''
    data = ''
    left_node = None
    right_node = None
    left_bound = ''
    right_bound = ''
    plug_node = None
    traveled_left = False
    traveled_right = False

    def __init__(self, id, plug, leftSocket, rightSocket):
        self.id = id
        self.plug = plug
        self.leftSocket = leftSocket
        self.rightSocket = rightSocket
        self.left_node = None
        self.right_node = None
        self.left_bound = ''
        self.right_bound = ''
        self.plug_node = None
        self.visited_left = False
        self.visited_right = False

    def get_id(self):
        return self.id

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

    def get_plug_node(self):
        return self.plug_node

    def set_left_node(self, new_left_node):
        self.left_node = new_left_node

    def set_right_node(self, new_right_node):
        self.right_node = new_right_node

    def set_plug_node(self, new_plug_node):
        self.plug_node = new_plug_node

    def get_plug_color(self):
        return self.plug.split(' ')[0]

    def get_leftSocket_color(self):
        return self.leftSocket.split(' ')[0]

    def get_rightSocket_color(self):
        return self.rightSocket.split(' ')[0]

    def get_plug_shape(self):
        return self.plug.split(' ')[1]

    def get_leftSocket_shape(self):
        return self.leftSocket.split(' ')[1]

    def get_rightSocket_shape(self):
        return self.rightSocket.split(' ')[1]

    def set_left_bound(self, which_bound):
        self.left_bound = which_bound

    def set_right_bound(self, which_bound):
        self.right_bound = which_bound

    def get_left_bound(self):
        return self.left_bound

    def get_right_bound(self):
        return self.right_bound

    def attach_new_node(self, new_node):
        if self.visited_left and self.visited_right and self.get_id() != 1:
            if self.get_plug_node():
                self.get_plug_node().attach_new_node(new_node)
        elif self.visited_left and self.visited_right and self.get_id() == 1:
            reset_visited()
            self.attach_new_node(new_node)
        elif not self.visited_left and not self.visited_right:
            self.visited_left = True
            next_left = self.get_left_node()
            if not next_left and self.get_leftSocket_color() == new_node.get_plug_color() and self.get_leftSocket_shape() == new_node.get_plug_shape():
                self.set_left_node(new_node)
                new_node.set_plug_node(self)
                self.set_left_bound('STRONG')
            elif not next_left and (self.get_leftSocket_color() == new_node.get_plug_color() or self.get_leftSocket_shape() == new_node.get_plug_shape()):
                self.set_left_node(new_node)
                new_node.set_plug_node(self)
                self.set_left_bound('WEAK')
            elif not next_left:
                self.attach_new_node(new_node)
            else:
                next_left.attach_new_node(new_node)
        elif self.visited_left and not self.visited_right:
            next_right = self.get_right_node()
            self.visited_right = True
            if not next_right and self.get_rightSocket_color() == new_node.get_plug_color() and self.get_rightSocket_shape() == new_node.get_plug_shape():
                self.set_right_node(new_node)
                new_node.set_plug_node(self)
                self.set_right_bound('STRONG')
            elif not next_right and (self.get_rightSocket_color() == new_node.get_plug_color() or self.get_rightSocket_shape() == new_node.get_plug_shape()):
                self.set_right_node(new_node)
                new_node.set_plug_node(self)
                self.set_right_bound('WEAK')
            elif not next_right:
                self.attach_new_node(new_node)
            else:
                next_right.attach_new_node(new_node)

    def do_travel(self):
        if self.visited_left and self.visited_right:
            if self.get_plug_node():
                self.get_plug_node().do_travel()
        elif not self.visited_left and not self.visited_right:
            self.visited_left = True
            next_left = self.get_left_node()
            if next_left:
                next_left.do_travel()
            else:
                result.append(self.get_id())
                self.do_travel()
        else:
            self.visited_right = True
            if self.get_id() not in result:
                result.append(self.get_id())
            next_right = self.get_right_node()
            if next_right:
                next_right.do_travel()
            else:
                self.do_travel()


def reset_visited():
    for n in node_list:
        if n:
            n.visited_right = False
            n.visited_left = False


inp = open("../../input.txt").read().splitlines()
start_node = None
result = []
node_list = []

for i in inp:
    split_line = i.split(', ')
    node_id = 0
    node_plug = ''
    node_leftSocket = ''
    node_rightSocket = ''
    for attribute in split_line:
        if 'id' in attribute:
            node_id = int(attribute.split('=')[1])
        elif 'plug' in attribute:
            node_plug = attribute.split('=')[1]
        elif 'leftSocket' in attribute:
            node_leftSocket = attribute.split('=')[1]
        elif 'rightSocket' in attribute:
            node_rightSocket = attribute.split('=')[1]

    new_node = Node(node_id, node_plug, node_leftSocket, node_rightSocket)
    if not start_node:
        start_node = new_node
        node_list.append(start_node)
        continue
    node_list.append(new_node)
    start_node.attach_new_node(new_node)
    reset_visited()


start_node.do_travel()
final_result = 0
for i in range(len(result)):
    final_result += (i + 1) * result[i]
print(final_result)