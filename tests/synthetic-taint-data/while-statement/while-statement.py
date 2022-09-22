from os.path import abspath
from random import randint
import json
from secrets import randbelow
import sys
import helper

class while_loop:
    def randomize_prime(self):
        random_number = randint(1,20)
        max_run_count = 10
        return_value = ''
        while not self.is_prime(random_number) and max_run_count != 0:
            return_value = sys.argv[1]
        return return_value
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
    helper.run_cmd(while_loop_.randomize_prime()) 