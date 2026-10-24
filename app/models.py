# This file contains the user models and other models this app might use
# NOTE: this is only the models the database side of this done in the file user_db_repo.py
# NOTE: DO NOT STORE THE PASSWORD AFTER IT IS WROTE INTO THE DATABASE! DO NOT LET IT LEAK TO LOGS!


import re

from werkzeug.security import check_password_hash, generate_password_hash


class User:
    def __init__(self, username: str, age: int, password, user_id: int | None = None):
        self.user_id = user_id
        self.name = username
        self.age = age
        self._password = password

    def pass_create(pass_wd):
        password_rule = re.compile(r"^\S{8,30}$")
        if password_rule.fullmatch(pass_wd):
            hashed_password = generate_password_hash(pass_wd)
        else:
            msg_warning = "Incorrect form of password"
            raise ValueError(msg_warning)

        return hashed_password

    def name_validity(name_user):
        username_rule = re.compile(r"[A-Za-z0-9_]{3,30}")
        if username_rule.fullmatch(name_user):
            return name_user
        else:
            msg_warning = "Invalid name, keep names between 3-30 and should not contain special char other than '_'"
            raise ValueError(msg_warning)

    def age_valdity(age_user):
        if 3 <= age_user <= 120:
            return age_user
        else:
            msg_warning = "Invalid age (users under age 3 is not permitted and age above 120 is not permitted,if you by any chance is above 120 congrats on a long life please contanct customer service)"
            raise ValueError(msg_warning)


class AuthenticationError(Exception):
    pass
