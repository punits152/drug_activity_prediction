from flask.templating import render_template
from app_package import app
from flask import render_template

# Homepage
@app.route("/")
@app.route("home")
def home_page():
    return render_template("home_page.html")