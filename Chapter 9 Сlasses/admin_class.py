from user_class import User


class Privileges:  # самостоятельный класс
    def __init__(self, privileges="разрешено всё"):
        self.privileges = privileges

    def show_privileges(self):
        print("\nПривилегии данного сотрудника - " + self.privileges.title())


class Admin(User):  # создание класса наследника User
    def __init__(self, first_name, last_name, phone_number, date_of_birth):
        super().__init__(first_name, last_name, phone_number, date_of_birth)
        self.privileges = Privileges()  # новый экземпляр класса
