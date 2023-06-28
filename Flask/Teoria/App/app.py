from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
app.config.from_pyfile("config.py")

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

@app.route("/use1r/<name>")
def user1(name):
    return "<h1>Bye, {}!</h1>".format(name)