# file chứa các đường dẫn
from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from market import db, app
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market', methods=["GET","POST"])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object.price):
                p_item_object.owner = current_user.id
                current_user.budget -= p_item_object.price
                db.session.commit()
                flash(f'Congratulations! You purchased {p_item_object.name} for {p_item_object.price}', category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}", category='danger')
        return redirect(url_for('market_page'))
    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
    sell_form = SellItemForm()
    return render_template('market.html', items = items, purchase_form=purchase_form, sell_form=sell_form)

@app.route('/register', methods=["GET","POST"])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        
        user_to_create = User(username = form.username.data,
                                email_address = form.email_address.data,
                                password = form.password.data)

        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully ! You are now logged in as {user_to_create.username}", category='success')
        
        return redirect(url_for('market_page'))

    if form.errors != {}: # If there aren't errors from the validators
        for error_message in form.errors.values():
            flash(f'There was an error with creating a user: {error_message}', category='danger')
            
    return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Login successfully! Welcome {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('home_page'))