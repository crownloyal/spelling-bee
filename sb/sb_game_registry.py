#!/usr/bin/env python3

from logging import error
import time
import threading
from typing import List
from uuid import uuid4

from letter_scramble import roll_multiple_unique_letters

class SBGameState:
    def __init__(
            self, 
            player = 0, 
            session = 0, 
            score = 0, 
            tries = 0,
            wordlist = [],
            time = 0,
            letters = [],
        ):
        self.player = player
        self.session = session
        self.score = score
        self.tries = tries
        self.wordlist = wordlist
        self.timestamp = time
        self.letters = letters

    def print(self):
        print("Player:", self.player)
        print("session:", self.session)
        print("score:", self.score)
        print("wordlist:", self.wordlist)
        print("timestamp:", self.timestamp)
        print("letters:", self.letters)

class SBGameRegistry:
    _instance = None
    _lock = threading.Lock()

    def __init__(self) -> None:
        self.matches = []
        self.letters = None
        self.attempts = 0
        self.score = 0
        self.highscore = 0

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
    
    def create_game(self):
        if self.highscore < self.score:
            self.highscore = self.score
        self.letters = roll_multiple_unique_letters(7)
        self.attempts = 0
        self.score = 0
        self.matches = []
        print(self.print_game_status())
        
    def print_game_status(self):
        letters = self.letters
        points = self.score
        return [ letters, points ]

    def gamestate(self):
        state = SBGameState(
            "crown", 
            0,
            self.score,
            self.attempts,
            self.matches,
            int(time.time()),
            letters=self.letters
        )
        return state
