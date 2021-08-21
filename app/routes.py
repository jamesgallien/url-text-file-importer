from app import app
from flask import render_template

from .models import Link

@app.route('/')
def index():
    application_name = {'name': 'My Links'}
    links = Link.query.all()
    return render_template ('index.html', links=links, application_name=application_name)

@app.route('/add')
def add():
    application_name = {'name': 'My Links'}
    return render_template ('add.html', application_name=application_name)
