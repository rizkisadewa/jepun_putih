# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
# from flask_debugtoolbar import DebugToolbarExtension
app = Flask('project')
app.config['SECRET_KEY'] = 'random'
app.debug = True
# toolbar = DebugToolbarExtension(app)
from project.controllers import *

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'myakar01'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
