class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Название ресторана - " + self.restaurant_name.title() + ".")
        print("Тип кухни в ресторане - " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("Ресторан '" + self.restaurant_name.title() + "' сейчас открыт!")


class IceCreamStand(Restaurant):  # создание класса наследника Restaurant

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)  # наследование всех типов класса-родителя
        self.flavors = flavors  # новый атрибут

    def get_flavors(self):
        print("В этом ресторане есть следующие сорта мороженного: " + self.flavors)


ice_cream_stand = IceCreamStand("Братья Цыплята", "фаст-фуд", "нет никакого")
ice_cream_stand.get_flavors()