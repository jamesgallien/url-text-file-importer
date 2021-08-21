import os
from posixpath import pardir
basedir = os.path.abspath(os.path.dirname(__file__))
parentdir = os.path.abspath(os.path.dirname(basedir))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(parentdir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
    
    