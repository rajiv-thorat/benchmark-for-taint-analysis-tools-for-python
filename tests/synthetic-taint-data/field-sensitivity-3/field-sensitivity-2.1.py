import sys
import helper
import character

if __name__=='__main__':
    char = character.Character()
    char.set_name = 'name'
    path = sys.argv[1]
    helper.run_cmd(char.get_path())
    char.set_path(path)

    