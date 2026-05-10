class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)



customDict = { "a" : ["d"],
               "b" : ["c"],
               "c" : ["b", "c", "d", "e"],
               "d" : ["a", "c"],
               "e" : ["c"],
               "f" : []}

g = Graph(customDict)
g.addEdge("a","f")
g.addEdge("f","a")
print(g.gdict)
