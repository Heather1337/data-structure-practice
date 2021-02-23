# Implement a Tree data structure class

class Node():
    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []

    # def __repr__(self):
        # implement a repr method for testing

    # Add child
    def add_child(self, node):
        self.children.append(node)

    # print children
    def print_children(self):
        for child in self.children:
            print(f'Child of {self.data}: ', child.data)

    def print_descendants(self):
        # create list for nodes to check instantiate it with current nodes children
        nodes_to_check = self.children.copy()
        # while nodes are in list
        while nodes_to_check:  # [] == false
            # pop off front of list to print value
            curr = nodes_to_check.pop(0)
            # print value
            print('Child of Parent 1', curr.data)
            # check if node has any children
            if curr.children:  # [] == false
                # add children to front of nodes to check list
                for child in curr.children:
                    # insert each child at front of list
                    nodes_to_check.insert(0, child)

    def is_child(self, data):
        nodes_to_check = self.children.copy()

        while nodes_to_check:
            curr = nodes_to_check.pop()
            if curr.data == data:
                print('True')
                return
            else:
                if curr.children:
                    for child in curr.children:
                        nodes_to_check.append(child)
        print('False')


node1 = Node(1)
node9 = Node(9)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node1.add_child(node9)
node1.add_child(node2)
node2.add_child(node4)
node4.add_child(node6)
node4.add_child(node5)
node6.add_child(node7)
node3.add_child(node8)
node1.add_child(node3)


node1.print_descendants()
node3.is_child(10)  # True
