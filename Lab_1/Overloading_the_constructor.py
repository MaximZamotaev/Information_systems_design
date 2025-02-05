import re
import json

class Clients:
    def __init__(self, client_id, fullname, phone_number, email):
        # Инициализация полей через универсальный метод
        self.set_field("client_id", client_id, self.validate_client_id,
                        "Некорректный идентификатор клиента. Идентификатор должен быть положительным целым числом.")
        self.set_field("fullname", fullname, self.validate_fullname,
                        "Некорректное полное имя. Полное имя не может быть пустым.")
        self.set_field("phone_number", phone_number, self.validate_phone_number,
                        "Некорректный номер телефона. Должен быть строкой из цифр и, возможно, начинаться с '+'.")
        self.set_field("email", email, self.validate_email,
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
        return self.client_id

    def get_fullname(self):
        return self.fullname

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email

    # Сеттеры
    def set_client_id(self, client_id):
        self.set_field("client_id", client_id, self.validate_client_id,
                        "Некорректный идентификатор клиента. Идентификатор должен быть положительным целым числом.")

    def set_fullname(self, fullname):
        self.set_field("fullname", fullname, self.validate_fullname,
                        "Некорректное полное имя. Полное имя не может быть пустым.")

    def set_phone_number(self, phone_number):
        self.set_field("phone_number", phone_number, self.validate_phone_number,
                        "Некорректный номер телефона. Должен быть строкой из цифр и, возможно, начинаться с '+'.")

    def set_email(self, email):
        self.set_field("email", email, self.validate_email,
                        "Некорректный email. Проверьте формат: должен быть в виде 'что-то@что-то.домен'.")

    # Приватный метод для установки значения с валидацией
    def set_field(self, field_name, value, validator, error_message):
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

    def __str__(self):
        return f"Client{{client_id={self.client_id}, fullname='{self.fullname}', phone_number='{self.phone_number}', email='{self.email}'}}"

client1 = Client(client_id=1, fullname="Иван Иванов", phone_number="+79161234567", email="ivanov@example.com")
print(client1)

# Создание объекта Client с использованием перегрузки конструктора
json_data = '{"client_id": 2, "fullname": "Мария Смирнова", "phone_number": "+79161234568", "email": "smirnova@example.com"}'
client2 = Client.from_json(json_data)
print(client2)
