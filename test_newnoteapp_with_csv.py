# import necessary modules

import unittest
import newnoteapp_with_csv_file
from newnoteapp_with_csv_file import notes

# test class
class Testnewnoteapp(unittest.TestCase):
    # happy test for the first function

    def test_create_note_happy_path(test):
        is_created = False
        newnoteapp_with_csv_file.create_note("thursday","wash clothes")
        note1 = newnoteapp_with_csv_file.notes[0]
        for note in notes:
            if note["note_tittle"] == "thursday":
                is_created = True
            if is_created == False:
                test.assertRaises(ValueError)

    def note_name_should_be_specific(test):
        is_empty = False
        newnoteapp_with_csv_file.create_note("note1","wash dishes")
        note1 = newnoteapp_with_csv_file.notes[0]
        for note in notes:
            if note["note_tittle"] == "note1":
                is_empty = True
        if is_empty == False:
            test.assertRaises(ValueError)

    def note_content_should_be_specific(self):
        is_similar = False
        newnoteapp_with_csv_file.create_note("note2","code")
        note2 = newnoteapp_with_csv_file.notes[0]
        for note in notes:
            if note["note_content"] == "code":
                is_similar = True
        if is_similar == False:
            self.assertRaises(ValueError)

    def note_name_and_content_should_not_be_empty(self):
        with self.assertRaises(ValueError):
            newnoteapp_with_csv_file.create_note(None,None)

    # happy path test for the find_note_by_id function

    def test_find_note_by_id_happy_path(self):
        is_found = False
        newnoteapp_with_csv_file.create_note("note3","sleep")
        note3 = newnoteapp_with_csv_file.notes[0]
        newnoteapp_with_csv_file.find_note_by_ID(note3["note_id"])
        is_found = True
        if is_found == False:
            self.assertRaises(ValueError)

    # happy path test for the view_note function

    def test_view_note_happy_path(self):
        is_viewed = False
        newnoteapp_with_csv_file.create_note("note4","worship")
        note4 = newnoteapp_with_csv_file.notes[0]
        is_note_found = False
        for note in notes:
            if note["note_id"] == note4["note_id"]:
                is_note_found = True
                note_ = note
        newnoteapp_with_csv_file.find_note_by_ID(note_["note_id"])
        is_viewed = True
        if is_viewed == False:
            self.assertRaises(ValueError)

    # happy path test for the delete_note function

    def test_delete_note_happy_path(self):
        is_deleted = False
        newnoteapp_with_csv_file.create_note("note5","pray")
        note5 = newnoteapp_with_csv_file.notes[0]
        is_note_found = False
        for note in notes:
            if note["note_id"] == note5["note_id"]:
                is_note_found = True
                note_ = note
        newnoteapp_with_csv_file.find_note_by_ID(note_["note_id"])
        is_deleted = True
        if is_deleted == False:
            self.assertRaises(ValueError)

if __name__ == '__main__':
    unittest.main()


