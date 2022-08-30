from flask import render_template
from . import main

@main.route('/', methods=['GET'])
def index():
    return render_template('views/index.html')

