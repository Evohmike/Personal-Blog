from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required,current_user
#from .forms import CategoryForm

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title = "Welcome | One Minute Pitch"
    return render_template('index.html',title=title)
