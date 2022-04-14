import json
from posixpath import abspath

class with_statement:
    def __init__(self, file_path):
        self.file_path = file_path
      
    def __enter__(self):
        self.file = open(abspath(self.file_path))
        return json.load(self.file)
  
    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()

def print_character(character_sheet):
    print(character_sheet["race"])
    print(character_sheet["name"])

if __name__ == "__main__":
    with with_statement("synthetic-taint-data/resources/character-sheet.json") as character_sheet:
        print_character(character_sheet)