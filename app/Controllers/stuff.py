from app import db

from ..models import Entry
from ..models import Link

# try:
#     outputFile = open("sample_txt_file2.txt", "x")
# except:
#     outputFile = open("sample_txt_file2.txt", "w")

def populateDatabase():
    return "Hello"

def getLinkList():
    inputFile = open("sample_txt_file.txt", "r")
    linkList = []
    inputFile.seek(0)
    for line in inputFile:
        if line != "\n":
            # outputFile.write(line)
            real_line = ""
            for x in line:
                if x != "\n":
                    real_line += x
            if real_line[0] == "*":
                real_line = real_line[1:]
                entry = Entry(real_line, True)
                link = Link(url=real_line, starred=True)
                db.session.add(link)
                db.session.commit()
            else:
                entry = Entry(real_line)
                link = Link(url=real_line)
                db.session.add(link)
                db.session.commit()
            print(link.id)
            print(link.url)
            print(link.starred)
            print(link.read)
            print(link.dead_link)
            linkList.append(entry)
    for link in Link.query.all():
        print(link)
    inputFile.close
    return linkList

# outputFile.close