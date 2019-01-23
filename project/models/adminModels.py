# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, flash, redirect, url_for, session, request, logging #stuff from Flask
from project import mysql
from passlib.hash import sha256_crypt

class adminModel(object):

        # Admin Register
    def registerAdmin(self, admin_name, email, username, password):
        # Create a cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO admins(name, email, username, password) VALUES(%s,%s,%s,%s)", (admin_name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()
