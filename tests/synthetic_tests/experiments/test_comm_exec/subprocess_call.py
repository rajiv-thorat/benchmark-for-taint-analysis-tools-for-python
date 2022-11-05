import sys
from subprocess import call_check

def command_execution_unsafe(action) -> None:
    call_check(["application", action])

if __name__=='__main__':
    command_execution_unsafe(sys.argv[1])
