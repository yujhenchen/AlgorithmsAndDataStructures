import math


class Node(object):
    def __init__(self, value):
        super().__init__()
        self.next = None
        self.prev = None
        self.value = value


class DoublyLinkedList(object):
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        # create new node
        # tail.next = node
        # node.prev = tail
        # tail = node
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return

    def pop(self):
        # if length == 0, head and tail set to None
        # else, keep tail as node, set tail.prev as tail, node.prev = None, tail.next = None
        node = None
        if self.length >= 1:
            node = self.tail
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            node.prev = None
            self.length -= 1
        return node

    def shift(self):
        # remove the first node
        node = None
        if self.length >= 1:
            node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        node.next = None
        self.length -= 1
        return node

    def unshift(self, value):
        # add a node to the beginning of the linked list
        node = Node(value)
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        return

    def get(self, index):
        # return None if index >= length
        # check index is bigger or smaller than mid length
        # loop from head if index < mid length
        # loop from tail if index > mid length
        if index >= self.length or index < 0:
            return None
        else:
            mid_length = math.floor(self.length / 2)
            node = None
            if index <= mid_length:
                node = self.head
                for i in range(index):
                    node = node.next
            else:
                node = self.tail
                for i in range(self.length, index + 1, -1):
                    node = node.prev
            return node

    def set(self, index, value):
        if index >= self.length or index < 0:
            return False
        else:
            self.get(index).value = value
            return True

    def insert(self, index, value):
        # return false if index > length or index < 0
        # call unshift if index == 0
        # call push if index == length
        # call get to get node of insert position as pre_node
        # create new node, node.next = pre_node.next, node.prev= pre_node
        # pre_node.next.prev = node, pre_node.next = node
        if index >= self.length or index < 0:
            return False
        if index == 0:
            self.unshift(value)
        elif index == self.length - 1:
            self.push(value)
        else:
            pre_node = self.get(index)
            node = Node(value)
            node.next = pre_node.next
            node.prev = pre_node
            pre_node.next.prev = node
            pre_node.next = node
        self.length += 1
        return True

    def remove(self, index):
        # return false if index < 0 or >= length
        # return head if length is 1, set head and tail to None
        # call shift if index is 0
        # call pop if index is length-1
        # get the node to remove as rm_node, rm_node.prev.next = rm_node.next
        # rm_node.next.prev = rm_node.prev
        # rm_node.next = None, # rm_node.prev = None
        if index >= self.length or index < 0:
            return None
        rm_node = None
        if index == 0:
            rm_node = self.shift()
        elif index == self.length - 1:
            rm_node = self.pop()
        else:
            rm_node = self.get(index)
            rm_node.prev.next = rm_node.next
            rm_node.next.prev = rm_node.prev
            rm_node.next = rm_node.prev = None
        self.length -= 1
        return rm_node

    def reverse(self):
        self.tail = self.head
        node = self.head
        p_node = node.prev
        n_node = node.next
        while n_node is not None:
            node.next = p_node
            node.prev = n_node

            p_node = node
            node = n_node
            n_node = n_node.next
        self.head = node
        self.head.next = p_node
        self.tail.next = None
        return
