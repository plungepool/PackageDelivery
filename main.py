# Main
import csv
import hash

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

    print(h.get('3'))