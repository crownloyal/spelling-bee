#!/usr/bin/env python3

import time
import config
import config_game
from uuid import uuid4
from sb_game_registry import SBGameRegistry

from oxforddictionaries.words import OxfordDictionaries

o = OxfordDictionaries(config.api_key, config.api_secret)

class Attempt:
    def __init__(self, word: str, letters: list):
        self.word = word
        self.letters = letters
        validation = False # sane defaults
        if str(letters) in word:
            validation = True
        self.valid = validation

class Player:
    def __init__(self):
        self.id = uuid4()
        self.name = 'name'

class SBGame:
    def __init__(self, gr: SBGameRegistry):
        self.gr = gr

    def new_game(self):
        return self.gr.create_game()

    def validate_attempt(self, new_attempt: Attempt):
        self.gr.attempts += 1

        new_attempt = AttemptEvaluation(new_attempt.word, new_attempt.letters)

        if new_attempt.valid is False:
            new_attempt.message = "Word has non-matching letters"
            return new_attempt

        if new_attempt.word in self.gr.matches:
            new_attempt.message = "Word already part of the solution set"
            return new_attempt
        if len(new_attempt.word) < config_game.MIN_WORD_LENGTH:
            new_attempt.message = (f"Guessed word is too short. Minimum length: {str(config_game.MIN_WORD_LENGTH)}")
            return new_attempt
        if new_attempt.word[0] not in self.gr.letters[0]:
            new_attempt.message = (f"Must include letter: {self.gr.letters[0]}")
            return new_attempt

        result = o.get_info_about_word(Attempt.word).json()
        if result is None:
            new_attempt.error = True
            new_attempt.message = (f"Not a valid word if you believe Oxford")
            return new_attempt
        print(result)
        return new_attempt
        
    def calculate_points(attempt: Attempt):
        # simple scoring algorithm, for now
	    return len(attempt.word) - config_game.MIN_WORD_LENGTH + 1

    def process_valid_attempt(self, attempt: Attempt):
        if attempt.valid:
            additional_points = self.calculate_points(attempt)
            self.gr.score += additional_points
            self.gr.matches.append(attempt.word)
        

class AttemptEvaluation(Attempt):
    def __init__(self, word: str, letters: list):
        super().__init__(word, letters)
        self.points = SBGame.calculate_points(self)
        self.timestamp = str(time.time())
        self.attemptId = str(uuid4())
        self.message = None
        self.error = False
        self.errorMessage = ""
