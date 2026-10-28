#TODO: make a dashboard html file and change fill_it to that respective file name (do it pls)

from flask import Flask, render_template, request
from auth import login_to_acc

app = Flask(__name__)


@app.route("/")
def Greeting():
    return render_template("index.html")


@app.route("/sign_in")
def Sign_in():
    return render_template("sign_in.html")

@app.route("/login",methods=["POST"])
def Login():
    username = request.form["username"]
    password = request.form["password"]

    if login_to_acc(username,password):
        return render_template("fill_it.html")
    
    return render_template("login_in.html")
    


if __name__ == "__main__":
    app.run(debug=True)
