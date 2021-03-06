from app import app, db
from flask import render_template, flash, redirect, url_for, request

from .models import Link
from .forms import AddForm

@app.route('/')
def index():
    page_name = 'Link list'
    page = request.args.get('page', 1, type=int)
    sort = request.args.get('sort', "a")
    if sort == 'a' or sort == None:
        links = Link.query.paginate(page, app.config['POSTS_PER_PAGE'], False)
    else:
        links = Link.query.order_by(Link.id.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)
    prev_url = url_for('index', page=links.prev_num, sort=sort) if links.has_prev else None
    next_url = url_for('index', page=links.next_num, sort=sort) if links.has_next else None
    pages = links.pages
    return render_template ('index.html', links=links.items, 
                            application_name=page_name, 
                            next_url=next_url, 
                            prev_url=prev_url,
                            page=page,
                            pages=pages,
                            sort=sort)

@app.route('/add', methods=['GET', 'POST'])
def add():
    page_name = 'Add a link'
    form = AddForm()
    if form.validate_on_submit():
        link=Link(url=form.link.data, starred=form.starred.data, read=form.read.data,
            dead_link=form.dead_link.data, header=form.header.data)
        db.session.add(link)
        db.session.commit()
        flash('Added link: {}'.format(form.link.data))
        return redirect(url_for('add'))
    return render_template('add.html', application_name=page_name, form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    link=Link.query.get(request.args.get('id'))
    db.session.delete(link)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    page_name = 'Edit a link'
    form = AddForm()
    link=Link.query.get(request.args.get('id'))
    if not form.validate_on_submit():
        form.link.data=link.url
        form.starred.data=link.starred 
        form.read.data=link.read
        form.dead_link.data=link.dead_link
        form.header.data=link.header
        return render_template('add.html', application_name=page_name, form=form)
    link.url=form.link.data
    link.starred=form.starred.data
    link.read=form.read.data
    link.dead_link=form.dead_link.data
    link.header=form.header.data
    db.session.commit()
    return redirect('/?page=' + request.args.get('return'))
