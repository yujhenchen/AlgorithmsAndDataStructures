import pytest
from binaryheap import MaxBinaryHeap


def print_heap(binaryheap):
    for node in binaryheap.values:
        print(node.value)


@pytest.mark.skip(reason="wait for finishing")
def test_insert():
    binaryheap = MaxBinaryHeap()
    binaryheap.insert(1)
    binaryheap.insert(5)
    binaryheap.insert(8)
    binaryheap.insert(17)
    binaryheap.insert(9)
    # print_heap(binaryheap)
    return binaryheap


#@pytest.mark.skip(reason="wait for finishing")
def test_extractMax():
    binaryheap = test_insert()
    binaryheap.extractMax()
    #print_heap(binaryheap)


@pytest.mark.skip(reason="wait for finishing")
def test_queue():
    binaryheap = test_insert()
    print_heap(binaryheap)
