from flask import Blueprint, redirect, render_template, request, session, flash, url_for, current_app

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")


@main.route("/some")
def confirm():
    return render_template('some.html')
