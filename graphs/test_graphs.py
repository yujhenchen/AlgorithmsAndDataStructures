from graphs import Graph


def printGraph(graph):
    print(graph.adjancencyList)
    print()


def testAddVertex():
    graph = Graph()
    graph.addVertex("A")
    graph.addVertex("B")
    graph.addVertex("C")
    printGraph(graph)
    return graph


def testAddEdge():
    graph = testAddVertex()
    graph.addEdge("A", "C")
    graph.addEdge("B", "C")
    printGraph(graph)
    return graph


def testRemoveEdge():
    graph = testAddEdge()
    graph.removeEdge("B", "C")
    printGraph(graph)
    return graph


def testRemoveVertex():
    graph = testAddEdge()
    graph.removeVertex("B")
    printGraph(graph)
    return graph
