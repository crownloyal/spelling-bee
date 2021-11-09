#!/usr/bin/env python3

import time
import threading
import random
import string
from typing import List
from uuid import uuid4

import config_game

class SBGameState:
    def __init__(
            self, 
            player = 0, 
            session = 0, 
            score = 0, 
            tries = 0,
            wordlist = [],
            time = 0
        ):
        self.player = player
        self.session = session
        self.score = score
        self.tries = tries
        self.wordlist = wordlist
        self.timestamp = time

class SBGameRegistry:
    _instance = None
    _lock = threading.Lock()

    matches = []
    letters = None
    attempts = 0
    score = 0

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
            # another thread could have created the instance
            # before we acquired the lock. So check that the
            # instance is still nonexistent.
                if not cls._instance:
                    cls._instance = super(SBGameRegistry, cls).__new__(cls)
        return cls._instance                

    @staticmethod
    def get_instance(self):
        if SBGameRegistry._instance is None:
            with threading.Lock():
                if SBGameRegistry._instance is None:
                    SBGameRegistry()
                return SBGameRegistry._instance

    def no_more_than_2_vowels(self, letter: str, list: List):
        vowel_counts = {}
        for vowel in config_game.VOWELS:
            count = list.count(vowel)
            vowel_counts[vowel] = count

        counts = vowel_counts.values()
        total_vowels = sum(counts)
        if total_vowels < 3:
            return True
        return False
    
    def roll_letter_not_s(self):
        letter = 'S'
        while(letter in 'S'):
            letter = random.choice(string.ascii_letters).upper()
        return letter
    
    def roll_letter_not_vowel_nor_s(self):
        invalid_letters = config_game.VOWELS + ["S"]
        letter = 'S'
        while(letter in invalid_letters):
            letter = random.choice(string.ascii_letters).upper()
        return letter        

    def not_yet_in_list(self, letter: str, list: List):
        if letter in list:
            return False
        return True

    def roll_multiple_unique_letters(self, count: int):
        list = []
        # first letter is special!
        list.append(self.roll_letter_not_vowel_nor_s())

        while(len(list) < count):
            letter = self.roll_letter_not_s()
            if self.no_more_than_2_vowels(letter, list):
                if self.not_yet_in_list(letter, list):
                    list.append(letter)
        return list

    def create_game(self):
        self.letters = self.roll_multiple_unique_letters(7)
        self.attempts = 0
        self.score = 0

    def print_game_status(self):
        letters = self.letters
        points = self.score
        return [ letters, points ]

    def gamestate(self):
        state = SBGameState(
            0, 
            0,
            self.score,
            self.attempts,
            self.matches,
            time.time()
        )
        return state
