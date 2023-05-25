class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
car=Car()
my_car = car("Toyota", "Prius")
print(my_car.make)