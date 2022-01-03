# Where to use graphs:
# Social networks, location, routing system, visual hierarchy, file system optimizations

# Essential graph terms:
# Vertex: a node
# Edge: a connection between nodes
# Weighted/ Unweighted: values assigned to distances between vertices
# Directed/ Undirected: directions assigned to distanced between vertices

# Type of graphs:
# Undirected graph, directed graph, unweighted graph, weighted graph

# Storing graphs: adjacency matrix, adjacency list


class Graph(object):
    def __init__(self):
        super().__init__()
        self.adjancencyList = {}

    def addVertex(self, vertex):
        if vertex not in self.adjancencyList:
            self.adjancencyList[vertex] = []

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjancencyList:
            self.adjancencyList[vertex1].append(vertex2)
        if vertex2 in self.adjancencyList:
            self.adjancencyList[vertex2].append(vertex1)

    def removeEdge(self):
        return

    def removeVertex(self):
        return
