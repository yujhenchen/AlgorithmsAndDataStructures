import pytest
from linked_list import DoublyLinkedList


def print_nodes(node):
    while node is not None:
        if node.prev is not None:
            print("node prev value: " + str(node.prev.value))
        print("node value: " + str(node.value))
        if node.next is not None:
            print("node next value: " + str(node.next.value))
        node = node.next
    print()


@pytest.mark.skip(reason="wait for finishing")
def test_push():
    linked_list = DoublyLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    linked_list.push(5)
    print_nodes(linked_list.head)
    return linked_list


@pytest.mark.skip(reason="wait for finishing")
def test_pop():
    linked_list = test_push()
    node = linked_list.pop()
    print("test_pop: node that pop out: " + str(node.value))
    node = linked_list.pop()
    print("test_pop: node that pop out: " + str(node.value))
    print_nodes(linked_list.head)


@pytest.mark.skip(reason="wait for finishing")
def test_shift():
    linked_list = test_push()
    node = linked_list.shift()
    print("test_shift: node that shift out: " + str(node.value))
    print_nodes(linked_list.head)


@pytest.mark.skip(reason="wait for finishing")
def test_unshift():
    linked_list = test_push()
    linked_list.unshift(11)
    linked_list.unshift(111)
    print_nodes(linked_list.head)


@pytest.mark.skip(reason="wait for finishing")
def test_get():
    linked_list = test_push()
    node = linked_list.get(0)
    print("test_get: " + str(node.value))
    node = linked_list.get(2)
    print("test_get: " + str(node.value))
    node = linked_list.get(3)
    print("test_get: " + str(node.value))
    node = linked_list.get(4)
    print("test_get: " + str(node.value))
    node = linked_list.get(5)
    if node is not None:
        print("test_get: " + str(node.value))


@pytest.mark.skip(reason="wait for finishing")
def test_set():
    linked_list = test_push()
    linked_list.set(0, 11)
    linked_list.set(3, 111)
    linked_list.set(4, 1111)
    linked_list.set(5, 11111)
    print_nodes(linked_list.head)


@pytest.mark.skip(reason="wait for finishing")
def test_insert():
    linked_list = test_push()
    linked_list.insert(0, 11)
    print_nodes(linked_list.head)

    linked_list.insert(4, 111)
    print_nodes(linked_list.head)

    linked_list.insert(2, 1111)
    print_nodes(linked_list.head)

    linked_list.insert(8, 8)
    print_nodes(linked_list.head)

    linked_list.insert(-1, -1)
    print_nodes(linked_list.head)


@pytest.mark.skip(reason="wait for finishing")
def test_remove():
    linked_list = test_push()
    linked_list.remove(-1)
    print_nodes(linked_list.head)

    linked_list.remove(6)
    print_nodes(linked_list.head)

    linked_list.remove(5)
    print_nodes(linked_list.head)

    linked_list.remove(0)
    print_nodes(linked_list.head)

    linked_list.remove(3)
    print_nodes(linked_list.head)

    linked_list.remove(1)
    print_nodes(linked_list.head)


@pytest.mark.skip(reason="wait for finishing")
def test_reverse():
    linked_list = test_push()
    linked_list.reverse()
    print_nodes(linked_list.head)
