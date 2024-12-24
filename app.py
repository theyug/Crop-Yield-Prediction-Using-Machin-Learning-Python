from flask import Flask, request, render_template, flash, redirect, url_for
import random

# Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages
users = {
    'testuser': 'password123',  # Example user
}

@app.route('/')
def index():
    # Initialize prediction to 0 when the page loads
    prediction = 0
    return render_template('index.html', prediction=prediction)

@app.route('/predict', methods=['POST'])
def predict():
    # Generate a random value when the "Predict" button is clicked
    prediction = round(random.uniform(1000, 5000), 2)
    return render_template('index.html', prediction=prediction)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            flash('Login successful!', 'success')
            return redirect(url_for('index'))  # Redirect to home page
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))  # Redirect back to login page

    return render_template('login.html')  # Serve the login page

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('signup'))

        if username in users:
            flash('Username already exists', 'danger')
            return redirect(url_for('signup'))

        # Add new user (in a real application, store this in a database)
        users[username] = password
        flash('Account created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('signup.html')  # Serve the signup page

if __name__ == "__main__":
    app.run(debug=True)
