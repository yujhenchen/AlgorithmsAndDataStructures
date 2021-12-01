# tree is not linear
# tree basic: root, parents, siblings, childrens, leaves
# every parent node has at most 2 children nodes
# every node to the left of parent node is always less than the parent
# every node to the right of parent node is always greater than the parent
# binary search tree is a type of binary tree, it sorted in order (BST)


class Node(object):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        super().__init__()
        self.root = None

    def insert(self, value):
        return

    def find(self, value):
        return
