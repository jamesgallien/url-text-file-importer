from app import app
from flask import render_template

@app.route('/')
def index():
    # return "Hello, world!"
    application_name = {'name': 'Links'}
    return render_template ('index.html', application_name=application_name)
