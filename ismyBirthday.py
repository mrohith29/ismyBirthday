from flask import Flask, render_template
import datetime
from flask_frozen import Freezer

ismyBirthday = Flask(__name__)
freezer = Freezer(ismyBirthday)

@ismyBirthday.route('/')
def home():
    now = datetime.datetime.now()
    mybirthday = now.month == 11 and now.day == 29
    return render_template('index.html', mybirthday=mybirthday)

@ismyBirthday.route('/date')
def date():
    return render_template('date.html')

if __name__ == '__main__':
    ismyBirthday.run(debug=True)