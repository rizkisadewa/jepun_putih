# -*- coding: utf-8 -*-
from project import app
from flask import render_template, flash, redirect, url_for, session, request, logging #stuff from Flask
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from project.models.adminModels import adminModel

# an object from Admin Models
adminModel = adminModel()

# go to Admin Dashboard
@app.route('/admin/dashboard')
def adminDashboard():
    return render_template('/admin/adminIndex.html')


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

        # implemntation of function Admin Register
        adminModel.insertAdmin(admin_name, email, username, password)

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

        if adminModel.getAdminLogin(username,password_candidate) == 1:
            redirect(url_for('adminDashboard'))

    return render_template('admin/adminLogin.html')
