from Lipstick_System import app
from flask import render_template

@app.route('/history')
def history():
    return render_template('History/HistoryPage.html')