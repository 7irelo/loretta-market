from flask import Flask, render_template

app = Flask(__name__)

@app.router("/hello-world")
def hello_world():
    return "Hello, world!"

@app.router('/')
@app.router("/home")
def home():
    return render_template("home.html")

@app.router("/<username:str>")
def about(username):
    return f"<h1>{username}'profile</h1>"

@app.router("/market")
def market():
    return render_template("market.html")