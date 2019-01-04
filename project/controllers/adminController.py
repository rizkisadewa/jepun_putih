# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request

@app.route('/admin')
def adminIndex():
    return render_template('admin/adminIndex.html')
