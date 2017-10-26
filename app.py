# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for, session
from models.executeSqlite3 import executeSelectOne, executeSelectAll, executeSQL
from functools import wraps
from models.model_manager import UserManager
import os

# створюємо головний об'єкт сайту класу Flask
app = Flask(__name__)
# добавляємо секретний ключ для сайту щоб шифрувати дані сессії
# при кожнаму сапуску фласку буде генечитись новий рандомний ключ з 24 символів
app.secret_key = os.urandom(24)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


# описуємо логін роут
# вказуємо що доступні методи "GET" і "POST"
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        # якщо метод пост дістаємо дані з форми і звіряємо чи є такий користвач в базі данних
        # якшо є то в дану сесію добавляєм ключ username
        # і перекидаємо користувача на домашню сторінку
        email = request.form.get('email', '')
        passw = request.form.get('passw', '')
        sql = 'select name from users where email = "{}" and passw = "{}"'.format(email, passw)
        name = executeSelectOne(sql)[0]
        if name:
            addToSession(name)
            return redirect(url_for('home'))

    return render_template('login.html')



# описуємо роут для вилогінення
# сіда зможуть попадати тільки GET запроси
@app.route('/logout')
@login_required
def logout():
    user = session.get('username', None)
    if user:
        # якщо в сесії є username тоді видаляємо його
        del session['username']
    return redirect(url_for('login'))



# описуємо домашній роут
# сіда зможуть попадати тільки GET запроси
@app.route('/')
@login_required
def home():
    user = session.get('username', None)
    context = {}
    if user:
        # якщо в сесії є username тоді дістаємо його дані
        # добавляємо їх в словник для передачі в html форму
        sql = '''SELECT first_name,last_name,name,email,passw FROM users where name = "{}" '''.format(user)
        user_data = executeSelectOne(sql)
        context['first_name'] = user_data[0]
        context['last_name'] = user_data[1]
        context['name'] = user_data[2]
        context['email'] = user_data[3]
        context['pasww'] = user_data[4]

    return render_template('home.html', context=context)


def addToSession(name):
    session['username'] = name


@app.route('/registration', methods=["GET", "POST"])
def registr():
    context = {'Error': []}
    if request.method == 'POST':
        user = UserManager().getModelFromForm(request.form)
        if user.check_user():
            context['Error'].append('wrong name or email')
        if not user.user.password:
            context['Error'].append('incorrect password')
        if context['Error']:
            return render_template('registration.html', context=context)
        if user.addNewUser():
            addToSession(user.user.nickname)
            return redirect(url_for('home'))

        context['Error'].append('incorrect data')
    return render_template('registration.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)