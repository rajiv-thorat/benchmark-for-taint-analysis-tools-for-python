#!/usr/bin/env python3
import json
import random
from os.path import abspath

def read_character_file(path):
    character_file = open(path)
    char_dict = json.load(character_file)
    character_file.close()
    return char_dict

if __name__ == "__main__":
    i = 10
    j = -1
    if i > 0:
        j = 0
        print("Wrong value:", i)
    else:
        # Taint introduced in the unreachable branch.
        char_dict = read_character_file(abspath("tests/synthetic-taint-data/resources/character-sheet.json"))
        print(char_dict)
        j = j + char_dict['age']
    print("final score :", i + j)