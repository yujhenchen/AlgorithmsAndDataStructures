# add root in the queue
# if there's anything in the queue, add into visited queue
# if the first node in the queue has left, move left into queue
# if the first node in the queue has right, move right into queue
# everytime set current root to the first node in the queue
# return visited queue when current root is None
def bfs(root):
    visited = []

    if root is None:
        return visited

    visited.append(root)
    
    if root.left is not None:
        visited.append(root.left)
    if root.right is not None:
        visited.append(root.right)

    return visited + bfs(root.left) + bfs(root.right)

    # Remove not need part
    # if root.left is None and root.right is None:
    #     return visited
    # else:
    #     if root.left is not None:
    #         visited.append(root.left)
    #     if root.right is not None:
    #         visited.append(root.right)

    #     return visited + bfs(root.left) + bfs(root.right)
        # Below is the first attempt that I didn't figure how to include the right part of the tree
        # if root.left is not None:
        #     return visited + bfs(root.left)
        # if root.right is not None:
        #     return visited + bfs(root.right)
