from flask import Flask
from flask import render_template, redirect, request
from hero import Hero

app = Flask(__name__)
app.secret_key = "Sensei, oh Sensei, please give me guidance!"


@app.route("/")
def index():
    return render_template("index.html")


@app.post("/create_hero")
def create_hero():
    Hero.save(request.form)
    return redirect("/all_heroes")


@app.route("/all_heroes")
def all_heroes():
    return render_template("all_heroes.html", all_heroes=Hero.get_all())


if __name__ == "__main__":
    app.run(debug=True)
