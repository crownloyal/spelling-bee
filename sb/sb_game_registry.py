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
            players = [],
            admin_uuid = None, 
            game_id = None,
            score = 0,
            attempts = 0,
            wordlist = [], 
            letters = [],
            matches = [],
            created_at = str(time.time()),
            last_update = None,
            gamecode = None
        ):
        # game ids
        self.players = players
        self.admin_uuid = admin_uuid
        self.game_id = game_id if game_id else str(uuid4())
        # game preperation
        self.score = score
        self.attempts = attempts
        self.wordlist = wordlist
        self.letters = letters
        self.matches = matches
        self.created_at = created_at
        self.last_update = last_update if last_update != None else self.created_at
        # generate game id (playername + uuid[1:8])
        short_gamecode = self.players[0] if len(self.players) > 0 else "game"
        self.gamecode = short_gamecode + self.game_id[1:8]

    def print(self):
        print("")
        print("= = = = =")
        print("INFO")
        print("Player:", self.players)
        print("Score:", self.score, "/ Avg:", self.score/self.attempts if self.attempts else 0) # sheesh python, I'll never like you but this kinda neat
        print("Tries:", self.attempts)
        print("Solved:", self.wordlist)
        print("Letters:", self.letters)
        print("           ^ First letter required!")
        print("= = = = =")
        print("")

    def print_game_status_short(self):
        letters = str(self.letters)
        gamecode = self.gamecode
        print(f"{gamecode} :: {letters}")

class SBGameRegistry:
    _instance = None
    _lock = threading.Lock()

    def __init__(self) -> None:
        self.games = {}
        
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
    
    def create_game(self, uuid, playername) -> SBGameState:
        letters = roll_multiple_unique_letters(7)
        new_game = SBGameState(
            players = [ playername ],
            admin_uuid = uuid,
            letters = letters
            )
        self.games[new_game.gamecode] = new_game
        new_game.print_game_status_short()
        return new_game

    def lookup_game_session(self, sessionid):
        for game in self.games:
            if game.session == sessionid:
                return game
            else:
                return None

    def lookup_game_code(self, gamecode: str):
        if self.games[gamecode]:
            return self.games[gamecode]
        return None

    def gamestate(self, gamecode: str) -> SBGameState:
        game = self.lookup_game_code(gamecode)
        return game