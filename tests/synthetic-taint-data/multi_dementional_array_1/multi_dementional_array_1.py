import sys
import helper
import numpy

if __name__=='__main__':
    multi_dem = numpy.array([sys.argv[1], 'element 1'],['element 2', 'element 3'])
    source_item = multi_dem[0,0]
    helper.run_cmd(source_item)
