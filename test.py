from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('test', __name__)

@bp.route('/')
def index():
    return render_template('test/index.html')
