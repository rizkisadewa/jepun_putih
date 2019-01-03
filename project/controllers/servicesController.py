from project import app
from flask import render_template, request

@app.route('/services')
def startServices():
    return render_template('client/services.html')
