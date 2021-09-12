from flask.templating import render_template
from app_package import app
from flask import render_template

# Homepage
@app.route("/")
@app.route("home")
def home_page():
    return render_template("home_page.html")

@app.route("/training")
def training_page():
    return render_template("train_page.html")

@app.route("/prediction")
def prediction_page():
    return render_template("predict_page.html")