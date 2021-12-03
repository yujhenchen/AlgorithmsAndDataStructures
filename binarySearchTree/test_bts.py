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


#@pytest.mark.skip(reason="wait for finishing")
def test_search():
    bst = test_insert()
    found_9 = bst.find(9)
    if found_9 is not None:
        print(found_9.value)
    else:
        print("cannot find 9")

    found_13 = bst.find(13)
    if found_13 is not None:
        print(found_13.value)
    else:
        print("cannot find 13")
