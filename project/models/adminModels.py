# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, flash, redirect, url_for, session, request, logging #stuff from Flask
from project import mysql
from passlib.hash import sha256_crypt

class adminModel(object):

        # Admin Register
    def insertAdmin(self, admin_name, email, username, password):
        # Create a cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO admins(name, email, username, password) VALUES(%s,%s,%s,%s)", (admin_name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

    # Admin Login
    def getAdminLogin(self, username, password_candidate):

        # Create cursor
        cur = mysql.connection.cursor()

        #Get user by Username
        result = cur.execute("SELECT * FROM admins WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Password
            if sha256_crypt.verify(password_candidate, password):
                # app.logger.info("PASSWORD MATCHED")
                session['logged_in'] = True
                session['username'] = username

                return 1
            else:
                print("Password not correct")
                return render_template('admin/adminLogin.html')
            # close the connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('admin/adminLogin.html', error=error)
