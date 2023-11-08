from flask import Flask, redirect, render_template, request, url_for
from config import config
app = Flask(__name__)
@app.route("/")
def index():
    return redirect("login")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        _user = request.form["username"]
        _pass = request.form["password"]
        print(_user)
        print(_pass)
        if _user == "admin" and _pass == "123":
            return redirect(url_for("home"))
        else:
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()