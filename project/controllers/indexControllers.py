# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request

@app.route('/')
def startIndex():
    return render_template('index/index.html')
