from app import app
from flask import render_template

from app.Controllers.stuff import getLinkList

@app.route('/')
def index():
    application_name = {'name': 'My Links'}
    links=getLinkList()
    return render_template ('index.html', application_name=application_name, links=links)
