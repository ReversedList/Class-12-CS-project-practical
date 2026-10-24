import os  # noqa: I001
from flask import Flask, render_template
import mysql.connector as ms

app = Flask(__name__)


@app.route("/")
def Greeting():
    return render_template("index.html")


@app.route("/sign_in")
def Sign_in():
    return render_template("sign_in.html")


def get_db_connection():
    return ms.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )


if __name__ == "__main__":
    app.run(debug=True)
