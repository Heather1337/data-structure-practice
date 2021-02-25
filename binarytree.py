# Implement a Binary Tree data structure

class Binary_Node():

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Binary_Tree():

    def __init__(self, root=None):
        self.root = root

    def add_node(self, node):
        # first check to see if the root of our tree is empty
        if self.root == None:
            self.root = node
            return
        else:
            def check_children(parent=self.root):
                if not parent.left:
                    parent.left = node
                    return
                if not parent.right:
                    parent.right = node
                    return
                check_children(parent.left)
            check_children()

    def print_children(self, current=None):
        if not current:
            current = self.root
        if current:
            print(current.data)
            if current.left:
                self.print_children(current.left)
            if current.right:
                self.print_children(current.right)

    # Replace a node
    def replace_node(self, node_to_replace, new_node):

        nodes_to_visit = [self.root]
        # current = self.root
        # [9]
        while nodes_to_visit:
            current = nodes_to_visit.pop(0)  # 9
            if current.data == node_to_replace.data:  # 9 == 8
                node_to_replace.data = new_node.data
                return
            else:
                nodes_to_visit.extend([current.left, current.right])
                print(nodes_to_visit)

        # Does node exist in tree

        # Remove node from the tree


node15 = Binary_Node(15)
node9 = Binary_Node(9)
node30 = Binary_Node(30)
node8 = Binary_Node(8)
node5 = Binary_Node(5)

btree = Binary_Tree()
btree.add_node(node9)
btree.add_node(node15)
btree.add_node(node30)
btree.add_node(node8)
# print(btree.root.left.left.data)
# btree.print_children()
btree.replace_node(node15, node5)
btree.print_children()
