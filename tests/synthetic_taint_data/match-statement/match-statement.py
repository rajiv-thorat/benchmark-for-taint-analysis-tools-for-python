import json
from posixpath import abspath


class match_class:
    def read_file(self, path):
        character_file = open(abspath(path))
        character_sheet = json.loads(character_file)
        character_file.close()
        return character_sheet
    def match_case(self, character_sheet):
        match (character_sheet["race"]):
            case ("altmer") if self.character_sheet["name"] != "rajiv":
                self.print_character(self.character_sheet)
            case _:
                print("there was a problem reading the character file.")
    def print_character(self, character_sheet):
        print(character_sheet["race"])
        print(character_sheet["name"])

if __name__ == "__main__":
    match_case_ = match_class()
    character_sheet = match_case_.read_file(abspath("tests/synthetic-taint-data/resources/character-sheet.json"))
    match_case_.match_case(character_sheet)