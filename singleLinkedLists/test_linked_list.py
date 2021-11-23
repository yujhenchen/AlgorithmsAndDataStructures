from linked_list_class import Node
from linked_list_class import SingleLinkedList


def print_nodes(node):
    while node is not None:
        print(node.value)
        node = node.next


def test_push():
    linked_list = SingleLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    print_nodes(linked_list.head)
    return linked_list


def test_pop():
    linked_list = test_push()
    node = linked_list.pop()
    print("node that pop out: " + str(node.value))
    node = linked_list.pop()
    print("node that pop out: " + str(node.value))
    print_nodes(linked_list.head)


def test_shift():
    linked_list = test_push()
    node = linked_list.shift()
    print("node that shift out: " + str(node.value))
    print_nodes(linked_list.head)


def test_unshift():
    linked_list = test_push()
    linked_list.unshift(4)
    print_nodes(linked_list.head)


def test_get():
    linked_list = test_push()
    node = linked_list.get(0)
    if node is not None:
        print("test_get: " + str(node.value))
    node = linked_list.get(1)
    print("test_get: " + str(node.value))
    node = linked_list.get(2)
    print("test_get: " + str(node.value))
    node = linked_list.get(3)
    print("test_get: " + str(node.value))
    node = linked_list.get(4)
    if node is not None:
        print("test_get: " + str(node.value))