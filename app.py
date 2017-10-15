# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for, session
from executeSqlite3 import executeSelectOne, executeSelectAll
import os

# створюємо головний об'єкт сайту класу Flask
app = Flask(__name__)
# добавляємо секретний ключ для сайту щоб шифрувати дані сессії
# при кожнаму сапуску фласку буде генечитись новий рандомний ключ з 24 символів
app.secret_key = os.urandom(24)


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
        name = executeSelectOne(sql)
        if name:
            session['username'] = name
            return redirect(url_for('home'))

    return render_template('login.html')

# описуємо домашній роут
# сіда зможуть попадати тільки GET запроси
@app.route('/')
def home():
    user = session.get('username', None)
    context = {}
    if user:
        # якщо в сесії є username тоді дістаємо його дані
        # добавляємо їх в словник для передачі в html форму
        sql = '''SELECT first_name,last_name,name,email,passw FROM users where name = "{}" '''.format(user[0])
        user_data = executeSelectOne(sql)
        context['first_name'] = user_data[0]
        context['last_name'] = user_data[1]
        context['name'] = user_data[2]
        context['email'] = user_data[3]
        context['pasww'] = user_data[4]

    return render_template('home.html', context=context)

# описуємо роут для вилогінення
# сіда зможуть попадати тільки GET запроси
@app.route('/logout')
def logout():
    user = session.get('username', None)
    if user:
        # якщо в сесії є username тоді видаляємо його
        del session['username']
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
