# Each parent has at most two child nodes
# The left and right node have no order
# A binary heap is as compact as possible.
# All the children of each node are as full as they can be and left children are filled out first

# MaxBinaryHeap: parent nodes are always larger than child nodes
# MinBinaryHeap: parent nodes are always smaller than child nodes

# Sorting Heaps:
# Has parent to find child: For any index of an array n, the left child is sorted at 2n+1, the right child is at 2n+2
# Has child to find parent: For any child node at index n, Its parent is at index floor(( n-1)/2 )


class MaxBinaryHeap(object):
    def __init__(self):
        super().__init__()
        self.values = []
