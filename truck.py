# Truck class

import datetime
import graph

class Truck:
    def __init__(self):
        self.packageList = []
        self.size = 16
        self.speed_MPH = 18
        self.departureTime = datetime.time
        self.currentLocation = 'Western Governors University'
        self.travelMileage = 0.0
        self.travelTime = 0.0

    def get_distance_to_next_delivery(self, graph, start, end):
        edges = graph.get_edges()
        return edges.get((start, end))
