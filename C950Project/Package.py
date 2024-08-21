#Creates a package class to store all package details
class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, weight, notes, time_left_hub, status, delivery_time):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.time_left_hub = time_left_hub
        self.status = status
        self.delivery_time = delivery_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state, self.zip,
                                                           self.deadline, self.weight, self.notes, self.time_left_hub,
                                                           self.status, self.delivery_time)


    def update_status(self, user_time):
        if self.delivery_time <= user_time:
            self.status = "Delivered"
        elif self.time_left_hub <= user_time <= self.delivery_time:
            self.status = "En route"
        else:
            self.status = "At Hub"
