import re
import json

class ClientsShort:
    def __init__(self, client_id, fullname):
        # Инициализация только краткой версии данных через универсальный метод
        self._set_field("_client_id", client_id, self.validate_client_id,
                        "Некорректный идентификатор клиента. Идентификатор должен быть положительным целым числом.")
        self._set_field("_fullname", fullname, self.validate_fullname,
                        "Некорректное полное имя. Полное имя не может быть пустым.")

    # Классовый метод для создания объекта из JSON
    @classmethod
    def from_json(cls, data_json):
        try:
            data = json.loads(data_json)
            return cls(
                client_id=data["client_id"],
                fullname=data["fullname"]
            )
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError("Некорректные данные JSON.")

    # Геттеры
    def get_client_id(self):
        return self._client_id

    def get_fullname(self):
        return self._fullname

    # Сеттеры
    def set_client_id(self, client_id):
        self._set_field("_client_id", client_id, self.validate_client_id,
                        "Некорректный идентификатор клиента. Идентификатор должен быть положительным целым числом.")

    def set_fullname(self, fullname):
        self._set_field("_fullname", fullname, self.validate_fullname,
                        "Некорректное полное имя. Полное имя не может быть пустым.")

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

    # Полная версия объекта
    def __str__(self):
        return f"Client{{client_id={self._client_id}, fullname='{self._fullname}'}}"

    # Краткая версия объекта
    def short_version(self):
        return f"Client{{client_id={self._client_id}}}"

    # Метод __eq__ для сравнения объектов
    def __eq__(self, other):
        if not isinstance(other, ClientsShort):
            return False
        return self._client_id == other._client_id

# Пример использования
client1 = ClientsShort(client_id=1, fullname="Иван Иванов")
client2 = ClientsShort(client_id=2, fullname="Мария Смирнова")
client3 = ClientsShort(client_id=1, fullname="Иван Иванов")

print("Полная версия клиента 1:")
print(client1)
print("Краткая версия клиента 1:")
print(client1.short_version())

print("\nСравнение объектов:")
print(f"client1 == client2: {client1 == client2}")
print(f"client1 == client3: {client1 == client3}")
