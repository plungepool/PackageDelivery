# Truck class
import datetime


class Truck:
    def __init__(self):
        self.packageList = []
        self.size = 16
        self.speed_MPH = 18
        self.departureTime = datetime.time()
        self.currentLocation = 'Western Governors University'
        self.travelMileage = 0.0
        self.travelTime = 0.0

    def get_distance_to_delivery(self, graph, start, end):
        edges = graph.get_edges()
        return edges.get((start, end))

    def deliver_to_nearest_neighbors(self, hash, graph, arrivallog):
        package_list = self.packageList.copy()
        for i in range(len(package_list)):
            min_id = int
            min_location = str
            min_distance = 99999.0
            departure_datetime = datetime.datetime.combine(datetime.date.today(), self.departureTime)
            for package in package_list:
                next_location_name = hash.get(str(package))[1]
                next_location_distance = float(self.get_distance_to_delivery(graph, self.currentLocation, next_location_name))
                if next_location_distance < min_distance:
                    min_id = package
                    min_location = next_location_name
                    min_distance = next_location_distance
            self.travelMileage += min_distance
            self.travelTime += min_distance / 18
            self.currentLocation = min_location
            arrivallog[min_id] = departure_datetime + datetime.timedelta(hours=self.travelTime)
            package_list.remove(min_id)
        self.return_to_hub(graph)

    def return_to_hub(self, g):
        next_location_name = 'Western Governors University'
        next_location_distance = float(self.get_distance_to_delivery(g, self.currentLocation, next_location_name))
        self.travelMileage += next_location_distance
        self.travelTime += next_location_distance / 18
        self.currentLocation = next_location_name
