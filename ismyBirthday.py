import datetime

from flask import Flask, render_template

ismyBirthday = Flask(__name__)

@ismyBirthday.route('/')

def index():
    now = datetime.datetime.now()
    mybirthday = now.month == 11 and now.day == 29
    return render_template('index.html', mybirthday=mybirthday)

@ismyBirthday.route('/date')

def date():
    return render_template('date.html')

@ismyBirthday.route('/')
def home():
    return render_template('index.html')

from flask_frozen import Freezer

freezer = Freezer(ismyBirthday)

if __name__ == '__main__':
    freezer.freeze()