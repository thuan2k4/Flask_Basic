from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        new_user = User.query.filter_by(username = username_to_check.data).first()
        if new_user:
            raise ValidationError('Username already exists! Please try a different username')
    
    def validate_email_address(self, email_address_check):
        new_email_address = User.query.filter_by(email_address = email_address_check.data).first()
        if new_email_address:
            raise ValidationError('Email address already exists! Please try a different email address')
        
    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=3, max=30), DataRequired()])
    repeat_password = PasswordField(label='Repeat_password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')