from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from webApplication.models import User

class RegisterForm(FlaskForm):
    
    def validate_username(self, name):
        new_user = User.query.filter_by(username = name.data).first()
        if new_user:
            raise ValidationError(f'Username already exists!')
    
    def validate_email_address(self, email):
        new_email = User.query.filter_by(email = email.data).first()
        if new_email:
            raise ValidationError(f'Someone is already registered with the email entered!')
    
    username = StringField(label='User Name:', validators=[DataRequired(), Length(3,10)])
    email_address = StringField(label='Email Address:', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password:', validators=[DataRequired(), Length(6)])
    confirm_pass = PasswordField(label='Confirm Password:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Create Account')
    