# -*- coding: utf-8 -*-
from project import app
from flask import render_template, flash, redirect, url_for, session, request, logging #stuff from Flask
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from project.models.adminModels import adminModel

# an object from Admin Models
adminModel = adminModel()

@app.route('/admin')
def adminDashboard():
    return render_template('/admin/adminIndex.html')

@app.route('/admin/login')
def adminLogin():
    return render_template('/admin/adminLogin.html')


class RegisterForm(Form):
    admin_name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')

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
