from flask import Flask, render_template
app = Flask(__name__)
app.config["SECRET_KEY"]='c30bdf3e315acd9bc3aa14ff'

from app_package import routes

if __name__=="__main__":
    app.run(debug=1,host="0.0.0.0",port=5000)