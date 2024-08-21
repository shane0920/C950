#Creates a truck class to use to deliver the packages
class Truck:
    def __init__(self, capacity, speed, packages, mileage, address, depart_time, return_time):
        self.capacity = capacity
        self.speed = speed
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time
        self.return_time = return_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.packages, self.mileage,
                                               self.address, self.depart_time, self.return_time)