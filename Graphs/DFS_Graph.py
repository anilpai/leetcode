
from collections import defaultdict


class Graph(object):

    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        '''
        Function to add an edge to graph.
        '''
        self.graph[u].append(v)

    def DFSutil(self, v, visited):

        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSutil(i, visited)

    def DFS(self, v):
        '''
        Function to print a DFS of a graph
        '''
        visited = [False] * (len(self.graph))

        for i in range(len(self.graph)):
            if visited[i] is False:
                self.DFSutil(v, visited)


if __name__=='__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("DFS Traversal")
    g.DFS(2)
