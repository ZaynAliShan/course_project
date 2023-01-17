from app import create_app
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

file_path = os.path.abspath(os.getcwd()) + "\database.db"

app = create_app()

app.config['SECRET_KEY'] = "ahmad123."
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path

# initalize db
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# User Schema
class Admins(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

# Content (Article Schema)
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return Admins.query.get(int(user_id))



class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route("/articles")
def articles():
    return render_template("admin_panel.html")

@app.route("/add_article")
def add_article():
    return render_template("addarticle.html")

@app.route("/show_all_articles")
def show_all_articles():
    articles = Content.query.all()
    return render_template("show_all_articles.html", articles = articles)


# Route to add articles
@app.route('/add_content', methods=['POST'])
def add_content():
    title = request.form['title']
    body = request.form['body']
    new_content = Content(title=title, body=body)
    db.session.add(new_content)
    db.session.commit()
    return render_template("addarticle.html", msg = 'Article Added Successfully!') 


@app.route("/admin_login", methods=['GET', 'POST'])
def admin_login():
        form = LoginForm()

        # check if form was submitted
        if form.validate_on_submit():
            user = Admins.query.filter_by(username=form.username.data).first() # check if user exisits in database
            if user:
                if check_password_hash(user.password, form.password.data): #check if password matches
                    login_user(user, remember=form.remember.data)
                    return redirect(url_for('admin_dashboard'))         

            # incase username or password doesn't exist
            return '<h1>Invalid username or password</h1>'
        return render_template("admin_login.html" ,form = form)

@app.route("/show_articles_forUser")
def show_articles_forUser():
    articles = Content.query.all()
    return render_template("show_articles_forUser.html", articles = articles)

@app.route("/faqs")
def faqs():
    return render_template("FAQs.html")


@app.route("/admin_dashboard")
@login_required
def admin_dashboard():
    return render_template("admin_panel.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
 
    @app.route("/homepage")
    def homepage():
        return render_template ("index.html")





# @app.route("/member_signup", methods=['GET', 'POST'])
# def member_signup():
#         form = RegisterForm()

#         # check if form was submitted : Store data in DB if submission done
#         if form.validate_on_submit():
#             hashed_password = generate_password_hash(form.password.data, method='sha256')
#             new_user = Admins(username=form.username.data, email=form.email.data, password=hashed_password)
#             db.session.add(new_user)
#             db.session.commit()        
#             return '<h1>New User has been Created!</h1>'
#         return render_template("member_signup.html", form = form)