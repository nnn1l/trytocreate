"""
Modify the 'depth-first search' to produce strongly connected components
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertex_dict = defaultdict(list)

    def add_edge(self, source, destination):
        """Add a directed edge from source to destination."""
        self.vertex_dict[source].append(destination)

    def dfs(self, vertex, visited, stack=None):
        """Depth-First Search (DFS)."""
        visited[vertex] = True
        for neighbor in self.vertex_dict[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        if stack is not None:
            stack.append(vertex)

    def reverse(self):
        """Reverses the graph's edges."""
        reversed_graph = Graph()
        for vertex in self.vertex_dict:
            for neighbor in self.vertex_dict[vertex]:
                reversed_graph.add_edge(neighbor, vertex)  # Reverse the edge
        return reversed_graph

    def find_sccs(self):
        stack = []
        visited = {vertex: False for vertex in self.vertex_dict}
        for vertex in self.vertex_dict:
            if not visited[vertex]:
                self.dfs(vertex, visited, stack)

        reversed_graph = self.reverse()

        visited = {vertex: False for vertex in self.vertex_dict}
        sccs = []
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                scc = []
                reversed_graph.dfs(vertex, visited, scc)
                sccs.append(scc)  # Add the collected SCC
        return sccs


if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'A')
    g.add_edge('B', 'D')
    g.add_edge('D', 'E')
    g.add_edge('E', 'F')
    g.add_edge('F', 'D')
    g.add_edge('G', 'F')
    g.add_edge('G', 'H')
    g.add_edge('H', 'I')
    g.add_edge('I', 'J')
    g.add_edge('J', 'G')

    print("Strongly Connected Components:")
    sccs = g.find_sccs()
    for idx, scc in enumerate(sccs, start=1):
        print(scc)
