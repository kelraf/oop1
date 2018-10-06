from app import app, user, bucketlist
from flask import request, render_template


@app.route('/register', methods=['POST', 'GET'])
def register(username, email, password, confirm_password):
    if request.method == "POST":
        register = request.form.user.register(username, email, password, confirm_password)
        return render_template('lo')
