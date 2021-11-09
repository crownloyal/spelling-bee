#!/usr/bin/env python3

import random
import time
import threading
from tinydb import TinyDB, Query

class DatabaseManager:
    
    def db_update_session(data):
        TinyDB.find()
        pass

    def db_update_game(data):
        pass

    def db_update_highscore(data):
        pass

    def get_last_session_by_player(player: Player):
        pass
        # do things

    def revoke_last_active_session(player: Player):
        pass
