import re
import json


class Client:
    def __init__(self, client_id, fullname, phone_number, email):
        # Инициализация полей через универсальный метод
        self._set_field("_client_id", client_id, self.validate_client_id,
                        "Некорректный идентификатор клиента. Идентификатор должен быть положительным целым числом.")
        self._set_field("_fullname", fullname, self.validate_fullname,
                        "Некорректное полное имя. Полное имя не может быть пустым.")
        self._set_field("_phone_number", phone_number, self.validate_phone_number,
                        "Некорректный номер телефона. Должен быть строкой из цифр и, возможно, начинаться с '+'.")
        self._set_field("_email", email, self.validate_email,
                        "Некорректный email. Проверьте формат: должен быть в виде 'что-то@что-то.домен'.")

    # Классовый метод для создания объекта из JSON
    @classmethod
    def from_json(cls, data_json):
        try:
            data = json.loads(data_json)
            return cls(
                client_id=data["client_id"],
                fullname=data["fullname"],
                phone_number=data["phone_number"],
                email=data["email"]
            )
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError("Некорректные данные JSON.")

    # Геттеры
    def get_client_id(self):
        return self._client_id

    def get_fullname(self):
        return self._fullname

    def get_phone_number(self):
        return self._phone_number

    def get_email(self):
        return self._email

    # Сеттеры
    def set_client_id(self, client_id):
        self._set_field("_client_id", client_id, self.validate_client_id,
                        "Некорректный идентификатор клиента. Идентификатор должен быть положительным целым числом.")

    def set_fullname(self, fullname):
        self._set_field("_fullname", fullname, self.validate_fullname,
                        "Некорректное полное имя. Полное имя не может быть пустым.")

    def set_phone_number(self, phone_number):
        self._set_field("_phone_number", phone_number, self.validate_phone_number,
                        "Некорректный номер телефона. Должен быть строкой из цифр и, возможно, начинаться с '+'.")

    def set_email(self, email):
        self._set_field("_email", email, self.validate_email,
                        "Некорректный email. Проверьте формат: должен быть в виде 'что-то@что-то.домен'.")

    # Приватный метод для установки значения с валидацией
    def _set_field(self, field_name, value, validator, error_message):
        if not validator(value):
            raise ValueError(error_message)
        setattr(self, field_name, value)

    # Статические методы для валидации
    @staticmethod
    def validate_client_id(client_id):
        return isinstance(client_id, int) and client_id > 0

    @staticmethod
    def validate_fullname(fullname):
        return isinstance(fullname, str) and len(fullname.strip()) > 0

    @staticmethod
    def validate_phone_number(phone_number):
        return isinstance(phone_number, str) and re.fullmatch(r'\+?\d{10,15}', phone_number) is not None

    @staticmethod
    def validate_email(email):
        return isinstance(email, str) and re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email) is not None

    # Полная версия объекта
    def __str__(self):
        return f"Client{{client_id={self._client_id}, fullname='{self._fullname}', phone_number='{self._phone_number}', email='{self._email}'}}"

    # Краткая версия объекта
    def short_version(self):
        return f"Client{{client_id={self._client_id}, fullname='{self._fullname}'}}"

    # Метод __eq__ для сравнения объектов
    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return self._client_id == other._client_id and self._fullname == other._fullname


# Пример использования
client1 = Client(client_id=1, fullname="Иван Иванов", phone_number="+79161234567", email="ivanov@example.com")
client2 = Client(client_id=2, fullname="Мария Смирнова", phone_number="+79161234568", email="smirnova@example.com")
client3 = Client(client_id=1, fullname="Иван Иванов", phone_number="+79161234567", email="ivanov@example.com")

print("Полная версия клиента 1:")
print(client1)
print("Краткая версия клиента 1:")
print(client1.short_version())

print("\nСравнение объектов:")
print(f"client1 == client2: {client1 == client2}")
print(f"client1 == client3: {client1 == client3}")
