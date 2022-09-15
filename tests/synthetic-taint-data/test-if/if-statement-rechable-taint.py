#!/usr/bin/env python3
import random
from os.path import abspath
import subprocess
import sys

import helper

        
if __name__=='__main__':
    i = 10
    j = -1
    if len(sys.argv) < 2:
        print("please include args.")
        exit(1) 
    path = sys.argv[1]
    helper.run_cmd(path)
    #subprocess.call("wget %s", path)
    #subprocess.call("wget %s", sys.arg[0])
    if i > 0:
        # 
        char_dict = helper.read_character_file(abspath(path))
        helper.run_cmd(['co', 'test', 'run', '--keep-databases', path],
                "codeql test failed. Please fix up the test before proceeding.")
        print(char_dict)
        j = j + char_dict['age']
    else:
        j = 0
        print("Wrong value:", i)
        helper.run_cmd(path)
    print("final score :", i + j)

