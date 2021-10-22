# Main
import csv
import hash
import graph
import truck

# Hash Packages
with open('WGUPS Package File.csv') as packageFile:
    read_csv = csv.reader(packageFile, delimiter=',')
    h = hash.HashMap()

    for row in read_csv:
        id = row[0]
        location = row[1]
        address = row[2]
        city = row[3]
        state = row[4]
        zip = row[5]
        deliveryTime = row[6]
        mass = row[7]
        specialNotes = row[8]

        value = [id, location, address, city, state, zip, deliveryTime, mass, specialNotes]
        h.add(id, value)

# Graph Delivery Table
with open('WGUPS Distance Table.csv') as distanceFile:
    read_csv = csv.reader(distanceFile, delimiter=',')
    adjacencyList = []

    count = 0
    for row in read_csv:
        distances = []
        i = 0
        for column in row:
            if column == '':
                break
            if i == 0:
                key = column
                i += 1
                continue
            distances.append(column)
            i += 1
        newItem = {key: distances}
        count += 1
        adjacencyList.append(newItem)

    g = graph.Graph()
    locationsList = []
    for pair in adjacencyList:
        g.add_vertex(*pair.keys())
        locationsList.append(*pair.keys())

    for pair in adjacencyList:
        i = 0
        for distanceList in pair.values():
            for distance in distanceList:
                g.add_undirected_edge(*pair.keys(), locationsList[i], distance)
                i += 1

# Create 3 Truck objects
    t1 = truck.Truck()
    # t1.departureTime.hour = 8
    # t1.departureTime.minute = 0
    t1.packageList = [1, 2, 12, 4, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

    t2 = truck.Truck()
    # t2.departureTime.hour = 9
    # t2.departureTime.minute = 5
    t2.packageList = [3, 5, 6, 7, 10, 11, 17, 18, 25, 28, 32, 33, 35, 36, 38, 39]

    t3 = truck.Truck()
    # t3.departureTime.hour = 10
    # t3.departureTime.minute = 20
    t3.packageList = [8, 9, 21, 22, 23, 24, 26, 27]

    print(t1.get_distance_to_next_delivery(g, t1.currentLocation, 'City Center of Rock Springs'))

# Load packages into trucks

# Calculate distances and print
