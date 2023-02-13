from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap5

#resource: https://hackersandslackers.com/flask-wtforms-forms/
#https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields
#https://wtforms.readthedocs.io/en/2.3.x/crash_course/#validators
#https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
#https://bootstrap-flask.readthedocs.io/en/stable/migrate/#create-base-template

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[InputRequired("Please enter your email address."), Email("This field requires a valid email address.")])
    password = PasswordField(label='Password', validators=[InputRequired("Please enter your password."), Length(min=8)])
    submit = SubmitField(label='Log In')

app = Flask(__name__)

app.secret_key = "secret_rent"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)

