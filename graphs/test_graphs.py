from graphs import Graph


def testAddVertex():
    graph = Graph()
    graph.addVertex("A")
    graph.addVertex("B")
    graph.addVertex("C")
    # print(graph.adjancencyList)
    return graph


def testAddEdge():
    graph = testAddVertex()
    graph.addEdge("A", "C")
    graph.addEdge("B", "C")
    print(graph.adjancencyList)


def testRemoveEdge():
    return


def testRemoveVertex():
    return
