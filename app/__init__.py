#! /usr/bin/env python3

import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.main import routes, models
