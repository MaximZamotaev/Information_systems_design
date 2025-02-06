class Clients:
    def __init__(self, client_id, fullname, phone_number, email):
        self._client_id = client_id
        self._fullname = fullname
        self._phone_number = phone_number
        self._email = email

    def get_client_id(self):
        return self._client_id

    def set_client_id(self, client_id):
        self._client_id = client_id

    def get_fullname(self):
        return self._fullname

    def set_fullname(self, fullname):
        self._fullname = fullname

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def __str__(self):
        return f"Client{{client_id={self._client_id}, fullname='{self._fullname}', phone_number='{self._phone_number}', email='{self._email}'}}"
      
