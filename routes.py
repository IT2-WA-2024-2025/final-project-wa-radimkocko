from flask import Blueprint, render_template, session, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/sporty')
def sporty():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    return render_template('sporty.html')

@main_bp.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')
