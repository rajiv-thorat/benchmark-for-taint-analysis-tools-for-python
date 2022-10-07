import sys
import helper

if __name__=='__main__':
    diction = {'tainted': sys.argv[1], 'untainted': 'untainted value'}

    helper.run_cmd(diction.get('tainted'))