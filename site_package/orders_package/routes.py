from flask import Blueprint, redirect, render_template, request, session, flash, url_for, current_app
from site_package.orders_package.forms import RegistrationForm
from site_package.orders_package.emails import email_form
import sqlite3

order = Blueprint('order', __name__)



@order.route("/add_order", methods=["GET", "POST"])
def add_order():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create a database connection
        conn = sqlite3.connect('order.db')
        # Create a cursor
        cursor = conn.cursor()

        cursor.execute("INSERT INTO orders VALUES ('bacon', 'meet', '12')")
        #ord = new(name = form.name.data, category = form.category.data, quantity = form.quantity.data)
        
        # Commit our command
        conn.commit()

        # Close our connection
        conn.close()
        print("command executed")
        
        #email_form().send_emails()
        return redirect(url_for('main.orders'))
    return render_template('add_order.html', title='Add order', form=form)
 