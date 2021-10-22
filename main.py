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
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deliveryTime = row[5]
        mass = row[6]
        specialNotes = row[7]

        value = [id, address, city, state, zip, deliveryTime, mass, specialNotes]
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
            # print(distanceList)
            for distance in distanceList:
                # print(distance)
                g.add_undirected_edge(*pair.keys(), locationsList[i], distance)
                i += 1

    edges = g.get_edges()
    print(edges.get(('Western Governors University', 'City Center of Rock Springs')))

# Create 3 Truck objects
    t = truck.Truck()
    # print(t.get_distance_to_next_delivery(, )

# Load packages into trucks

# Calculate distances and print
