import sys
import helper
import numpy

if __name__ == '__main__':
    empty_list = numpy.empty( numpy.sqrt(49), dtype=object)
    source = ''
    try:
        source = sys.argv[1]
        if empty_list[8] == 'test value':
            source = 'problem'
    except:
        helper.run_cmd(source)