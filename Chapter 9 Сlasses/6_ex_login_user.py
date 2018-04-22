class User():  # создаём класс
    def __init__(self, first_name, last_name, phone_number, date_of_birth):  # инициализируем атрибуты
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.login_attempts = 0  # количество попыток входа

    def describe_user(self):  # создаём метод вывода информации о пользователе
        print("Имя пользователя: " + self.first_name.title())
        print("Фамилия пользователя: " + self.last_name.title())
        print("Номер телефона пользователя: " + self.phone_number)
        print("Год рождения: " + self.date_of_birth)

    def greet_user(self):  # приветствие пользователя
        print("\nПриветствуем тебя " + self.first_name.title() + " в нашем сообществе!")

    def increment_login_attempts(self):  # увеличивает количество на 1
        self.login_attempts += 1

    def reset_login_attempts(self):  # сбрасывает количество попыток
        self.login_attempts = 0


user = User("Алексей", "Кочетов", "+79111381223", "1986")
user.describe_user()
print("\nКоличество попыток входа - " + str(user.login_attempts) + " раз(а).")
user.increment_login_attempts()
user.increment_login_attempts()
print("\nСпустя 1 день количество попыток входа - " + str(user.login_attempts) + " раз(а).")
user.reset_login_attempts()
print("\nВ новом году количество попыток входа - " + str(user.login_attempts) + " раз(а).")