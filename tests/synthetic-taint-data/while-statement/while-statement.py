from os.path import abspath
from random import randint
import json
from secrets import randbelow

class while_loop:
    def randomize_prime(self):
        random_number = randint(1,20)
        max_run_count = 10
        while not self.is_prime(random_number) and max_run_count != 0:
            print("the number is not prime. reading the character sheet.")
            character_file = open(abspath("tests/synthetic-taint-data/resources/character-sheet.json"))
            character_sheet = json.load(character_file)
            character_file.close()
            self.print_character(character_sheet)
            random_number = randint(0, 20)
            max_run_count = max_run_count - 1
        print("The randomly generated number was a prime number")
    def is_prime(self, random_number):
        if random_number == 2 or random_number == 3:
            return True
        for i in range(2, random_number - 1):
            if random_number % i == 0:
                return False
        return True
    def print_character(self, character_sheet):
        print(character_sheet["race"])
        print(character_sheet["name"]) 

if __name__ == "__main__":
    while_loop_ = while_loop()
    while_loop_.randomize_prime()