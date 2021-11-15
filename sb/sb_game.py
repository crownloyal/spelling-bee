#!/usr/bin/env python3

import time
import config
import config_game
from uuid import uuid4
from sb_game_registry import SBGameRegistry

from lib.oxford_apiv2 import OxfordApiV2, CachingLanguageDictionary

ox = OxfordApiV2(config.api_key, config.api_secret)
cache = CachingLanguageDictionary(ox, 'en-gb')

class Attempt:
    def __init__(self, word: str, letters: list):
        self.word = word
        self.letters = letters
        validation = False # sane defaults
        if any(element in self.word for element in self.letters):
            validation = True
        self.valid = validation

class AttemptEvaluation(Attempt):
    def __init__(self, word: str, letters: list):
        super().__init__(word, letters)
        self.timestamp = str(time.time())
        self.attemptId = str(uuid4())
        self.message = None
        self.error = False
        self.errorMessage = ""
        self.points = 0

class Player:
    def __init__(self):
        self.id = uuid4()
        self.name = 'name'


class SBGame:
    def __init__(self, gr: SBGameRegistry):
        self.gr = gr

    def new_game(self):
        return self.gr.create_game()

    def validate_attempt(self, new_attempt: Attempt) -> AttemptEvaluation:
        self.gr.attempts += 1

        new_attempt = AttemptEvaluation(new_attempt.word, new_attempt.letters)

        if new_attempt.valid is False:
            new_attempt.message = "Word has non-matching letters"
            return new_attempt
        if new_attempt.word in self.gr.matches:
            new_attempt.valid = False
            new_attempt.message = "Word already part of the solution set"
            return new_attempt
        if len(new_attempt.word) < config_game.MIN_WORD_LENGTH:
            new_attempt.valid = False
            new_attempt.message = (f"Guessed word is too short. Minimum length: {str(config_game.MIN_WORD_LENGTH)}")
            return new_attempt
        if self.gr.letters[0] not in new_attempt.word:
            new_attempt.valid = False
            new_attempt.message = (f"Must include letter: {self.gr.letters[0]}")
            return new_attempt

        ox_result = cache.get_definitions(new_attempt.word)
        if ox_result == None:
            new_attempt.valid = False
            new_attempt.message = (f"Not a valid word if you believe Oxford")
            return new_attempt
        print(ox_result)
        word_type = ox_result[0]["lexicalEntries"][0]["lexicalCategory"]["text"]
        
        # sometimes words don't make sense?
        try: 
            word_sense = ox_result[0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
            new_attempt.message = (f"{word_type}; {word_sense}")
        except:
            new_attempt.message = (f"{word_type};")
        return new_attempt
    
    def calculate_points(self, attempt: AttemptEvaluation):
        # simple scoring algorithm, for now
        points = len(attempt.word) - config_game.MIN_WORD_LENGTH + 1
        return points

    def process_valid_attempt(self, attempt: AttemptEvaluation):
        if attempt.valid:
            attempt.points = self.calculate_points(attempt)
            self.gr.score += attempt.points
            self.gr.matches.append(attempt.word)
        
