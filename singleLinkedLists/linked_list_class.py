class Node(object):
    def __init__(self, value):
        super().__init__()
        self.next = None
        self.value = value


class SingleLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.tail.next = node
            self.tail = node

    def pop(self):
        return

    def shift(self):
        return

    def unshift(self):
        return

    def get(self):
        return

    def set(self):
        return

    def insert(self):
        return

    def remove(self):
        return

    def reverse(self):
        return


if __name__ == "__main__":
    # test linked list nodes usage
    # node1 = Node(1)
    # node2 = Node(2)
    # node1.next = node2
    # head = node1
    # while head is not None:
    #     print(head.value)
    #     head = head.next

    linked_list = SingleLinkedList()

    # push
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    curr = linked_list.head
    while curr is not None:
        print(curr.value)
        curr = curr.next

    # pop

    # shift

    # unshift

    # get

    # set

    # insert

    # remove

    # reverse
