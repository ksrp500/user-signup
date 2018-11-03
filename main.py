from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('home.html')
    return render_template('home.html')


@app.route("/add", methods=['POST'])
def add():

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    
    # check for invalid Username
    if username == "": 
        username_error = "Please enter a valid username."
    elif len(username) <= 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters long."
        username = ""
    elif " " in username:
        username_error = "Your username cannot contain any spaces."
        username = ""

    # check for invalid Password
    if password == "": 
        password_error = "Please enter a valid password."
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters long."
    elif " " in password:
        password_error = "Your password cannot contain any spaces."

    
    # check if Password matches
    if verify == "" or verify != password: 
        verify_error = "Passwords do not match. Please try again."
        verify = ""

    #check for invalid email
    if email == "":
        email_error = " "
    elif "." not in email: 
        email_error = "Your email must contain one '.' character."
    elif len(email) <= 3 or len(email) > 20:
        email_error = "email must be between 3 and 20 characters long."
    elif " " in email:
        email_error = "Your email cannot contain any spaces."
    elif "@" not in email:
        email_error = "Your email must contain one @ character."
        

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template('home.html', 
        username = username,
        username_error = username_error,
        password_error = password_error,
        verify_error = verify_error,
        email = email,
        email_error = email_error)

app.run()