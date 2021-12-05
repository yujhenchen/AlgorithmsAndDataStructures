# depth first pre-order
# visit left side of the tree till the end
# after done the left side, go to the right side
def pre_order_dfs(root):
    visited = []

    if root == None:
        return visited

    visited.append(root)

    if root.left is not None:
        visited += pre_order_dfs(root.left)
    if root.right is not None:
        visited += pre_order_dfs(root.right)
    return visited


# visit node from left side all the way till the end
# start to add left node at the end, and add the right node at the end
# from end to the top, left first to the right
def post_order_dfs(root):
    # visit all the way from left and right till the end
    visited = []

    if root is None:
        return visited

    post_order_dfs(root.left), post_order_dfs(root.right)

    if root.left is not None:
        print("root.left.value: " + str(root.left.value))
    if root.right is not None:
        print("root.right.value: " + str(root.right.value))

