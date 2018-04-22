class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restauran(self):
        print("\nНазвание ресторана - " + self.restaurant_name.title() + ".")
        print("Тип кухни в ресторане - " + self.cuisine_type.title() + ".")

    def open_restauran(self):
        print("Ресторан '" + self.restaurant_name.title() + "' сейчас открыт!")

    def set_number_served(self, served):
        self.number_served = served

    def increment_served(self, new_served):
        self.number_served += new_served



restaurant_1 = Restaurant('осака', 'японская')
restaurant_1.describe_restauran()
restaurant_1.open_restauran()
print("Количество обслуженных посетителей - " + str(restaurant_1.number_served))
restaurant_1.set_number_served(45)
print("Спустя 1 день количество обслуженных посетителей - " + str(restaurant_1.number_served))
restaurant_1.increment_served(23)
print("Спустя 2 дня количество обслуженных посетителей - " + str(restaurant_1.number_served))


restaurant_2 = Restaurant('ламантин', 'русская')
restaurant_2.describe_restauran()
restaurant_2.open_restauran()
print("Количество обслуженных посетителей - " + str(restaurant_2.number_served))


restaurant_3 = Restaurant('Содексо', 'хрень собачья')
restaurant_3.describe_restauran()
restaurant_3.open_restauran()
print("Количество обслуженных посетителей - " + str(restaurant_3.number_served))