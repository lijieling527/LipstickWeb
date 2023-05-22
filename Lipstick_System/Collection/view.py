from Lipstick_System import app
from flask import render_template

@app.route('/collection')
def like():
    return render_template('Collection/LikePage.html')