import json
from posixpath import abspath


class match_class:
    def read_file(self, path):
        character_file = open(abspath(path))
        self.character_sheet = json.loads(character_file)
        character_file.close()
    def match_case(self):
        match (self.character_sheet["race"]):
            case ("altmer") if self.character_sheet["name"] != "rajiv":
                print_character(self.character_sheet)