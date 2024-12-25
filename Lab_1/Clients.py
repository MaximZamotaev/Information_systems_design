class Clients:
    def __init__(self, client_id, fullname, phone_number, email):
        self.__client_id = client_id
        self.__fullname = fullname
        self.__phone_number = phone_number
        self.__email = email

    def get_client_id(self):
        return self.__client_id

    def set_client_id(self, client_id):
        self.__client_id = client_id

    def get_fullname(self):
        return self.__fullname

    def set_fullname(self, fullname):
        self.__fullname = fullname

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def __str__(self):
        return f"Client{{client_id={self.__client_id}, fullname='{self.__fullname}', phone_number='{self.__phone_number}', email='{self.__email}'}}"
      
