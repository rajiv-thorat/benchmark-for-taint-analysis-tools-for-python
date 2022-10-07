import sys
import helper
import numpy

if __name__ == '__main__':
    empty_list = numpy.empty( numpy.sqrt(49), dtype=object)
    source = ''
    try:
        source = sys.argv[1]
        empty_list[2] == ''
        if empty_list[2] == 'test value':
            source = 'problem'
    except:
        helper.run_cmd(source)