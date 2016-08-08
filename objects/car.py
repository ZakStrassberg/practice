class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayAll()

    def displayAll(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax

car1 = Car(10000, "60mph", "Full", "35mpg")
car2 = Car(12000, "45mph", "Not Full", "23mpg")
car3 = Car(16000, "51mph", "Kind of Full", "33mpg")
car4 = Car(20000, "74mph", "Full", "24mpg")
car5 = Car(8000, "78mph", "Empty", "40mpg")
car6 = Car(220000, "69mph", "Empty", "25mpg")
