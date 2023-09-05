from webApplication import app
from flask import render_template, request, redirect, url_for, flash, get_flashed_messages
from webApplication.registerForm import RegisterForm
from webApplication.models import User
from webApplication import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit(): #if 'POST'
        print(form.username.data)
        print(form.password.data)
        newUser = User(username = form.username.data, email = form.email_address.data, password = form.password.data)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for error in form.errors.values():
            flash(f'Oops: {error}')
    
    return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])

    

@app.route('/chat')
def chat_page():
    username = request.args.get('username')
    return render_template('chat.html')