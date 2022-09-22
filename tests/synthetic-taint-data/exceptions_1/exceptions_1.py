import sys
import helper

if __name__ == '__main__':
    source = ''

    try:
        source = sys.argv[1]
        raise RuntimeError()
    except:
        helper.run_cmd(source)