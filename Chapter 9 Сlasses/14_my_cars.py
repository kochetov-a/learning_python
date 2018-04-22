from car_class import Car, ElectricCar  # импортировани нескольких определенных классов из одного модуля

"""from car - импортирование всего модуля"""
"""from car import * - импортирование всех классов из модуля"""

my_beetle = Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "roadstep", 2018)
print(my_tesla.get_descriptive_name())