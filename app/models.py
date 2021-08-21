from app import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(300))
    starred = db.Column(db.Boolean)
    read = db.Column(db.Boolean)
    dead_link = db.Column(db.Boolean)
    header = db.Column(db.Boolean)
    space = db.Column(db.Boolean)

    def __init__(self, url="", starred=False, read=False, dead_link=False, header=False, space=False):
        self.url=url
        self.starred = starred
        self.read = read
        self.dead_link = dead_link
        self.header = header
        self.space = space
        
    def __repr__(self):
        return '<URL {}>'.format(self.url)

class Entry():
    def __init__(self, url, starred=False, read=False):
        self.url = url
        self.starred = starred
        self.read = read