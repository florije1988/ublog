# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask.ext.wtf import Form
from wtforms.fields import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email
from models import User


class ContactForm(Form):
    name = StringField("Name", [DataRequired("Please enter your name.")])
    email = StringField("Email", [DataRequired("Please enter your email address."),
                                  Email("Please enter your email address.")])
    subject = StringField("Subject", [DataRequired("Please enter a subject.")])
    message = TextAreaField("Message", [DataRequired("Please enter a message.")])
    submit = SubmitField("Send")


class SignupForm(Form):
    firstname = StringField("First name", [DataRequired("Please enter your first name.")])
    lastname = StringField("Last name", [DataRequired("Please enter your last name.")])
    email = StringField("Email", [DataRequired("Please enter your email address."),
                                  Email("Please enter your email address.")])
    password = PasswordField('Password', [DataRequired("Please enter a password.")])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True


class SigninForm(Form):
    email = StringField("Email", [DataRequired("Please enter your email address."),
                                  Email("Please enter your email address.")])
    password = PasswordField('Password', [DataRequired("Please enter a password.")])
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid e-mail or password")
            return False
