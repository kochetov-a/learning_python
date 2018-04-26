from random import randint


class Die:

    def __init__(self, sides=6):  # один атрибут с значением 6
        self.sides = sides

    def roll_die(self):
        random = randint(1, self.sides)  # получаем случаное число от 1 до значения атрибута класса
        print("\nВыпало случайное число: " + str(random))


chance = Die(10)
chance.roll_die()
chance.roll_die()
chance.roll_die()
chance.roll_die()
chance.roll_die()
chance.roll_die()
chance.roll_die()
chance.roll_die()
chance.roll_die()
chance.roll_die()


