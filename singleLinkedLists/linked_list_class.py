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
            self.tail.next = None
            self.length += 1

    def pop(self):
        # if length is 1, set head and tail to None
        # else loop head till length-1 get the node before tail
        # set next of the node to None
        # set tail to the node
        # length --
        if self.length < 1:
            return self, None
        pop_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            node_before_tail = self.head
            while node_before_tail.next is not self.tail:
                node_before_tail = node_before_tail.next
            node_before_tail.next = None
            self.tail = node_before_tail
        self.length -= 1
        return pop_node

    def shift(self):
        # remove a node from the befinning of the list
        # if length < 1
        # if length == 1, set pop_node to head, set head and tail to none, legth --
        # else set head to next of pre head, set pop_node = head, set next of pre head to None, legth --
        if self.length < 1:
            return self, None
        pop_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = pop_node.next
            pop_node.next = None
        self.length -= 1
        return pop_node

    def unshift(self, value):
        # add a node to the beginning of the list
        new_head = Node(value)
        if self.length < 1:
            self.head = new_head
            self.tail = new_head
        else:
            new_head.next = self.head
            self.head = new_head
        self.length += 1

    def get(self, index):
        if index > self.length - 1 or index < 0:
            return None
        curr_node = self.head
        curr_index = 0
        while curr_index is not index:
            curr_node = curr_node.next
            curr_index += 1
        return curr_node

    def set(self, index, value):
        if index > self.length - 1 or index < 0:
            return None
        curr_node = self.head
        curr_index = 0
        while curr_index is not index:
            curr_node = curr_node.next
            curr_index += 1
        curr_node.value = value

    def insert(self):
        return

    def remove(self):
        return

    def reverse(self):
        return
