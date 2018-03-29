from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    firstName = StringField("First Name", validators=[InputRequired(message="Please enter your first name")], description="First Name...")
    lastName = StringField("Last Name", description="Last Name")
    email = StringField("Email", validators=[InputRequired(message="Please enter your email"), Email()], description="Email...")
    username = StringField("Username", validators=[InputRequired(message="Please choose an awesome username"), Length(min=6, max=15)], description="Username...")
    pword = PasswordField("Password", validators=[InputRequired("You need a password"), Length(min=8, max=80)], description="Password...")
    pword1 = PasswordField("Reenter Password", validators=[InputRequired("You must reenter your password"), EqualTo(pword, message="Your Passwords must be identical")], description="Reenter Password")

class LoginForm(FlaskForm):
    uname = StringField("Username", validators=[InputRequired(message="Please enter your username")], description="Username...")
    pword = PasswordField("Password", validators=[InputRequired(message="Please enter your password")], description="Password")

