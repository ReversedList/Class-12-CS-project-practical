# This file contains the user models and other models this app might use
# NOTE: this is only the models the database side of this done in the file user_db_repo.py
# NOTE: DO NOT STORE THE PASSWORD AFTER IT IS WROTE INTO THE DATABASE! DO NOT LET IT LEAK TO LOGS!


import re

from werkzeug.security import generate_password_hash

PASSWORD_RULE = re.compile(r"\S{8,50}")
USERNAME_RULE = re.compile(r"[A-Za-z0-9_]{3,30}")


class User:
    def __init__(
        self, username: str, age: int, password_hash, user_id: int | None = None
    ):
        self.user_id = user_id
        self.username = username
        self.age = age
        self.password_hash = password_hash

    @staticmethod
    def password_validity(pass_wd):
        error_msg = "Password must be 8 - 50 character ,no spaces."
        if pass_wd is None:
            raise ValueError(error_msg)

        if not isinstance(pass_wd, str):
            raise TypeError(error_msg)

        if PASSWORD_RULE.fullmatch(pass_wd):
            return pass_wd
        raise ValueError(error_msg)

    @staticmethod
    def name_validity(name_user):
        if name_user is None:
            raise ValueError("pls enter name")

        if not isinstance(name_user, str):
            raise TypeError("name must be text")

        if USERNAME_RULE.fullmatch(name_user):
            return name_user

        msg_warning = "Invalid name, keep names between 3-30 and should not contain special char other than '_'"
        raise ValueError(msg_warning)

    @staticmethod
    def age_validity(age_user):
        try:
            age = int(age_user)
        except (ValueError, TypeError):
            raise ValueError("Invalid age input (must be a whole number)") from None

        if 3 <= age <= 120:
            return age
        raise ValueError(
            "Invalid age (under 3 or above 120 is not permitted. "
            "If you are above 120, congrats on a long life, please contact customer service)"
        )

    @staticmethod
    def hash_password(password_plain):
        hashed_password = generate_password_hash(password_plain)
        return hashed_password

    @classmethod
    def create_user(
        cls, username: str, age: int, password
    ) -> "User":  # this function creates the User object with the help of the class
        valid_username = cls.name_validity(username)
        valid_age = cls.age_validity(age)
        valid_password = cls.password_validity(password)
        valid_hash = cls.hash_password(valid_password)

        return cls(valid_username, valid_age, valid_hash)


class AuthenticationError(Exception):
    pass

class UsernameTakenError(Exception):
    pass