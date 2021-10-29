# Truck class
import datetime


# Return distance on a graph between two vertices
# Vertices pair used as the index when accessing the list
# Time complexity of O(1)
def get_distance_to_delivery(graph, start, end):
    edges = graph.get_edges()
    return edges.get((start, end))


# Class representing a delivery truck
class Truck:
    def __init__(self):
        # Initialize truck with beginning-of-day properties
        self.packageList = []
        self.size = 16
        self.speed_MPH = 18
        self.departureTime = datetime.time()
        self.currentLocation = 'Western Governors University'
        self.travelMileage = 0.0
        self.travelTime = 0.0

    # Apply **Nearest Neighbor Algorithm** to determine sequence of package deliveries
    # Self-adjusting heuristic
    # Time complexity of O(n^2)
    def deliver_to_nearest_neighbors(self, hash, graph, arrivallog):
        package_list = self.packageList.copy()
        for i in range(len(package_list)):
            min_id = int
            min_location = str
            min_distance = 99999.0
            departure_datetime = datetime.datetime.combine(datetime.date.today(), self.departureTime)
            for package in package_list:
                next_location_name = hash.get(str(package))[1]
                next_location_distance = float(get_distance_to_delivery(graph, self.currentLocation,
                                                                        next_location_name))
                if next_location_distance < min_distance:
                    min_id = package
                    min_location = next_location_name
                    min_distance = next_location_distance
            self.travelMileage += min_distance
            self.travelTime += min_distance / self.speed_MPH
            self.currentLocation = min_location
            arrivallog[min_id] = departure_datetime + datetime.timedelta(hours=self.travelTime)
            package_list.remove(min_id)
        self.return_to_hub(graph)

    # Return the truck to hub from wherever it currently is
    # Time complexity of O(1)
    def return_to_hub(self, g):
        next_location_name = 'Western Governors University'
        next_location_distance = float(get_distance_to_delivery(g, self.currentLocation, next_location_name))
        self.travelMileage += next_location_distance
        self.travelTime += next_location_distance / self.speed_MPH
        self.currentLocation = next_location_name
