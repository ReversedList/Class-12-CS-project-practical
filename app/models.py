import re
from typing import Optional







class User:
    def __init__(self, user_id :int,name : str, age: int, password):
        self.user_id = user_id
        self.name = name
        self.age = age
        self._password = password
