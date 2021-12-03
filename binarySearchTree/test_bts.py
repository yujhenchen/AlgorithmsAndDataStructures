import pytest
from bst import BST


@pytest.mark.skip(reason="wait for finishing")
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

def print_find(found, value):
    if found is not None:
        print("found node: " + str(found.value))
    else:
        print("cannot find " + str(value))

#@pytest.mark.skip(reason="wait for finishing")
def test_search():
    bst = test_insert()
    print_find(bst.find(1), 1)
    print_find(bst.find(2), 2)
    print_find(bst.find(3), 3)
    print_find(bst.find(21), 21)
    print_find(bst.find(8), 8)
    print_find(bst.find(9), 9)
    print_find(bst.find(14), 14)
