# -*- coding: utf-8 -*-
from flask import flash

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'myAkar01'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
