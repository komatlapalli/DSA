from collections import defaultdict
class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.vertices = numberOfVertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
    

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited=[]
        stack =[]
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)

        print(stack)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)         
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")
g.topologicalSort()
print(g.graph)

        
