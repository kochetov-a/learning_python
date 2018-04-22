class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("Пробег этой машины " + str(self.odometer_reading) + " километра(ов).")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Нельзя уменьшать значение пробега!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(2000)
my_new_car.read_odometer()

my_new_car.increment_odometer(222)
my_new_car.read_odometer()