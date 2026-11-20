class Vehicle:
    def drive(self):
        return "Driving a vehicle"


# Car inherits from Vehicle
class Car(Vehicle):
    # Override: replace the parent's drive() with its own version
    def drive(self):
        return "Driving a car"


# Bicycle inherits from Vehicle
class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"


if __name__ == "__main__":
    v = Vehicle()
    c = Car()
    b = Bicycle()

    print(v.drive())
    print(c.drive())
    print(b.drive())
