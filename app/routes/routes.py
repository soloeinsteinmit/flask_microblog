from flask import render_template, Blueprint, flash, redirect, url_for, request
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

microblog = Blueprint('main', __name__)

@microblog.route('/')
@microblog.route('/index')
@login_required
def index():
    user = {'username': "Solomon"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!',
         },
        {
            'author': {'username': 'Susan'},
            'body': 'The avenger movie is cool!',
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@microblog.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # first() methods Returns the first result of this Query or None if the result doesn't contain any row.
        if user is None or not user.check_password(form.password.data):
            flash(f'Invalid username of password')
            return redirect(url_for('main.login'))
        
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(url_for(next_page))

    return render_template('login.html', title="Sign In", form=form)

@microblog.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
