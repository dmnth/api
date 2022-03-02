#! /usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, InputRequired, EqualTo
from datetime import datetime
from wtforms.widgets import PasswordInput, CheckboxInput, TextArea, Select
from wtforms.widgets.html5 import EmailInput
from app.main.models import User



