import newnoteapp_with_csv_file

#to create a new note
newnoteapp_with_csv_file.create_note("sunday notes","to Make notes on the sunday service")
newnoteapp_with_csv_file.create_note("monday notes","to Make a new note application")
newnoteapp_with_csv_file.create_note("tuesday notes","to play playstation")
newnoteapp_with_csv_file.create_note("wednesday notes","to listen to music")

#giving the notes variables
note1 = newnoteapp_with_csv_file.notes[0]
note2 = newnoteapp_with_csv_file.notes[1]
note3 = newnoteapp_with_csv_file.notes[2]
note4 = newnoteapp_with_csv_file.notes[3]

#to test if the function that finds a class by class id really works
#print(newnoteapp_with_csv_file.find_note_by_ID(note1["note_id"]))

#to view a note
#print(newnoteapp_with_csv_file.note_view(note1["note_id"]))
#to delete a note
#print(newnoteapp_with_csv_file.note_delete(note1["note_id"]))
#to list the notes
#print(newnoteapp_with_csv_file.note_list())
#to search a note by the note tittle
#print(newnoteapp_with_csv_file.note_query("sunday notes"))
#to search for notes by a word in the note content
#print(newnoteapp_with_csv_file.note_query2("Make"))
#to limit the note list to a specific number
#print(newnoteapp_with_csv_file.list_note_parameter())
#to limit the note search by a specific number
#print(newnoteapp_with_csv_file.note_query2_parameter("to"))
#pagination that limits the number of notes in a page
#print(newnoteapp_with_csv_file.next(2,newnoteapp_with_csv_file.notes))
#export all notes to the notes.csv 
#newnoteapp_with_csv_file.export_notes("notes.csv")
#import all notes from notes.csv
#newnoteapp_with_csv_file.import_notes("notes.csv")
