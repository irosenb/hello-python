from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import os
from pyairtable import Table


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/events')
def retrieve_events():
    events = Table(os.environ['AIRTABLE_API_KEY'], 'appkgFanuGmwzHgbv', 'tblipl9Nu1Q2ylZLs')
    print(events.all())
    return "hello world!"


if __name__ == '__main__':
    app.run(debug=True)
