import secrets
from flask import Flask, jsonify, request, render_template, redirect
from flask_login import LoginManager, login_required, current_user
from models import db, User
from mysql_utils import DBHelper
from auth_routes import auth
import os

app = Flask(__name__)

# Configure Flask app
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Generates a new key each time
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql://fastserver:Kishore123%24@localhost/products')
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # Redirect to login page if not logged in

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register the auth blueprint
app.register_blueprint(auth)

# Initialize the database helper instance
db_helper = DBHelper(host='localhost', user='fastserver', password='Kishore123$', database='products')
db_helper.init_db_connection()

@app.route('/')
@login_required
def root():
    """Redirect to the home page."""
    return redirect('/index')

@app.route('/index')
@login_required
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/item')
@login_required
def item():
    return render_template('item.html')

@app.route('/view')
@login_required
def view():
    """Render the view page."""
    items = db_helper.fetch_results("SELECT * FROM products")  # Fetch items from the database
    return render_template('view.html', items=items)

# API routes...

if __name__ == '__main__':
    app.run(debug=True)
