# file chứa các đường dẫn
from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db, app
from flask_login import login_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items = items)

@app.route('/register', methods=["GET","POST"])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        
        user_to_create = User(username = form.username.data,
                                email_address = form.email_address.data,
                                password = form.password.data)

        db.session.add(user_to_create)
        db.session.commit()
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