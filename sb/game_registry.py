#!/usr/bin/env python3

import time
import threading
from sb_game import SBGame

class GameRegistry:

    __instance = home

    def __init__(self):
        if GameRegistry.__instance in not None:
            raise Exception("This is a singleton and already instanciated")
        else:
            GameRegistry.__instance = self
        self.lock = threading.lock()
        self.matches = {}
        self.instance = None

    def get_instance():
        if GameRegistry.__instance is None:
            with threading.lock():
                if GameRegistry.__instance is None:
                    GameRegistry()

    def createGame(player):
        SBGame.new_game(player)

        return