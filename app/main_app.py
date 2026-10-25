from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Greeting():
    return render_template("index.html")


@app.route("/sign_in")
def Sign_in():
    return render_template("sign_in.html")

if __name__ == "__main__":
    app.run(debug=True)
