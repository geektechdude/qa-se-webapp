from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskwebapp.database import get_database

from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('test', __name__)

@bp.route('/')
def index():
    return render_template('test/index.html')

@bp.route('/register', methods=('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_database()
        error = None
    
        if not username:
            error = 'Username and Password are required.'
        elif not password:
            error = 'Username and Password are required.'
        
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?,?)",
                    (username, generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                error = f"The username {username} is not available. Please login or create an account with a different username"
            else:
                return redirect(url_for("auth.login"))
    return render_template('test/register.html')

@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500