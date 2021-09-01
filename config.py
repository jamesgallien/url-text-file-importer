import os
from posixpath import pardir
basedir = os.path.abspath(os.path.dirname(__file__))
parentdir = os.path.abspath(os.path.dirname(basedir))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(parentdir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-should-change-this-password'
    POSTS_PER_PAGE = 10
    
    