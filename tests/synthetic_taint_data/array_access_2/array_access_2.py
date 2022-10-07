import sys
import helper
import random

if __name__=='__main__':
    new_array = []
    new_array[5] = sys.argv[1]
    new_array[4] = 'element 4'

    helper.run_cmd(new_array[calculate_index()])

def calculate_index():
    return random.randint(0, 5)