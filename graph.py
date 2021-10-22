# Source: zybooks
# import queue


class Vertex:
    def __init__(self, label):
        self.label = label


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def get_vertices(self):
        return self.adjacency_list

    def get_edges(self):
        return self.edge_weights

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    # def breadth_first_search(self, start_vertex):
    #     discovered_set = []
    #     frontier_queue = queue.LifoQueue()
    #
    #     frontier_queue.push(start_vertex)  # Push start_vertex to frontier_queue
    #     discovered_set.append(start_vertex)  # Add start_vertex to discovered_set
    #
    #     while (frontier_queue.list.head is not None):  # While the queue is not empty
    #         current_vertex = frontier_queue.pop()  # current_vertex is currently visited
    #         for adjacent_vertex in self.adjacency_list[current_vertex]:
    #             if (discovered_set.count(adjacent_vertex) == 0):
    #                 frontier_queue.push(adjacent_vertex)
    #                 discovered_set.append(adjacent_vertex)
    #                 # Distance of adjacent_vertex is 1 more than current_vertex
    #                 adjacent_vertex.distance = current_vertex.distance + 1
    #
    #     return discovered_set
