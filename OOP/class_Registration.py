from string import digits, ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def is_include_digit(value):
        for digit in digits:
            if digit in value:
                return True
        return False

    @staticmethod
    def is_include_all_register(value):
        if value.islower() or value.isupper():
            return False
        return True

    @staticmethod
    def is_include_only_latin(value):
        for symbol in value:
            if not (symbol not in digits and symbol in ascii_letters):
                return False
        return True

    @staticmethod
    def check_password_dictionary(value):
        with open('easy_passwords.txt') as file:
            if value in map(lambda x: x.rstrip(), file.readlines()):
                return True
            return False

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if not isinstance(login, str):
            raise TypeError('Логин может быть только типа string')
        if '@' not in login:
            raise ValueError("Login must include at least one ' @ '")
        if '.' not in login:
            raise ValueError("Login must include at least one ' . '")
        self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        if not 5 <= len(password) <= 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(password):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        if not Registration.is_include_all_register(password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(password):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = password

