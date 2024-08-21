from Package import Package
from CreateHashTable import CreateHashMap
import datetime
from Truck import Truck
from Data import addressData, distanceData


#Shane Hasart C950 student ID:010749437
#create all 40 package objects using the package class
p1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, "10:30AM", 21, "n/a","0",  "At Hub", "0")
p2 = Package(2, "2530 S 500 E", "Salt Lake City", "Ut", 84106, "EOD", 44, "n/a", "0", "At Hub", "0")
p3 = Package(3, "233 Canyon Rd", "Salt Lake City", "UT", 84103, "EOD", 2, "Can only be on truck 2", "0", "At Hub", "0")
p4 = Package(4, "380 W 2880 S", "Salt Lake City", "UT", 84115, "EOD", 4, "n/a", "0", "At Hub", "0")
p5 = Package(5, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", 5, "n/a", "0", "At Hub", "0")
p6 = Package(6, "3060 Lester St", "West Valley City", "UT", 84119, "10:30AM", 88, "Arrives at 9:05AM", "0", "At Hub", "0")
p7 = Package(7, "1330 2100 S", "Salt Lake City", "UT", 84106, "EOD", 8, "n/a", "0", "At Hub", "0")
p8 = Package(8, "300 State St", "Salt Lake City", "UT", 84103, "EOD", 9, "n/a",  "0", "At Hub", "0")
p9 = Package(9, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", 2, "Wrong address listed", "0", "At Hub", "0")
p10 = Package(10, "600 E 900 South", "Salt Lake City", "UT", 84105, "EOD", 1, "n/a", "0", "At Hub", "0")
p11 = Package(11, "2600 Taylorsville Blvd", "Salt Lake City", "UT", 84118, "EOD", 1, "n/a", "0", "At Hub", "0")
p12 = Package(12, "3575 W Valley Central Station bus Loop", "West Valley City", "UT", 84119, "EOD", 1, "n/a", "0", "At Hub", "0")
p13 = Package(13, "2010 W 500 S", "Salt Lake City", "UT", 84104, "10:30AM", 2, "n/a", "0", "At Hub", "0")
p14 = Package(14, "4300 S 1300 E", "Millcreek", "UT", 84117, "10:30AM", 88, "Must be delivered with 15, 19", "0", "At Hub", "0")
p15 = Package(15, "4580 S 2300 E", "Holladay", "UT", 84117, "9:00AM", 4, "n/a", "0", "At Hub", "0")
p16 = Package(16, "4580 S 2300 E", "Holladay", "UT", 84117, "10:30AM", 88, "Must be delivered with 13, 19", "0", "At Hub", "0")
p17 = Package(17, "3148 S 1100 W", "Salt Lake City", "UT", 84119, "EOD", 2, "n/a", "0", "At Hub", "0")
p18 = Package(18, "1488 4800 S", "Salt Lake City", "UT", 84123, "EOD", 6, "Can only be on truck 2", "0", "At Hub", "0")
p19 = Package(19, "177 W Price Ave", "Salt Lake City", "UT", 84115, "EOD", 37, "n/a", "0", "At Hub", "0")
p20 = Package(20, "3595 Main St", "Salt Lake City", "UT", 84115, "10:30AM", 37, "Must be delivered with 13, 15", "0", "At Hub", "0")
p21 = Package(21, "3595 Main St", "Salt Lake City", "UT", 84115, "EOD", 3, "n/a", "0", "At Hub", "0")
p22 = Package(22, "6351 South 900 East", "Murray", "UT", 84121, "EOD", 2, "n/a", "0", "At Hub", "0")
p23 = Package(23, "5100 South 2700 West", "Salt Lake City", "UT", 84118, "EOD", 5, "n/a", "0", "At Hub", "0")
p24 = Package(24, "5025 State St", "Murray", "UT", 84107, "EOD", 7, "n/a", "0", "At Hub", "0")
p25 = Package(25, "5383 South 900 East #104", "Salt Lake City", "UT", 84117, "10:30AM", 7, "Arrives at 9:05AM", "0", "At Hub", "0")
p26 = Package(26, "5383 South 900 East #104", "Salt Lake City", "UT", 84117, "EOD", 25, "n/a", "0", "At Hub", "0")
p27 = Package(27, "1060 Dalton Ave S", "Salt Lake City", "UT", 84104, "EOD", 5, "n/a", "0", "At Hub", "0")
p28 = Package(28, "2835 Main St", "Salt Lake City", "UT", 84115, "EOD", 7, "Arrives at 9:05AM", "0", "At Hub", "0")
p29 = Package(29, "1330 2100 S", "Salt Lake City", "UT", 84106, "10:30AM", 2, "n/a", "0", "At Hub", "0")
p30 = Package(30, "300 State St", "Salt Lake City", "UT", 84103, "10:30AM", 1, "n/a", "0", "At Hub", "0")
p31 = Package(31, "3365 S 900 W", "Salt Lake City", "UT", 84119, "10:30AM", 1, "n/a", "0", "At Hub", "0")
p32 = Package(32, "3365 S 900 W", "Salt Lake City", "UT", 84119, "EOD", 1, "Arrives at 9:05AM", "0", "At Hub", "0")
p33 = Package(33, "2530 S 500 E", "Salt Lake City", "UT", 84106, "EOD", 1, "n/a", "0", "At Hub", "0")
p34 = Package(34, "4580 S 2300 E", "Holladay", "UT", 84117, "10:30AM", 2, "n/a", "0", "At Hub", "0")
p35 = Package(35, "1060 Dalton Ave S", "Salt Lake City", "UT", 84104, "EOD", 88, "n/a", "0", "At Hub", "0")
p36 = Package(36, "2300 Parkway Blvd", "West Valley City", "UT", 84119, "EOD", 88, "Can only be on truck 2", "0", "At Hub", "0")
p37 = Package(37, "410 S State St", "Salt Lake City", "UT", 84111, "10:30AM", 2, "n/a", "0", "At Hub", "0")
p38 = Package(38, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", 9, "Can only be on truck 2", "0", "At Hub", "0")
p39 = Package(39, "2010 W 500 S", "Salt Lake City", "UT", 84104, "EOD", 9, "n/a", "0", "At Hub", "0")
p40 = Package(40, "380 W 2880 S", "Salt Lake City", "UT", 84115, "10:30AM", 45, "n/a", "0", "At Hub", "0")

#Create an instance of a hash map from my CreateHashTable class
hashMap = CreateHashMap()


#Insert all packages into the hashmap using the CreateHashTable insert method
hashMap.insert(1, p1)
hashMap.insert(2, p2)
hashMap.insert(3, p3)
hashMap.insert(4, p4)
hashMap.insert(5, p5)
hashMap.insert(6, p6)
hashMap.insert(7, p7)
hashMap.insert(8, p8)
hashMap.insert(9, p9)
hashMap.insert(10, p10)
hashMap.insert(11, p11)
hashMap.insert(12, p12)
hashMap.insert(13, p13)
hashMap.insert(14, p14)
hashMap.insert(15, p15)
hashMap.insert(16, p16)
hashMap.insert(17, p17)
hashMap.insert(18, p18)
hashMap.insert(19, p19)
hashMap.insert(20, p20)
hashMap.insert(21, p21)
hashMap.insert(22, p22)
hashMap.insert(23, p23)
hashMap.insert(24, p24)
hashMap.insert(25, p25)
hashMap.insert(26, p26)
hashMap.insert(27, p27)
hashMap.insert(28, p28)
hashMap.insert(29, p29)
hashMap.insert(30, p30)
hashMap.insert(31, p31)
hashMap.insert(32, p32)
hashMap.insert(33, p33)
hashMap.insert(34, p34)
hashMap.insert(35, p35)
hashMap.insert(36, p36)
hashMap.insert(37, p37)
hashMap.insert(38, p38)
hashMap.insert(39, p39)
hashMap.insert(40, p40)


#create the address lookup function
def address_lookup(string_address):
    if string_address in addressData:
        #takes an address string and returns an int of the address location in the address data table
        return int(addressData.index(string_address))


#create distance between function
def distance_between(address1, address2):
    #calls the address lookup function to get 2 ints of the address locations
    a1 = address_lookup(address1)
    a2 = address_lookup(address2)
    distance = distanceData[a1][a2]
    # finds the distance between address 1 and 2 and returns a float value
    if distance is None:
        #if distance returns None then address 1 and 2 are reversed because of how the distance data is in the table
        distance = distanceData[a2][a1]

    return float(distance)


#create a funtion to find smallest distance in the array of truck packages
#also returns next address and next ID
def min_distance_from(from_address, truck_packages):
    min = 20.5
    distance = 0
    next_address = None
    next_id = 0
    for package in truck_packages:
        #finds distance between truck from address and the package address
        pkg = hashMap.search(package)
        distance = distance_between(from_address, pkg.address)
        if distance < min:
            #finds the smallest distance to set as min distance
            min = distance
            next_address = pkg.address
            next_id = pkg.package_id
    return min, next_address, next_id


#function to calculate the truck return trip for the final distance total
def return_trip(truck):
    distance = 0
    if truck.address != "4001 South 700 East":
       distance = distance_between(truck.address, "4001 South 700 East")
       truck.address = "4001 South 700 East"
    truck.mileage += distance
    truck.time += datetime.timedelta(hours=distance / 18)


#funtion for nearest neighbor algorithim to deliver packages
def deliver_packages(truck):
    min = 90
    next_address = "4001 South 700 East"
    next_id = 0
    #updates the time the packages leaves the hub
    for packages in truck.packages:
        hashMap.search(packages).time_left_hub = truck.time
    while len(truck.packages) > 0:
        #loops through the packages on the truck to find the shortest distance to travel next
        min, next_address, next_id = min_distance_from(next_address, truck.packages)
        #updates truck address
        truck.address = next_address
        #removes package from truck upon delivery
        truck.packages.remove(next_id)
        #updates truck milage
        truck.mileage += min
        #updates truck time
        truck.time += datetime.timedelta(hours=min / 18)
        #updates each packages with the time it was delivered
        hashMap.search(next_id).delivery_time = truck.time
    return_trip(truck)
    #adds the return time to hub from last package delivered
    truck.return_time = truck.time


#manually load all 3 trucks with the notes from each package being met
truck1 = Truck(16, 18, [1, 2, 13, 14, 15, 16, 19, 20, 29, 30, 34, 40], 0, "4001 South 700 East", datetime.timedelta(hours=8), "0")


truck2 = Truck(16, 18, [3, 6, 18, 25, 26, 28, 31, 32, 33, 36, 37, 38], 0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5), "0")


truck3 = Truck(16, 18, [4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 27, 35, 39], 0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20), "0")


#put each truck through the deliverey algorithim
deliver_packages(truck1)
deliver_packages(truck2)
deliver_packages(truck3)


#User interface
class UserInterface:
    #Show total of all 3 trucks distance
    total_distance = truck1.mileage + truck2.mileage + truck3.mileage
    print("Total Distance Traveled:", total_distance, "miles.")
    text = input("please input the word 'time':")
    #start the loop by inputting in the word time
    if text == "time":
        try:
            #takes a specific time to see the status of all packages at that time
            time = input("please enter a time in the format hh:mm:ss")
            (h, m, s) = time.split(":")
            user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            print("|ID|", "|---Address---|", "|City|", "|State|", "|Zip|", "|Deadline|", "|Weight|", "|Package Note|", "|Departure Time|", "|Status|", "|Delivery Time|t")
            for package_id in range(1, 41):
                package = hashMap.search(package_id)
                #update package status based on the user time
                package.update_status(user_time)
                print(str(package))
        except ValueError:
            exit()
    else:
        exit()





