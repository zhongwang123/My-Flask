from flask_login import login_required
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def home():
    return render_template('index.html')
