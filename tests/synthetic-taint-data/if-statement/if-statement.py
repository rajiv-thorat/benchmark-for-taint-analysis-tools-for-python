#!/usr/bin/env python3
import json
from os.path import abspath


class if_branch:
    name: str
    race: str

    def print_race(self):
        print("The selected race is: " + self.race)
        if self.race == "breton":
            print(
                "The Bretons are half-elves, with more human than elvish blood, and populate the province of High Rock. Bretons originated in the First Era. A series of raids on Nedic holdings by the Aldmer, resulted in the destruction of all human settlements in Skyrim. "
            )
        elif self.race == "nord":
            print(
                "The Nords inhabit the northern province of Skyrim. They are strong and able warriors who are also highly resistant to frost. They are generally fair haired, pale, and blue eyed. Their origins can be traced all the way to the continent of Atmora."
            )
        elif self.race == "khajit":
            print(
                "The Khajiit are an anthropomorphic feline race hailing from the province of Elsweyr. Khajiit vary considerably in appearance, ranging from almost Elven Ohmes-raht to larger species such as the Senche (large tigers used as mounts) and the Cathay-Raht. Khajiit are generally excellent thieves and good fighters, and fierce individualists with generally no sense of 'private property.' Most of the Khajiit vary from orange to dusky red, though they can be other colors like black, white and tan."
            )
        elif self.race == "redguard":
            print(
                "The Redguards hail from the province of Hammerfell in western Tamriel. They are noted for their great strength, agility, and physical hardiness, and are very adept at surviving in hot, dry conditions. They are known as the most naturally talented warriors in all of Tamriel. They possess dark skin, ranging from light brown to nearly black in hue, often with a distinct reddish tint."
            )
        elif self.race == "argonian":
            print(
                "Argonians are a beast race of reptilian humanoids, consistently portrayed throughout the Elder Scrolls as intelligent, quick and agile, tending towards classes of the mage and the thief. Argonians inhabit the swampy region of Black Marsh. Years of defending their homeland has made them masters of warfare. They can breath underwater and are resistant to poison and diseases, but sadly have little resistance to ice. "
            )
        elif self.race == "bosmer":
            print(
                "The Bosmer, also called Wood Elf, inhabit the province of Valenwood. They are among the shortest races, and they are remarkable thieves and archers, due to their superior dexterity and agility, presumably because they spend their time living in trees."
            )
        elif self.race == "orismer":
            print(
                "Although beast-like in appearance, the Orsimer (Pariah Folk or simply Orcs) are descended from a group of Altmer (or even Aldmer) that worshipped a god named Trinimac. Orsimer were the former inhabitants of the province of Hammerfell, but lost their land to the armies of Redguards."
            )
        elif self.race == "dumner":
            print(
                "Dunmer, also called Dark Elves, hail from Morrowind. The Dunmer are the descendants of the Chimer, who were punished by the Daedric goddess Azura for the betrayal of their General, Indoril Nerevar. Azura's punishment was to turn the color of all the Chimer race's skin to ash-gray and their eyes to ruby red. "
            )
        elif self.race == "altmer":
            print(
                "The Altmer, also called High Elves, live in the Summerset Isle. They are taller than the other races and have a golden skin color. They tend to be proud and consider themselves the most civilized race."
            )
        elif self.race == "imperial":
            print(
                "Natives of the civilized, cosmopolitan province of Cyrodiil, the Imperials are well-educated and well-spoken. Though less physically imposing than the other races, the Imperials are shrewd diplomats and traders. These traits, along with their remarkable skill and training as light infantry, have enabled them to subdue all the other provinces of Tamriel and unite them under the banner of their prosperous empire."
            )
        else:
            print("The selected race: " + self.race + " == unknown.")

    def read_character_file(self, path):
        character_file = open(path)
        char_dict = json.load(character_file)
        character_file.close()
        self.name = char_dict['name']
        self.race = char_dict['race']


if __name__ == "__main__":
    char = if_branch()
    char.read_character_file(abspath("tests/synthetic-taint-data/resources/character-sheet.json"))
    char.print_race()
