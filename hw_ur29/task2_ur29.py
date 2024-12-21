"""
Using breadth-first search write an algorithm that can determine the shortest path from each vertex to every other vertex.
This is called the all-pairs shortest path problem.
"""

import heapq

class WeightedGraph:
    def __init__(self):
        self.vertex_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertex_dict:
            self.vertex_dict[vertex] = []

    def add_edge(self, vertex_1, vertex_2, weight):
        if vertex_1 in self.vertex_dict and vertex_2 in self.vertex_dict:
            self.vertex_dict[vertex_1].append((vertex_2, weight))
            if vertex_1 != vertex_2:
                self.vertex_dict[vertex_2].append((vertex_1, weight))

    def display(self):
        for vertex, linked_vertexes in self.vertex_dict.items():
            print(f"{vertex}: {linked_vertexes}")

def dijkstra_algorithm_from_to(graph: WeightedGraph, start, end):
    priority_queue = [(0, start)]  # (cost, vertex)
    distances = {vertex: float('inf') for vertex in graph.vertex_dict}
    distances[start] = 0
    previous = {vertex: None for vertex in graph.vertex_dict}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If we reach the end vertex, break
        if current_vertex == end:
            break

        for neighbor, weight in graph.vertex_dict[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous[current]

    return distances[end], path


def all_pairs_shortest_paths(graph: WeightedGraph):
    all_paths = {}
    for start_vertex in graph.vertex_dict:
        all_paths[start_vertex] = {}
        for end_vertex in graph.vertex_dict:
            if start_vertex != end_vertex:
                distance, path = dijkstra_algorithm_from_to(graph, start, end)
                all_paths[start_vertex][end_vertex] = {"distance": distance, "path": path}
            else:
                all_paths[start_vertex][end_vertex] = {"distance": 0, "path": [start_vertex]}
    return all_paths


def all_pairs_shortest_paths(graph: WeightedGraph):
    all_paths = {}
    for start_vertex in graph.vertex_dict:
        all_paths[start_vertex] = {}
        for end_vertex in graph.vertex_dict:
            if start_vertex != end_vertex:
                distance, path = dijkstra_algorithm_from_to(graph, start_vertex, end_vertex)
                all_paths[start_vertex][end_vertex] = {"distance": distance, "path": path}
            else:
                all_paths[start_vertex][end_vertex] = {"distance": 0, "path": [start_vertex]}
    return all_paths



graph = WeightedGraph()
for vertex in ['A', 'B', 'C', 'D', 'E']:
    graph.add_vertex(vertex)
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 8)
    graph.add_edge('C', 'E', 10)
    graph.add_edge('D', 'E', 2)

    print("All-Pairs Shortest Paths:")
    results = all_pairs_shortest_paths(graph)
    for start, destinations in results.items():
        for end, data in destinations.items():
            print(f"Shortest path from {start} to {end}: Distance = {data['distance']}, Path = {data['path']}")
