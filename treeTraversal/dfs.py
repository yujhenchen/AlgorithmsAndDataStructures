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
