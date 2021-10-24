#!/usr/bin/env python3

import config
import time
import json
import requests
import sb_game
from oxforddictionaries.words import OxfordDictionaries


def 



class SBServer:

    def __init__(self):
        self.app_id = config.api_key
        self.app_key = config.api_secret
        self.o = OxfordDictionaries(self.app_id, self.app_key)

    def async_word_search(self, word):
        result = self.o.get_info_about_word(word).json()

class State():
    def 
