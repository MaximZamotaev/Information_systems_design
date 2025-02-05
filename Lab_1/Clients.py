class Clients:
    def __init__(self, client_id, fullname, phone_number, email):
        self.client_id = client_id
        self.fullname = fullname
        self.phone_number = phone_number
        self.email = email

    def get_client_id(self):
        return self.client_id

    def set_client_id(self, client_id):
        self.client_id = client_id

    def get_fullname(self):
        return self.fullname

    def set_fullname(self, fullname):
        self.fullname = fullname

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def __str__(self):
        return f"Client{{client_id={self.client_id}, fullname='{self.fullname}', phone_number='{self.phone_number}', email='{self.email}'}}"
      
