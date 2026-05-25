import heapq

#class Edges

class Edge:
    def __init__(self,weight, startVertex, endVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.endVertex = endVertex

#class for nodes
class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        # initially set the minimum distance to infinity
        self.minDistance = float('inf')

    def __lt__(self, other_node):
        return self.minDistance < other_node.minDistance
    
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)

# Dijkstra's algorithm implementation
class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.minDistance = 0
        heapq.heappush(self.heap, start_vertex)

        while self.heap:
            actual_vertex = heapq.heappop(self.heap)

            if actual_vertex.visited:
                continue

            for edge in actual_vertex.neighbors:
                start = edge.startVertex
                target = edge.endVertex
                new_distance = start.minDistance + edge.weight

                if new_distance < target.minDistance:
                    target.predecessor = start
                    target.minDistance = new_distance
                    heapq.heappush(self.heap, target)

            actual_vertex.visited = True


    def get_shortest_path(self, target_vertex):
        print(f"Shortest path to {target_vertex.name} is: {target_vertex.minDistance}")
        actual_vertex = target_vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=' ')
            actual_vertex = actual_vertex.predecessor
        

# Create vertices
vertexA = Node('A')
vertexB = Node('B')
vertexC = Node('C')
vertexD = Node('D')
vertexE = Node('E')
# Add edges
vertexA.add_edge(10, vertexB)
vertexA.add_edge(15, vertexC)
vertexB.add_edge(12, vertexD)
vertexB.add_edge(15, vertexE)
vertexC.add_edge(10, vertexE)
vertexD.add_edge(2, vertexE)        

# Calculate shortest paths from vertex A
dijkstra = Dijkstra()
dijkstra.calculate(vertexA) 
dijkstra.get_shortest_path(vertexE)
