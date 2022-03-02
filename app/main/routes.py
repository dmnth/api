#! /usr/bin/env python3

from app import app
from .. import db
from flask import render_template, url_for, redirect, session, request
from flask_login import current_user, login_user, logout_user, login_required
# from app.main.forms import someforms

@app.route('/', methods=['POST', 'GET'])
def page_one():
    return render_template('page_one.html')

