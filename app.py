from flask import Flask, render_template, url_for
from datetime import datetime

import os
from pyairtable import Table


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/events')
def retrieve_events():
    events = Table(os.environ['AIRTABLE_API_KEY'], 'appkgFanuGmwzHgbv', 'tblipl9Nu1Q2ylZLs')
    return render_template('index.html', events=events.all())

if __name__ == '__main__':
    app.run(debug=True)
