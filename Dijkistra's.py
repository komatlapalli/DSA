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
