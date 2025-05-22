from flask import Blueprint, render_template, request, redirect, url_for, session, flash  
from storage import find_user, add_user, verify_password  

auth_bp = Blueprint('auth', __name__)  

@auth_bp.route('/login', methods=['GET', 'POST'])  

def login():
    if request.method == 'POST':  
        username = request.form['username']  
        password = request.form['password']  
        user = find_user(username)  

        if verify_password(user, password):  
            session['user'] = username  
            return redirect(url_for('main.sporty'))  
        flash('Špatné přihlašovací údaje', 'danger')  
        return redirect(url_for('auth.login'))  
    return render_template('login.html')  

@auth_bp.route('/register', methods=['GET', 'POST'])  
def register():
    if request.method == 'POST':  
        username = request.form['username']  
        password = request.form['password']  
        if find_user(username):  
            flash('Uživatel již existuje', 'danger')  
            return redirect(url_for('auth.register'))  
        add_user(username, password)  
        session['user'] = username  
        return redirect(url_for('main.sporty'))  
    return render_template('register.html')  

@auth_bp.route('/logout')  

def logout():
    session.pop('user', None)  
    return redirect(url_for('main.index'))  