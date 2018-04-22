from car_class import Car  # импортируем класс Car из отдельного файла car_class.py

my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()