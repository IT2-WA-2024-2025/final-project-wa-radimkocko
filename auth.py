from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth_bp = Blueprint('auth', __name__)

users = {}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('main.sporty'))
        else:
            flash('Špatné přihlašovací údaje', 'danger')
            return redirect(url_for('auth.login'))
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Uživatel již existuje', 'danger')
            return redirect(url_for('auth.register'))
        users[username] = password
        session['user'] = username
        return redirect(url_for('main.sporty'))
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('main.index'))
