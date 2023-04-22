import csv

#export all notes 
def export_notes(filename):
    with open(filename,"w",newline="") as csvfile:
        fieldnames = ["note_id","note_tittle","note_content","created_at","updated_at"]
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        for note in notes:
            writer.writerow(note)
    print(f"notes exported to {filename}.")

#import notes from csv 
def import_notes(filename):
    with open(filename,"r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            notes.append({
                "note_tittle": row["note_tittle"],
                "note_content": row["note_content"],
                "note_id": uuid.UUID(row["note_id"]),
                "created_at": datetime.strptime(row["created_at"],'%Y-%m-%d %H:%M:%S.%f'),
                "updated_at": row["updated_at"]
            })
    print(f"notes imported from {filename}.")
#import necessary modules
import uuid
import math
from datetime import datetime
#creating an empty notes list to store the notes
notes = []
#create note function
def create_note(note_tittle,note_content):
    #note tittle should not b empty
    if note_tittle== "":
        raise ("note tittle cannot be empty")
    #note content should not be empty
    if note_content == "":
        raise ("note content should not be empty")
    #note tittle should not be similar
    for note in notes:
        if note["note_tittle"] == note_tittle :
            raise ("note tittle should be unique")
    #note content should be unique
    for note in notes:
        if note["note_content"] == note_content:
            raise ("note content should not be similar")

    #note properties
    note = {
        "note_id":str(uuid.uuid4()),
        "note_tittle": note_tittle,
        "note_content": note_content,
        "created_at":datetime.now(),
        "updated_at":None
        }
    #add the note to the list of notes
    notes.append(note)

#find a note using the note ID
def find_note_by_ID(note_id):
    is_note_found = False
    for note in notes:
        if note["note_id"] == note_id:
            note_ = note
            is_note_found = True
    if is_note_found == False:
        raise ValueError("note has not been created")


#note view function
def note_view(note_id):
    is_note_found,note_ = find_note_by_ID(note_id)
    if not is_note_found:
        raise("the note with the note id not found")
    return note_

#note delete function
def note_delete(note_id):
    is_deleted = False
    is_note_found,note_ = find_note_by_ID(note_id)
    notes.remove(note_)
    is_deleted = True
    if is_deleted == True:
        return ("note has been deleted")
    else:
        return ("note has not been deleted")

#notes list function
def note_list():
    return notes

#note tittle query
def note_query(note_tittle):
    for note in notes:
        if note["note_tittle"] == note_tittle:
            return note

#note query 2
def note_query2(query_string):
    notes_found = []
    for note in notes:
        if query_string in note["note_content"]:
            notes_found.append(note)

    return notes_found

def list_note_parameter(limit = 3):
    return notes[:limit]

def note_query2_parameter(query_string,limit = 1):
    notes_found = []
    for note in notes:
        if query_string in note["note_content"]:
            notes_found.append(note)

    return notes_found[:limit]

#diffrent way of doing  it
"""def next(page,notes,limit = 3):
    print("Numbber of notes: ",len(notes))
    total_pages = math.ceil(len(notes)/limit)
    if page < 1 or page > total_pages:
        raise("page number must be greater than 1 and less than (number of elements / limit)")
    if page == 1:
        return notes[0:limit]
    else:
        return notes[page * limit:(page*limit) + limit]
"""

def next(page, notes, limit=3):
    total_notes = len(notes)
    total_pages = math.ceil(total_notes / limit)

    if page < 1 or page > total_pages:
        raise ValueError("Invalid page number")

    start_index = (page - 1) * limit
    end_index = min(start_index + limit, total_notes)
    return notes[start_index:end_index]

import running_noteapp_with_csv_file