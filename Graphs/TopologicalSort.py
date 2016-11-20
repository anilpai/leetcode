from collections import defaultdict


class Graph(object):
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dict with adj list
        self.V = vertices  # no of vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortHelper(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] is False:
                self.topologicalSortHelper(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []

        for v in range(self.V):
            if visited[v] is False:
                self.topologicalSortHelper(v, visited, stack)
        print(stack)


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    print("Following is a Topological Sort of the given graph")
    g.topologicalSort()
