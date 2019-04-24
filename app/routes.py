from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ronald'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Singapore!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers Endgame was not that nice!'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)
