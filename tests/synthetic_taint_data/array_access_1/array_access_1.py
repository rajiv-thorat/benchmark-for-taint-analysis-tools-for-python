import helper
import sys

if __name__=='__main__':
    new_array = []
    new_array[0] = 'element 0'
    new_array[1] = sys.argv[1]
    new_array[2] = 'element 2'

    helper.run_cmd(new_array[1])
    helper.run_cmd(sys.argv[1])