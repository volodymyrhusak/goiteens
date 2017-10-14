# -*- coding:utf-8 -*-
from flask import Flask , request, render_template, redirect , url_for , session
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('my_db')
curs = conn.cursor()

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        passw = request.form['passw']
        curs.execute('select 1 from users where user_name = {} and passw = {}'.format(user_name,passw))
        data = curs.fetchone()
        if data:
            session['username'] = user_name
            return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)