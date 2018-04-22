class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Название ресторана - " + self.restaurant_name.title() + ".")
        print("Тип кухни в ресторане - " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("Ресторан '" + self.restaurant_name.title() + "' сейчас открыт!")