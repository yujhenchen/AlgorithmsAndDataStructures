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

    def insert_helper(self, cur_root, node):
        if node.value >= cur_root.value:
            if cur_root.right is None:
                cur_root.right = node
            else:
                self.insert_helper(cur_root.right, node)
        else:
            if cur_root.left is None:
                cur_root.left = node
            else:
                self.insert_helper(cur_root.left, node)

    def insert(self, value):
        # create a node
        # if root is None, root = node

        # else
        # cur_root = root
        # loop
        # if node >= cur_root,
        # if cur_root has no right, cur_root.right = node, break
        # else cur_root = cur_root.right

        # if node < cur_root, if cur_root has no left cur_root.lef = node, break
        # else cur_root = cur_root.left
        node = Node(value)
        if self.root == None:
            self.root = node
        else:
            cur_root = self.root
            self.insert_helper(cur_root, node)
        return

    def find(self, value):
        # loop, stop at cur_root == None
        # if value == cur_root, found, break
        # if value > cur_root, cur_root = right
        # if value < cur_root, cur_root = left
        found_node = None
        cur_root = self.root

        return found_node
