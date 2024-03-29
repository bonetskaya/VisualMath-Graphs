from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User, Lecture
from werkzeug.urls import url_parse
from datetime import datetime


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html", title="Main page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your registration completed!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/<username>/lectures')
@login_required
def progress(username):
    user = User.query.filter_by(username=username).first_or_404()
    lectures = Lecture.query.all()
    return render_template('lectures.html', user=user, lectures=lectures)


@app.route('/<username>/lectures/<lecture_name>')
@login_required
def show_lecture(username, lecture_name):
    return render_template('lectures/' + lecture_name)
