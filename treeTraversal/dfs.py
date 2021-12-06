# depth first pre-order
# visit left side of the tree till the end
# after done the left side, go to the right side
def pre_order_dfs(root):
    visited = []

    if root == None:
        return visited

    visited.append(root)

    visited += pre_order_dfs(root.left) + pre_order_dfs(root.right)

    # this is not needed, because each recursion pass either left or right as root
    # if root.left is not None:
    #     visited += pre_order_dfs(root.left)
    # if root.right is not None:
    #     visited += pre_order_dfs(root.right)
    return visited


# visit node from left side all the way till the end
# start to add left node at the end, and add the right node at the end
# from end to the top, left first to the right
def post_order_dfs(root):
    # visit all the way from left and right till the end
    visited = []

    if root is None:
        return visited

    visited += post_order_dfs(root.left) + post_order_dfs(root.right)
    # this is not needed, because each recursion pass either left or right as root
    # if root.left is not None:
    #     # print("root.left.value: " + str(root.left.value))
    #     visited.append(root.left)
    # if root.right is not None:
    #     # print("root.right.value: " + str(root.right.value))
    #     visited.append(root.right)
    # # debug use
    # # for node in visited:
    # #     print(node.value)

    visited.append(root)
    return visited


# visit node from left side all the way till the end
# add the entire tree from left, root, right
# move backward
def in_order_dfs(root):
    visited = []

    if root is None:
        return visited

    # # debug use
    # for node in visited:
    #     print(node.value)
    # print()

    return visited
