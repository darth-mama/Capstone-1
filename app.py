from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db
import os
from dotenv import load_dotenv

dotenv_path = '/Users/Thuy/.bashrc'
# Load environment variables from .env file (only in development)
load_dotenv()

# 2. Access the token from the .env file
TOKEN_DOTENV = os.getenv('TOKEN')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///forms_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "iknowwhatyoudidlastsummer"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Define routes after creating the app object


@app.route('/get_token')
def get_token():
    return f'Token: {TOKEN}'


debug = DebugToolbarExtension(app)


app.app_context().push()
with app.app_context():
    connect_db(app)
    db.create_all()

base_url = "https://app.formbold.com"
