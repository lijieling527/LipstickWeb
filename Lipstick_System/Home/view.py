from Lipstick_System import app
from flask import render_template

@app.route('/home')
def home():
    return render_template('Home/HomePage.html')