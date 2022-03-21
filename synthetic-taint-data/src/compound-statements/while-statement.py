from os.path import abspath
from random import randint
import json
from secrets import randbelow

class while_loop:
    def randomize_prime(self):
        random_number = randint(0,20)
        while not self.is_prime(random_number):
            print("the number is prime. reading the character sheet.")
            return json.load(open(abspath("synthetic-taint-data/resources/character-sheet.json")))
        print("The randomly generated number was not a prime number")
    def is_prime(self, random_number):
        for i in range(2, random_number):
            if random_number % i == 0:
                return False

if __name__ == "__main__":
    while_loop_ = while_loop()
    while_loop_.randomize_prime()