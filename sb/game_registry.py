#!/usr/bin/env python3

import time
import threading
import random
from uuid import uuid4

import database_manager
from sb_game import Player

class GameRegistry:

    __instance = None

    def __init__(self):
        if GameRegistry.__instance is not None:
            raise Exception("This is a singleton and already instanciated")
        else:
            GameRegistry.__instance = self
        self.lock = threading.lock()
        self.matches = {}
        self.instance = None

    @staticmethod
    def get_instance():
        if GameRegistry.__instance is None:
            with threading.lock():
                if GameRegistry.__instance is None:
                    GameRegistry()
                return GameRegistry.__instance

    def register_new_session(player: Player):
        if player is not None:
            Exception("Player object empty!")
        
    def update_game(letters: enumerate):
        if letters:
            return
    
    def roll_letters():
        list = []
        list.push()

    def create_game(player: Player):
        new_Player =GameRegistry.register_new_session(player)
        letters = GameRegistry.roll_letters()
        game = GameRegistry.update_game(letters)