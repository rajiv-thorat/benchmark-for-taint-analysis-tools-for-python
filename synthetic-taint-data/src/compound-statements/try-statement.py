from ast import Try
import json
from posixpath import abspath


class try_statement:
    def read_a_couple_of_character_sheets(self):
        try:
            character_printed = False
            missing_character_printed = False
            character_sheet = json.load(open(abspath("synthetic-taint-data/resources/character-sheet.json")))
            self.print_character(character_sheet)
            character_printed = True
            missing_character_sheet = json.load(open(abspath("synthetic-taint-data/resources/the-missing-character-sheet.json")))
            self.print_character(missing_character_sheet)
            missing_character_printed = True
        except:
            missing_character_sheet = json.load(open(abspath("synthetic-taint-data/resources/character-sheet.json")))
            self.print_character(missing_character_sheet)
            missing_character_printed = True
        finally:
            if not character_printed or not missing_character_printed:
                print("there was a problem reading the character sheets.")
        
    def print_character(self, character_sheet):
        print(character_sheet["race"])
        print(character_sheet["name"])

if __name__ == "__main__":
    try_statement_ = try_statement()
    try_statement_.read_a_couple_of_character_sheets()
