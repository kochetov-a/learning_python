class User():  # создаём класс
    def __init__(self, first_name, last_name, phone_number, date_of_birth):  # инициализируем атрибуты
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth

    def describe_user(self):  # создаём метод вывода информации о пользователе
        print("Имя пользователя: " + self.first_name.title())
        print("Фамилия пользователя: " + self.last_name.title())
        print("Номер телефона пользователя: " + self.phone_number)
        print("Год рождения: " + self.date_of_birth)

    def greet_user(self):
        print("\nПриветствуем тебя " + self.first_name.title() + " в нашем сообществе!")


class Privileges():  # самостоятельный класс
    def __init__(self, privileges="разрешено всё"):
        self.privileges = privileges

    def show_privileges(self):
        print("\nПривилегии данного сотрудника - " + self.privileges.title())


class Admin(User):  # создание класса наследника User
    def __init__(self, first_name, last_name, phone_number, date_of_birth):
        super().__init__(first_name, last_name, phone_number, date_of_birth)
        self.privileges = Privileges()  # новый экземпляр класса


user_1 = User("Алексей", "Кочетов", "+79111381223", "1986")
user_1.describe_user()
user_1.greet_user()

admin = Admin("Сергей", "Иванов", 911, 1985)
admin.privileges.show_privileges()