from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class LoginForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=4, max=16)])
  password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=128)])
  login = SubmitField("Login")

class RegisterForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=4, max=16)])
  password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=128)])
  confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=8, max=128), EqualTo("password")])
  register = SubmitField("Sign Up")