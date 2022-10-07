import sys
import helper

if __name__=='__main__':
    array_1 = ['element 1', sys.argv[1]]
    array_2 = ['element 3', 'element 4', array_1[1]]

    helper.run_cmd(array_2[2])