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
        # if index > self.length - 1 or index < 0:
        #     return None
        # curr_node = self.head
        # curr_index = 0
        # while curr_index is not index:
        #     curr_node = curr_node.next
        #     curr_index += 1

        # call get to get the found node and set value
        found_node = self.get(index)
        if found_node is None:
            return False
        else:
            found_node.value = value
            return True

    def insert(self, index, value):
        # if head, call unshift
        # else if tail, call push
        # else, create a new node with the value
        # next node = pre.next
        # pre.next = node
        # node.next = next node
        # length ++
        if index >= self.length or index < 0:
            return False

        if index == self.length - 1:
            self.push(value)
        elif index == 0:
            self.unshift(value)
        else:
            pre_node = self.get(index)
            pre_node_next = pre_node.next
            node = Node(value)
            pre_node.next = node
            node.next = pre_node_next
            self.length += 1
        return True

    def remove(self, index):
        # if head, call shift
        # if tail, call pop
        # get node before target node
        # pre.next = target.next
        # target.next = None
        if index >= self.length or index < 0:
            return None
        node = None
        if index == 0:
            node = self.shift()
        elif index == self.length - 1:
            node = self.pop()
        else:
            pre_node = self.get(index - 1)
            target_node = pre_node.next
            pre_node.next = target_node.next
            target_node.next = None
            self.length -= 1
        return node

    def reverse(self):
        return
