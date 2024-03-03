import datetime

from flask import Flask, render_template

ismyBirthday = Flask(__name__)

@ismyBirthday.route('/')

def index():
    now = datetime.datetime.now()
    mybirthday = now.month == 11 and now.day == 29
    return render_template('index.html', mybirthday=mybirthday)