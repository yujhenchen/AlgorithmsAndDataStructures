from graphTraversal import GraphTraversal


def printGraph(graph):
    print(graph.adjancencyList)
    print()


def addVertexEdges():
    graph = GraphTraversal()
    graph.addVertex("A")
    graph.addVertex("B")
    graph.addVertex("C")
    graph.addVertex("D")
    graph.addVertex("E")

    graph.addEdge("A", "B")
    graph.addEdge("A", "C")
    graph.addEdge("B", "A")
    graph.addEdge("B", "D")
    graph.addEdge("C", "A")
    graph.addEdge("C", "D")
    graph.addEdge("C", "E")
    graph.addEdge("D", "B")
    graph.addEdge("D", "C")
    graph.addEdge("D", "E")
    graph.addEdge("E", "C")
    graph.addEdge("E", "D")
    return graph


def test_dfs():
    graph = addVertexEdges()
    printGraph(graph)


def test_bfs():
    graph = addVertexEdges()
    # printGraph(graph)
