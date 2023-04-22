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




if __name__ == '__main__':
    unittest.main()


