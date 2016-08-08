class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print "Price:", self.price, "Max speed:", self.max_speed, \
            "Miles:", self.miles

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(150, "22mph")
bike3 = Bike(225, "18mph")

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()
