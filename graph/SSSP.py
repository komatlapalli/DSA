class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        """
        This function implements the breadth first search algorithm to find the 
        shortest path between two nodes in a graph. This function is only applicable
        for unweighted graphs. The function takes in the starting node and the ending node 
        as input and returns the shortest path between the two nodes as a list.
        """
        queue = [[start]]
        while queue:
            # print("Queue:", queue)
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                # print("Queue:", queue)

g = {"0": ["1", "2"],
"1": ["0", "3", "4"],
"2": ["0", "4"],
"3": ["1", "4", "5"],
"4": ["1", "2", "3"],
"5": ["3"]}
graph = Graph(g)
print(graph.bfs("0", "5"))