import random
import config_game
import string

def no_more_than_2_vowels(letter: str, list: list):
    vowel_counts = {}
    for vowel in config_game.VOWELS:
        count = list.count(vowel)
        vowel_counts[vowel] = count

    counts = vowel_counts.values()
    total_vowels = sum(counts)
    if total_vowels < 3:
        return True
    return False
    
def roll_letter_not_s():
    letter = 'S'
    while(letter in 'S'):
        letter = random.choice(string.ascii_letters).upper()
    return letter
    
def roll_letter_not_vowel_nor_s():
    invalid_letters = config_game.VOWELS + ["S"]
    letter = 'S'
    while(letter in invalid_letters):
        letter = random.choice(string.ascii_letters).upper()
    return letter        

def not_yet_in_list(letter: str, list: list):
    if letter in list:
        return False
    return True

def roll_multiple_unique_letters(count: int):
    list = []
    # first letter is special!
    # randomness has been a bit weird;
    # we see annoying characthers too often
    while len(list) == 0 or list[0] == 'X' or list[0] == 'Q' or list[0] == 'Y':
        list = []
        list.append(roll_letter_not_vowel_nor_s())

    while(len(list) < count):
        letter = roll_letter_not_s()
        if no_more_than_2_vowels(letter, list):
            if not_yet_in_list(letter, list):
                list.append(letter)

    return list
