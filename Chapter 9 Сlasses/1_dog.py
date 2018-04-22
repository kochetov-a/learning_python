class Dog():

    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(self.name.title() + " сейчас сидит.")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(self.name.title() + " перекатывается!")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("Имя моей собаки - " + my_dog.name.title() + ".")
print("Возраст моей собаки - " + str(my_dog.age) + " лет.")
my_dog.sit()

print("Имя твоей собаки - " + your_dog.name.title() + ".")
print("Возраст твоей собаки - " + str(your_dog.age) + " лет.")
your_dog.roll_over()