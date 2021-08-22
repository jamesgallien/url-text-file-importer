from app import app, db
from flask import render_template, flash, redirect, url_for

from .models import Link
from .forms import AddForm

@app.route('/')
def index():
    # application_name = {'name': 'My Links'}
    page_name = 'Link list'
    links = Link.query.all()
    return render_template ('index.html', links=links, application_name=page_name)

@app.route('/add', methods=['GET', 'POST'])
def add():
    page_name = 'Add a link'
    form = AddForm()
    if form.validate_on_submit():
        # flash('Add requested for link: {}'.format(form.link.data))
        link=Link(url=form.link.data, starred=form.starred.data, read=form.read.data,
            dead_link=form.dead_link.data, header=form.header.data)
        db.session.add(link)
        db.session.commit()
        flash('Added link: {}'.format(form.link.data))
        return redirect(url_for('add'))
    return render_template('add.html', application_name=page_name, form=form)

