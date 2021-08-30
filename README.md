# url-text-file-importer

Problem: I've got a whole bunch of old text files with URLs I wanted to save. Yeah so back then I just copied and pasted them into a handful of text files. Stop laughing.

Solution: Anyways, so this is a little project to grab all that stuff, put it into a database, and render it in HTML. Nothing too earth-shattering. I might develop it further as I have time and inspiration.

Technologies: Python, Flask, SQLite, Bootstrap

Setup:

- clone this repository
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `flask db upgrade`
- `python`
- > `from app.functions import populateDb`
- > `populateDb('`[your text file here]`')`
- > `exit()`
- `flask run`
- Database will be created one level up from cloned repository directory, and app will be available at `localhost:5000`
