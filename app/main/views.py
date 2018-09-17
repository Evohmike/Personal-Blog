from flask import render_template,redirect,url_for,abort,request,flash
from . import main
from flask_login import login_required,current_user
from ..models import User,Blogpost
from .forms import UpdateProfile,PostForm
from .. import db


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title = "Welcome | Personal-Blog"
    return render_template('index.html',title=title,
        blogposts=Blogpost.query.all()
    )



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        about(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photos' in request.files:
        filename = photo.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))





@main.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

# @main.route('/add')
# def add():
#     return render_template('add.html')

@main.route('/addpost', methods=['POST','GET'])
def addpost():
    form = PostForm()
    if form.validate_on_submit():
        title =  form.title.data
        subtitle = form.subtitle.data
        content = form.pitch.data

        post = Blogpost(title=title, subtitle=subtitle, author=current_user.id, content=content)

        db.session.add(post)
        db.session.commit()

        flash("Posted!")
        return redirect(url_for('.index'))

    return render_template('post.html',form=form)







