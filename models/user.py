#!/use/bin/python3
""" user module"""


from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from BaseModel

    Attributes:
        email: email.
        password: password
        first_name: first name.
        last_name: last name.
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
