import sys
import helper
import character

char = character.Character()

def setTaint(char):
    char.set_name = 'name'
    char.set_path(sys.argv[1])

def passTaint():
    helper.run_cmd(char.get_name())

if __name__=='__main__':
    setTaint(char)
    passTaint()

    