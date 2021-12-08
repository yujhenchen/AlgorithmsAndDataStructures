# Each parent has at most two child nodes
# The left and right node have no order
# A binary heap is as compact as possible.
# All the children of each node are as full as they can be and left children are filled out first

# MaxBinaryHeap: parent nodes are always larger than child nodes
# MinBinaryHeap: parent nodes are always smaller than child nodes

# Sorting Heaps:
# Has parent to find child: For any index of an array n, the left child is sorted at 2n+1, the right child is at 2n+2
# Has child to find parent: For any child node at index n, Its parent is at index floor(( n-1)/2 )

import math


class Node(object):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.left = None
        self.right = None


class MaxBinaryHeap(object):
    def __init__(self):
        super().__init__()
        self.values = []

    def insert(self, value):
        # add to the end
        # bubble up: take the newly inserted node to compare with parent node and swap if it is greater than parent node
        # and keep comparing and swaping until it reach to the root
        # find the parent of the node: use the formula and the nodes that are in values array
        node = Node(value)
        self.values.append(node)

        if len(self.values) == 0:
            return

        nodeIndex = len(self.values) - 1
        parentNodeIndex = math.floor((nodeIndex - 1) / 2)
        parentNode = self.values[parentNodeIndex]
        while node.value > parentNode.value:
            self.values[nodeIndex] = parentNode
            self.values[parentNodeIndex] = node
            # bubble up
            nodeIndex = parentNodeIndex
            parentNodeIndex = math.floor((nodeIndex - 1) / 2)
            parentNode = self.values[parentNodeIndex]
        return

    def extractMax(self):
        return

    def queue(self):
        return
