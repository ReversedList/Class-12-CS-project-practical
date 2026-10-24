import mysql.connector as ms
from main_app import get_db_connection as connection_sql
from werkzeug.security import check_password_hash
from models import AuthenticationError


def Access_check(username_search, passwd_entry):
    conn = connection_sql()
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
