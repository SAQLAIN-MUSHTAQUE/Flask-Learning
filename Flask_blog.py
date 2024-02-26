from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

app.config['SECRET_KEY'] =os.getenv('SECRET_KEY')

# Adding Dummy Data 
posts = [
    {
        'author': 'John Ducket',
        'title' : 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted': 'April 10, 2013'
    },
    {
        'author': 'Saqlain Mushtaque',
        'title' : 'Blog Post 2',
        'content' : 'Second Post content',
        'date_posted': 'April 15, 2013'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', Posts = posts)

@app.route('/about')
def About():
    return render_template("about.html", title = 'About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title = 'Sign Up' ,form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title = 'Sign in' ,form=form)

if __name__ == "__main__":
    app.run(debug=True)