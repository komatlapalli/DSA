class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def bfs(self, start_vertex):
        visited = set()
        visited.add(start_vertex)
        queue = [start_vertex]
        while queue:
            vertex = queue.pop(0)
            current_vertex = vertex
            print(current_vertex)
            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            current_vertex = vertex
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

    def _topological_sort_helper(self, vertex, visited, stack):
        visited.add(vertex)
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self._topological_sort_helper(neighbor, visited, stack)
        stack.append(vertex)
        
    def topological_sort(self):
        visited = set()
        stack = []
        for vertex in self.adjacency_list:
            if vertex not in visited:
                self._topological_sort_helper(vertex, visited, stack)
        return stack[::-1]


        




myGraph = Graph()
myGraph.add_vertex("A")
myGraph.add_vertex("B")
myGraph.add_vertex("C")
myGraph.add_vertex("D")
myGraph.add_edge("A", "B")
myGraph.add_edge("A", "D")
myGraph.add_edge("A", "C")  
myGraph.add_edge("B", "C")
myGraph.dfs("A")



