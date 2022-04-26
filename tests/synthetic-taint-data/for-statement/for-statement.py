#!/usr/bin/env python3
import os
import json
from os.path import abspath

class for_loop:
    def find_character_sheet(self, path):
       character_sheet = None
       for file in os.listdir(path):
           complete_path = os.path.join(path, file)
           if os.path.isfile(complete_path) and file == "character-sheet.json":
               character_file = open(complete_path)
               character_sheet = json.load(character_file)
               character_file.close()
               if character_sheet != "":
                   print("The loop executed successfully.")
                   return character_sheet
       if character_sheet is None:
            print("There was a problem reading the file.")

    def print_character(self, character_sheet):
        print(character_sheet["race"])
        print(character_sheet["name"]) 

if __name__ == "__main__":
    testing_for_loop = for_loop()
    testing_for_loop.print_character(testing_for_loop.find_character_sheet(abspath("tests/synthetic-taint-data/resources"))) 
