from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User
#from .forms import CategoryForm

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title = "Welcome | Personal-Blog"
    return render_template('index.html',title=title)




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        about(404)

    return render_template("profile/profile.html", user = user)




