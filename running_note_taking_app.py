import newnoteapp

#to create a new note
newnoteapp.create_note("sunday notes","to Make notes on the sunday service")
newnoteapp.create_note("monday notes","to Make a new note application")
newnoteapp.create_note("tuesday notes","to play playstation")
newnoteapp.create_note("wednesday notes","to listen to music")

#giving the notes variables
note1 = newnoteapp.notes[0]
note2 = newnoteapp.notes[1]
note3 = newnoteapp.notes[2]
note4 = newnoteapp.notes[3]

#to view a note
print(newnoteapp.note_view(note1["note_id"]))
#to delete a note
print(newnoteapp.note_delete(note1["note_id"]))
#to list the notes
print(newnoteapp.note_list())
#to search a note by the note tittle
print(newnoteapp.note_query("sunday notes"))
#to search for notes by a word in the note content
print(newnoteapp.note_query2("Make"))
#to limit the note list to a specific number
print(newnoteapp.list_note_parameter())
#to limit the note search by a specific number
print(newnoteapp.note_query2_parameter("to"))
#pagination that limits the number of notes in a page 
print(newnoteapp.next(3,newnoteapp.notes))
