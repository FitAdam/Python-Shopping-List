from flask import Blueprint, redirect, render_template, request, session, flash, url_for, current_app

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    user = {'username': 'Adam'}
    
    return render_template("home.html",title='Home', user=user)


@main.route("/orders")
def orders():
    return render_template('orders.html')
