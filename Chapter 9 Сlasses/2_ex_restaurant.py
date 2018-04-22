class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restauran(self):
        print("Название ресторана - " + self.restaurant_name.title() + ".")
        print("Тип кухни в ресторане - " + self.cuisine_type.title() + ".")

    def open_restauran(self):
        print("Ресторан '" + self.restaurant_name.title() + "' сейчас открыт!")


restaurant_1 = Restaurant('осака', 'японская')
restaurant_1.describe_restauran()
restaurant_1.open_restauran()

restaurant_2 = Restaurant('ламантин', 'русская')
restaurant_2.describe_restauran()
restaurant_2.open_restauran()

restaurant_3 = Restaurant('Содексо', 'хрень собачья')
restaurant_3.describe_restauran()
restaurant_3.open_restauran()