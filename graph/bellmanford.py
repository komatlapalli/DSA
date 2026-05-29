#bellmanford algorithm

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes=[]

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def add_node(self, name):
        self.nodes.append(name)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{self.nodes[i]} \t\t {dist[i]}")

    def bellman_ford(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float('inf') and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float('inf') and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(dist)


g = Graph(5)
g.add_node("A")                 
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")

g.add_edge(0, 1, 10)  # A -> B
g.add_edge(0, 2, 5)   # A -> C
g.add_edge(1, 2, 2)   # B -> C
g.add_edge(1, 3, 1)   # B -> D
g.add_edge(2, 1, 3)   # C -> B
g.add_edge(2, 3, 9)   # C -> D
g.add_edge(2, 4, 2)   # C -> E
g.add_edge(3, 4, 4)   # D -> E
g.add_edge(4, 3, 6)   # E -> D  

g.bellman_ford(0)  # Calculate shortest paths from vertex A (index 0)

