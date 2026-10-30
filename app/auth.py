# This file is where the log in function lives
from main_app import Login
from user_db_repo import access_check


def login_to_acc():
    username_entered,password_entered = Login()
    login_status = access_check(username_entered,password_entered)
    if login_status :
        pass
    if not login_status:
        pass