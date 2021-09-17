from flask import Flask, render_template
app = Flask(__name__)
app.config["SECRET_KEY"]='c30bdf3e315acd9bc3aa14ff'

from app_package import routes
