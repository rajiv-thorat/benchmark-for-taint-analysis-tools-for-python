import sys
from subprocess import check_call

variable = sys.argv[1]
check_call(['ls', variable])