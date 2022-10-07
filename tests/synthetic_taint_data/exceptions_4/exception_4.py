import sys
import helper

if __name__ == '__main__':
    source = ''

    try:
        source = sys.argv[1]
        raise RuntimeError(source)
    except RuntimeError as ex:
        helper.run_cmd(ex.message)