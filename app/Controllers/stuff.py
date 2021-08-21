class Entry:
    def __init__(self, url, starred=False, read=False):
        self.url = url
        self.starred = starred
        self.read = read

# try:
#     outputFile = open("sample_txt_file2.txt", "x")
# except:
#     outputFile = open("sample_txt_file2.txt", "w")

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
            else:
                entry = Entry(real_line)
            linkList.append(entry)
    inputFile.close
    return linkList

# outputFile.close