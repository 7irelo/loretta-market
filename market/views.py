from market import app
from flask import render_template
from market.models import Product, User

    
@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")

@app.route("/market")
def market_page():
    products = Product.query.all()
    users = User.query.all()
    return render_template("market.html", products=products, users=users)

@app.route("/login")
def login_page(request):
    return render_template("login_register.html")

@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")