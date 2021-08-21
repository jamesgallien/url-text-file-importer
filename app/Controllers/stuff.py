class Entry:
    def __init__(self, url, starred=False, read=False):
        self.url = url
        self.starred = starred
        self.read = read
    

inputFile = open("sample_txt_file.txt", "r")

try:
    outputFile = open("sample_txt_file2.txt", "x")
except:
    outputFile = open("sample_txt_file2.txt", "w")

inputFile.seek(0)
for line in inputFile:
    if line != "\n":
        outputFile.write(line)
        real_line = ""
        for x in line:
            if x != "\n":
                real_line += x
        if "google" in real_line:
            entry = Entry(real_line, True)
        else:
            entry = Entry(real_line)
        print(entry.url)
        print(entry.starred)
        print(entry.read)

inputFile.close
outputFile.close