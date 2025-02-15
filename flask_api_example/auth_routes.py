from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash  # Import for password hashing

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')  # Use .get() to avoid KeyError
        password = request.form.get('password')  # Use .get() to avoid KeyError
        
        if not username or not password:  # Check if fields are filled
            flash('Please enter both username and password.', 'danger')
            return render_template('login.html')

        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):  # Use hashed passwords
            login_user(user)
            return redirect(url_for('home'))  # Correctly redirecting to the index endpoint
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')  # Use .get() to avoid KeyError
        password = request.form.get('password')  # Use .get() to avoid KeyError
        
        if not username or not password:  # Check if fields are filled
            flash('Please enter both username and password.', 'danger')
            return render_template('register.html')

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)
        
        new_user = User(username=username, password=hashed_password)  # Store hashed password
        db.session.add(new_user)
        db.session.commit()
        flash('Account created for ' + username, 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')