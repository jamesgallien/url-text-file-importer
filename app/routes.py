from app import app
from flask import render_template

from .models import Link

@app.route('/')
def index():
    # application_name = {'name': 'My Links'}
    page_name = 'Link list'
    links = Link.query.all()
    return render_template ('index.html', links=links, application_name=page_name)

@app.route('/add')
def add():
    page_name = 'Add a link'
    return render_template ('add.html', application_name=page_name)
