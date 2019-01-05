# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request

@app.route('/admin')
def adminDashboard():
    return render_template('admin/adminIndex.html')

@app.route('/admin/login')
def adminLoginForm():
    return render_template('admin/adminLogin.html')
