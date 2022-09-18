import sys
import helper
import character

if __name__=='__main__':
    char = character.Character()
    char.set_name = 'name'
    char.set_path(sys.argv[1])
    helper.run_cmd(char.get_path())

    