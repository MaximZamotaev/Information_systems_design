from Full_and_Short_version import Clients


class ClientsShort(Clients):
    def __init__(self, client_id, fullname, phone_number, email):
        super().__init__(client_id, fullname, phone_number, email)


# Пример использования
if __name__ == "__main__":
    print("Запуск кода в Inheritance_hierarchy.py:")
    client1 = ClientsShort(client_id=1, fullname="Иван Иванов", phone_number="+79161234567", email="ivanov@example.com")
    client2 = ClientsShort(client_id=2, fullname="Мария Смирнова", phone_number="+79161234568", email="smirnova@example.com")
    client3 = ClientsShort(client_id=1, fullname="Иван Иванов", phone_number="+79161234567", email="ivanov@example.com")

    print("Полная версия клиента 1:")
    print(client1)
    print("Краткая версия клиента 1:")
    print(client1.short_version())  # Наследуется из Clients

    print("\nСравнение объектов:")
    print(f"client1 == client2: {client1 == client2}")
    print(f"client1 == client3: {client1 == client3}")
