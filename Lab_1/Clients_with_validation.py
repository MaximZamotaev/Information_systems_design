class Client:
    def __init__(self, client_id, fullname, phone_number, email):
        # Валидируем поля при создании объекта
        if not self.validate_client_id(client_id):
            raise ValueError("Некорректный идентификатор клиента. Идентификатор должен быть положительным целым числом.")
        if not self.validate_fullname(fullname):
            raise ValueError("Некорректное полное имя. Полное имя не может быть пустым.")
        if not self.validate_phone_number(phone_number):
            raise ValueError("Некорректный номер телефона. Должен быть строкой из цифр и, возможно, начинаться с '+'.")
        if not self.validate_email(email):
            raise ValueError("Некорректный email. Проверьте формат: должен быть в виде 'что-то@что-то.домен'.")

        self._client_id = client_id
        self._fullname = fullname
        self._phone_number = phone_number
        self._email = email

    # Геттеры и сеттеры с валидацией

    def get_client_id(self):
        return self._client_id

    def set_client_id(self, client_id):
        if not self.validate_client_id(client_id):
            raise ValueError("Некорректный идентификатор клиента. Идентификатор должен быть положительным целым числом.")
        self._client_id = client_id

    def get_fullname(self):
        return self._fullname

    def set_fullname(self, fullname):
        if not self.validate_fullname(fullname):
            raise ValueError("Некорректное полное имя. Полное имя не может быть пустым.")
        self._fullname = fullname

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        if not self.validate_phone_number(phone_number):
            raise ValueError("Некорректный номер телефона. Должен быть строкой из цифр и, возможно, начинаться с '+'.")
        self._phone_number = phone_number

    def get_email(self):
        return self._email

    def set_email(self, email):
        if not self.validate_email(email):
            raise ValueError("Некорректный email. Проверьте формат: должен быть в виде 'что-то@что-то.домен'.")
        self._email = email

    # Статические методы для валидации
    @staticmethod
    def validate_client_id(client_id):
        return isinstance(client_id, int) and client_id > 0

    @staticmethod
    def validate_fullname(fullname):
        return isinstance(fullname, str) and len(fullname.strip()) > 0

    @staticmethod
    def validate_phone_number(phone_number):
        # Простая проверка: строка длиной 10-15 символов, только цифры и знак "+"
        import re
        return isinstance(phone_number, str) and re.fullmatch(r'\+?\d{10,15}', phone_number) is not None

    @staticmethod
    def validate_email(email):
        # Простая проверка: формат "что-то@что-то.домен"
        import re
        return isinstance(email, str) and re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email) is not None

    def __str__(self):
        return f"Client{{client_id={self._client_id}, fullname='{self._fullname}', phone_number='{self._phone_number}', email='{self._email}'}}"
