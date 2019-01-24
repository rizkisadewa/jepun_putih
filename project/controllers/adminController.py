# -*- coding: utf-8 -*-
from project import app
from flask import render_template, flash, redirect, url_for, session, request, logging #stuff from Flask
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from project import mysql
from passlib.hash import sha256_crypt
from functools import wraps

#import from Model
from project.models.adminModels import adminModel

# an object from Admin Models
adminModel = adminModel()


#import from Admin Validation
from project.controllers.adminValidations import adminValidation
adminValidation = adminValidation()


# Register Class
class RegisterForm(Form):
    admin_name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')

# Register for Admin
@app.route('/admin/register', methods=['GET', 'POST'])
def adminRegister():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        admin_name = form.admin_name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # implemntation of function Admin Register from Admin Model
        adminModel.registerAdmin(admin_name, email, username, password)

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('adminLogin'))

    return render_template('admin/adminRegister.html', form=form)

# Login Admin
@app.route('/admin/login', methods=['GET', 'POST'])
def adminLogin():
    if request.method == 'POST':
        #Get form fields
        username = request.form['username']
        password_candidate = request.form['password']
        url = url_for('adminDashboard')

        adminValidation.adminLogin(username, password_candidate, url)
    return render_template('admin/adminLogin.html')

# Checking Login Status
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, please login', 'danger')
            return redirect(url_for('adminLogin'))
    return wrap

# go to Admin Dashboard
@app.route('/admin/dashboard')
@is_logged_in
def adminDashboard():
    return render_template('/admin/adminIndex.html')
