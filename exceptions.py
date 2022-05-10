# exceptions.py

class UserException(Exception):
    ...


class UserNotFoundError(UserException):
    def __init__(self):
        self.status_code = 404
        self.detail = "User Not Found"


class UserAlreadyExistError(UserException):
    def __init__(self):
        self.status_code = 409
        self.detail = "User Already Exists"
