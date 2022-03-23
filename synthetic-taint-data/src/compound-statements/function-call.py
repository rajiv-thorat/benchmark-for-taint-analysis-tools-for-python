import json
from posixpath import abspath


class function_call_test:
    def source_in_default_parameter_value(self, character_file=open(abspath("synthetic-taint-data/resources/character-sheet.json"))):
        self.print_character(json.load(character_file))
    def print_character(self, character_sheet):
        print(character_sheet["race"])
        print(character_sheet["name"])


if __name__ == "__main__":
    function_call_test_ = function_call_test()
    function_call_test_.source_in_default_parameter_value()