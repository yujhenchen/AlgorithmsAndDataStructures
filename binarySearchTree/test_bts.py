from bst import BST

def test_insert():
    bst = BST()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(21)
    bst.insert(8)
    bst.insert(9)
    bst.insert(14)
    return bst

def test_search():
    bst = test_insert
    bst.find(9)
    bst.find(19)