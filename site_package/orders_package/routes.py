from flask import Blueprint, redirect, render_template, request, session, flash, url_for, current_app
from site_package.orders_package.forms import RegistrationForm
from site_package.orders_package.emails import email_form


order = Blueprint('order', __name__)



@order.route("/add_order", methods=["GET", "POST"])
def add_order():
    form = RegistrationForm()
    if form.validate_on_submit():
        """
        ord = order(name=form.name.data, category = form.category.data)
        db.session.add(ord)
        db.session.commit()
        """
        email_form().send_emails()
        return redirect(url_for('main.confirm'))
    return render_template('add_order.html', title='Add order', form=form)
 