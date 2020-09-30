#!/usr/bin/env python


import json
import random
import urllib.request


def check_note_validity(note):
    if note['parent_id'] in excluded_ids:
        return False
    else:
        return True

def randomnote(notes):
    random.shuffle(notes)
    return notes[0]

def recurse_subnotebooks(notebook):
    if "children" in notebook.keys():
        for subnotebook in notebook['children']:
            excluded_ids.append(subnotebook['id'])
            recurse_subnotebooks(subnotebook)




token = "lalala"
excluded_notebooks = ["0 INBOX", "4 Archives"]

folders_bytes = urllib.request.urlopen("http://localhost:41184/folders?token={}".format(token)).read()
notes_bytes = urllib.request.urlopen("http://localhost:41184/notes?token={}".format(token)).read()
notebooks = json.loads(folders_bytes)
notes = json.loads(notes_bytes)

excluded_ids = []
for notebook in notebooks:
    if notebook['title'] in excluded_notebooks:
        excluded_ids.append(notebook['id'])
        recurse_subnotebooks(notebook)

found_a_valid_note = False
therandomnote = ""

while not found_a_valid_note:
    pluck = randomnote(notes)
    if check_note_validity(pluck):
        found_a_valid_note = True
        therandomnote = pluck['title']

print(therandomnote)

