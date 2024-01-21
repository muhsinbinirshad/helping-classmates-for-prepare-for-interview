# server.py
from flask import Flask, render_template, request, session
import os

app = Flask(__name__)

# Set a secret key for session management (used for CSRF token)
app.secret_key = os.urandom(24)

# Dummy storage for user data
user_data = []

@app.route('/')
def index():
    # Generate and store CSRF token in session
    csrf_token = os.urandom(24).hex()
    session['csrf_token'] = csrf_token
    return render_template('index.html', csrf_token=csrf_token)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Validate CSRF token
    if request.form.get('csrf_token') != session['csrf_token']:
        return 'Invalid CSRF token'

    # Get form data
    email = request.form.get('email')
    name = request.form.get('name')
    username = request.form.get('username')

    # Validate form data (you can add more validation as needed)
    if not email or not name or not username:
        return 'All fields are required'

    # Store user data (you might want to store it in a database)
    user_data.append({'email': email, 'name': name, 'username': username})

    return 'Form submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)
