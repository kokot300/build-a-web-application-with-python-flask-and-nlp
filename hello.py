#!/usr/bin/python3

from flask import Flask, escape, request, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def root():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/hello')
def hello():
    utc_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    return render_template("index.html", utc_time=utc_time)


if __name__ == '__main__':
    app.run(debug=True)

# env FLASK_APP=hello.py flask run
# http://127.0.0.1:5000/?name=yo
