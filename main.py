# Main
import csv
import datetime

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

# Create/Load 3 Truck objects
    t1 = truck.Truck()
    t1.departureTime = datetime.time(8)
    t1.packageList = [1, 2, 12, 4, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

    t2 = truck.Truck()
    t2.departureTime = datetime.time(9, 5)
    t2.packageList = [3, 5, 6, 7, 10, 11, 17, 18, 25, 28, 32, 33, 35, 36, 38, 39]

    t3 = truck.Truck()
    t3.packageList = [8, 9, 21, 22, 23, 24, 26, 27]

# UI
print("******WELCOME TO THE WGUPS PACKAGE TRACKING SYSTEM*****\n")
print("PLEASE MAKE A SELECTION:\n")
selection = input("1) RUN PACKAGE DELIVERY SIMULATION\n"
                  "2) LOOKUP PACKAGE STATUS BY TIME\n")

# Calculate distances and print
if selection == '1':
    print("NOW DELIVERING PACKAGES...")

arrivalLog = {}

# Truck 1
t1.deliver_to_nearest_neighbors(h, g, arrivalLog)

# Truck 2
t2.deliver_to_nearest_neighbors(h, g, arrivalLog)

# compare departure time + travel time of t1 and t2, then send truck that is finished
# first back to hub, then set t3 departure time to time of arrival at hub
t1_datetime = datetime.datetime.combine(datetime.date.today(), t1.departureTime)
t1CompletionDatetime = t1_datetime + datetime.timedelta(hours=t1.travelTime)

t2_datetime = datetime.datetime.combine(datetime.date.today(), t2.departureTime)
t2CompletionDatetime = t2_datetime + datetime.timedelta(hours=t2.travelTime)

if t1CompletionDatetime.time() < t2CompletionDatetime.time():
    t3.departureTime = t1CompletionDatetime.time()
else:
    t3.departureTime = t2CompletionDatetime.time()

# Truck 3
t3.deliver_to_nearest_neighbors(h, g, arrivalLog)

if selection == '1':
    print("TOTAL MILEAGE: " + str(t1.travelMileage + t2.travelMileage + t3.travelMileage)[0: 6] + " miles")
    print("TOTAL DELIVERY TIME: " + str(t1.travelTime + t2.travelTime + t3.travelTime)[0: 5] + " hours")
    print("THANK YOU FOR USING WGUPS - GOODBYE")

# Track packages
elif selection == '2':
    time = input("PLEASE ENTER TIME TO CHECK PACKAGE STATUS(HH:MM:SS):\n")
    time = datetime.datetime.strptime(time, '%H:%M:%S').time()
    for package in arrivalLog:
        if arrivalLog.get(package).time() <= time:
            print("#" + str(package) + " has been delivered at " + str(arrivalLog.get(package)))
        else:
            if time < t1.departureTime:
                print("#" + str(package) + " is at hub")
            elif t1.departureTime <= time < t2.departureTime:
                if package in t1.packageList:
                    print("#" + str(package) + " is en route")
                else:
                    print("#" + str(package) + " is at hub")
            elif t2.departureTime <= time < t3.departureTime:
                if package in t1.packageList or package in t2.packageList:
                    print("#" + str(package) + " is en route")
                else:
                    print("#" + str(package) + " is at hub")
            else:
                print("#" + str(package) + " is en route")

else:
    print("INVALID INPUT. TYPE 1 OR 2 TO MAKE SELECTION.")
