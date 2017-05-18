from flask import Blueprint, render_template, redirect, url_for, flash
from form import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required
from model import User
from app import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            flash('ok')
            login_user(user, form.remember_me.data)
            return redirect(url_for('main.home'))
        flash('Invalid username or password')
    
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.home'))

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can login now')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)