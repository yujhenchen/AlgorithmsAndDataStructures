from bst import BST
from bfs import bfs

def test_bfs():
    bst = BST()
    bst.insert(8)
    bst.insert(6)
    bst.insert(9)
    bst.insert(4)
    bst.insert(3)
    bst.insert(12)

    print(bst.root.value)
    results = bfs(bst.root)
    for node in results:
        print(node.value)