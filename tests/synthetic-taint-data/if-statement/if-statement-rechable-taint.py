#!/usr/bin/env python3
import json
import random
from os.path import abspath
import subprocess
import sys

def read_character_file(path):
    character_file = open(path)
    char_dict = json.load(character_file)
    character_file.close()
    return char_dict

def main():
    i = 10
    j = -1
    if i > 0:
        path = sys.arg[0]
        # "tests/synthetic-taint-data/resources/character-sheet.json"
        char_dict = read_character_file(abspath(path))
        run_cmd(path)
        print(char_dict)
        j = j + char_dict['age']
    else:
        j = 0
        print("Wrong value:", i)
    print("final score :", i + j)

def run_cmd(cmd, msg="Failed to run command"):
    print('Running ' + ' '.join(cmd))
    if subprocess.check_call(cmd):
        print(msg)
        exit(1)