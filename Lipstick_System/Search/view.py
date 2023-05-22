from Lipstick_System import app
from flask import render_template

@app.route('/pic_search')
def Picture_search():
    return render_template('Search/Picture_Search.html')