class Car:  # класс для описания автомобилей
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

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


class Battery:  # новый независимый класс для описания батареи
    def __init__(self, battery_size=75):
        self.battery_size = battery_size  # создание нового эксземпляра класса Battery

    def describe_battery(self):
        print("\nЭта машина имеет аккумулятор мощностью " + str(self.battery_size) + " КВТ.")

    def get_range(self):  # метод выводит приблизительный остаток хода для аккумулятора
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "Этот автомобиль может проехать " + str(range)
        message += " километров при полной зарядке."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        print("\nДобавили немного мощности!")


class ElectricCar(Car):  # новый класс наследюущий атрибуты класса Car
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # Инициализирует класса-родителя
        self.battery = Battery()


my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()