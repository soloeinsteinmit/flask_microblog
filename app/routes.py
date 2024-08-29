from flask import render_template, Blueprint

microblog = Blueprint('main', __name__)

@microblog.route('/')
@microblog.route('/index')
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

