from app import db

from .models import Link

def populateDb():
    inputFile = open("sample_txt_file.txt", "r")
    inputFile.seek(0)
    for line in inputFile:
        if line != "\n":
            real_line = ""
            for x in line:
                if x != "\n":
                    real_line += x
            if real_line[0] == "*":
                real_line = real_line[1:]
                link = Link(url=real_line, starred=True)
            elif ("www" not in real_line) or ("http" not in real_line):
                link = Link(url=real_line, header=True)
            else:
                link = Link(url=real_line)
        else:
            link = Link(space=True)
        db.session.add(link)
        db.session.commit()
    inputFile.close

def clearDb():
    for link in Link.query.all():
        db.session.delete(link)
    db.session.commit()

def printDb():
    for link in Link.query.all():
        print(link.id)
        print(link.url)
        print(link.starred)
        print(link.read)
        print(link.dead_link)
        print(link.header)
        print(link.space)
