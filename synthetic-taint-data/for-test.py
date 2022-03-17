#!/usr/bin/env python3
import os
import json

class for_loop:
   def find_character_sheet(self, path):
       character_sheet = None
       for file in os.listdir(path):
           if os.path.isfile(os.path.join(path, file)) and file == "character-sheet.json":
               character_sheet = json.loads(file)
       if character_sheet is None:
            print("There was a problem reading the file.")


if __name__ == "__main__":
    testing_for_loop = for_loop()
    testing_for_loop.find_character_sheet
