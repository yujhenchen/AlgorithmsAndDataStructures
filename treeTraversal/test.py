import pytest
from bst import BST
from bfs import bfs
from dfs import pre_order_dfs
from dfs import post_order_dfs


def get_bst():
    bst = BST()
    bst.insert(8)
    bst.insert(6)
    bst.insert(9)
    bst.insert(4)
    bst.insert(3)
    bst.insert(12)
    bst.insert(7)
    return bst


def print_nodes(results):
    for node in results:
        print(node.value)

@pytest.mark.skip(reason="wait for finishing")
def test_bfs():
    bst = get_bst()

    print(bst.root.value)
    results = bfs(bst.root)
    print_nodes(results)

@pytest.mark.skip(reason="wait for finishing")
def test_pre_order_dfs():
    bst = get_bst()
    results = pre_order_dfs(bst.root)
    print_nodes(results)


def test_post_order_dfs():
    bst = get_bst()
    results = post_order_dfs(bst.root)
    print_nodes(results)