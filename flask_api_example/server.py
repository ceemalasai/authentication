import secrets
from flask import Flask, jsonify, request, render_template, redirect, url_for, send_from_directory, flash
from flask_login import LoginManager, login_required, current_user
from models import db, User
from mysql_utils import DBHelper
from auth_routes import auth
import os
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Configure Flask app
app.config['SECRET_KEY'] = 'a38ed1b1369a27a3be1122ab49ce9723'  # Generates a new key each time
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql://fastserver:Kishore123%24@localhost/products')
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # Redirect to login page if not logged in

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))  # Use session.get() instead of User.query.get()

# Register the auth blueprint
app.register_blueprint(auth)

# Initialize the database helper instance
db_helper = DBHelper(host='localhost', user='fastserver', password='Kishore123$', database='products')
db_helper.init_db_connection()
@app.route('/static/style.css')
def serve_css():
    response =send_from_directory('static', 'style.css')
    response.headers['Cache-Control']='no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma']='no-cache'
    response.headers['Expires']='0'
    return response

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
@app.route('/item', methods=['GET', 'POST'])
@login_required
def item():
    """Render the item page."""
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        price = request.form.get('price')
        tag = request.form.get('tag')
        print(f"Received data - Name: {name}, Category: {category}, Price: {price}, Tag: {tag}")

        if name and category and price and tag:
            query = "INSERT INTO products (name, category, price, tag) VALUES (%s, %s, %s, %s)"
            params = (name, category, price, tag)
            try:
                db_helper.insert_record(query, params)
                message ="item added successfully"
            except Exception as e:
                message = f"Error:{str(e)}"
        else:
            message = "missing required fields"  

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
