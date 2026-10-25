import os

import mysql.connector as ms
from models import AuthenticationError
from werkzeug.security import check_password_hash


def get_db_connection():
    return ms.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )


def access_check(username_search, passwd_entry):
    conn = get_db_connection()
    cur_obj = conn.cursor()
    try:
        q1 = """
            SELECT password_hash
            FROM users
            WHERE username = %s
        """
        cur_obj.execute(q1, (username_search,))
        db_response = cur_obj.fetchone()
        if db_response and check_password_hash(db_response[0], passwd_entry):
            return True
        else:
            raise AuthenticationError("Invalid password or username")
    finally:
        cur_obj.close()
        conn.close()
