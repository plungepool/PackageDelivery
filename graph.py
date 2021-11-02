# Graph class
""" Portions of code adapted from:
Lysecky, Roman, and Frank Vahid. C950: Data Structures and Algorithms II. 2018th ed., Zybooks. """


# Class representing a graph of vertices and edges
class Graph:
    # Initialize graph with dictionaries for adjacency list and edge weights
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    # Return all vertices
    # Time complexity of O(1)
    def get_vertices(self):
        return self.adjacency_list

    # Return all edges
    # Time complexity of O(1)
    def get_edges(self):
        return self.edge_weights

    # Add a new vertex
    # Time complexity of O(1)
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    # Add a new directed edge
    # Time complexity of O(1)
    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    # Add a new undirected edge
    # Time complexity of O(1)
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
