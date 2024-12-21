from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)  # Adjacency list representation

    def add_edge(self, source, destination):
        """Adds a directed edge from source to destination."""
        self.graph[source].append(destination)

    def dfs(self, vertex, visited, stack):
        """Depth-First Search to process a vertex."""
        visited[vertex] = True
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(vertex)  # Add the vertex to the stack after visiting its neighbors

    def reverse(self):
        """Reverses the direction of all edges in the graph."""
        reversed_graph = Graph(self.num_vertices)
        for source in self.graph:
            for destination in self.graph[source]:
                reversed_graph.add_edge(destination, source)
        return reversed_graph

    def fill_order(self):
        """Performs DFS and returns vertices in decreasing order of finish time."""
        visited = [False] * self.num_vertices
        stack = []
        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                self.dfs(vertex, visited, stack)
        return stack

    def find_sccs(self):
        """Finds and returns all Strongly Connected Components (SCCs) in the graph."""
        # Step 1: Perform DFS and get vertices in finish time order
        stack = self.fill_order()

        # Step 2: Reverse the graph
        reversed_graph = self.reverse()

        # Step 3: Perform DFS on the reversed graph
        visited = [False] * self.num_vertices
        sccs = []

        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                scc = []
                reversed_graph.collect_scc(vertex, visited, scc)
                sccs.append(scc)

        return sccs

    def collect_scc(self, vertex, visited, scc):
        """Helper function to collect vertices of an SCC using DFS."""
        visited[vertex] = True
        scc.append(vertex)
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.collect_scc(neighbor, visited, scc)


g = Graph(5)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(1, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:")
sccs = g.find_sccs()
for scc in sccs:
    print(scc)
