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
        while node.value > parentNode.value and nodeIndex is not 0:
            self.values[nodeIndex] = parentNode
            self.values[parentNodeIndex] = node
            # bubble up
            nodeIndex = parentNodeIndex
            parentNodeIndex = math.floor((nodeIndex - 1) / 2)
            parentNode = self.values[parentNodeIndex]
        return

    def extractMax(self):
        # remove the max node from the heap
        # replace with the most recent added node (so it becomes new root)
        # adjust (sink down): compare the new root (the node) with children, replace the current root with the child which has biggest value
        # loop until the node with its children until none of children is greater than the node
        # sink down: the procedure for deleting the root from the heap (effectively extracting the maximum element
        # in a max-heap or the minimum element in a min-heap) and restoring the properties is called down-heap
        # also called bubble-down, ...
        return

    def queue(self):
        return
