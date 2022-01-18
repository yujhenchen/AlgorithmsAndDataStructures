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


class GraphTraversal(object):
    def __init__(self):
        super().__init__()
        self.adjancencyList = {}

    def addVertex(self, vertex):
        if vertex not in self.adjancencyList:
            self.adjancencyList[vertex] = []

    def addEdge(self, vertex1, vertex2):
        if vertex2 not in self.adjancencyList[vertex1]:
            self.adjancencyList[vertex1].append(vertex2)
        if vertex1 not in self.adjancencyList[vertex2]:
            self.adjancencyList[vertex2].append(vertex1)

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjancencyList:
            self.adjancencyList[vertex1].remove(vertex2)
        if vertex2 in self.adjancencyList:
            self.adjancencyList[vertex2].remove(vertex1)

    def removeVertex(self, vertex):
        for key in self.adjancencyList:
            if vertex in self.adjancencyList[key]:
                self.adjancencyList[key].remove(vertex)
        del self.adjancencyList[vertex]

    def dfs(vertex):
        result = []
        visited = {}

        return result

    def bfs():
        return
