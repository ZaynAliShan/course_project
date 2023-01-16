from flask import Blueprint, render_template, redirect, url_for, request
from app.models import User


main = Blueprint('main', __name__)

@main.route('/')

@main.route('/index', methods=['GET', 'POST'])
def index(cat=None):
    return render_template('index.html',  title='Home')

@main.route('/courses', methods=['GET', 'POST'])
def courses(cat=None):
    return render_template('courses.html',  title='Courses')

@main.route('/about', methods=['GET', 'POST'])
def about(cat=None):
    return render_template('about.html',  title='About')

@main.route('/blog', methods=['GET', 'POST'])
def blog(cat=None):
    return render_template('blog.html',  title='Blog')


@main.route('/Contact-us', methods=['GET', 'POST'])
def Contact(cat=None):
    return render_template('contact-us.html',  title='Contact-us')

@main.route('/FAQ', methods=['GET','POST'])
def FAQ(cat=None):
    return render_template('FAQ.html', title='FAQs')

@main.route('/news', methods=['GET','POST'])
def news(cat=None):
    return render_template('news.html', title='news')

@main.route('/Events', methods=['GET','POST'])
def Events(cat=None):
    return render_template('Events.html', title='Upcoming Events')


@main.route('/sponsor', methods=['GET','POST'])
def sponsor(cat=None):
    return render_template('sponsor.html', title='Business Sponsors')

@main.route('/reviews', methods=['GET','POST'])
def reviews(cat=None):
    return render_template('reviews.html', title='reviews')


@main.route('/Policy', methods=['GET','POST'])
def Policy(cat=None):
    return render_template('Policy.html', title='Policy')


