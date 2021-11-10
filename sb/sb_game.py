#!/usr/bin/env python3

import time
import config_game
from uuid import uuid4
from sb_game_registry import SBGameRegistry
from oxforddictionaries.words import OxfordDictionaries

o = OxfordDictionaries

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

        if new_attempt.valid is False:
            return Exception('Word has non-matching letters')
        if new_attempt.word in self.gr.matches:
            return Exception('Word already part of the solution set')
        if len(new_attempt.word) < config_game.MIN_WORD_LENGTH:
            return Exception('Guessed word is too short. Minimum length:', str(config_game.MIN_WORD_LENGTH))
        if new_attempt.word[0] not in self.gr.letters[0]:
            return Exception('Must include letter:', self.gr.letters[0])

        result = o.get_info_about_word(Attempt.word).json()
        if result is None:
            return Exception('Not a valid word!')
        return result
        
    def calculate_points(attempt: Attempt):
        # simple scoring algorithm, for now
	    return len(attempt.word) - config_game.MIN_WORD_LENGTH + 1

    def process_valid_attempt(self, attempt: Attempt):
        if attempt.valid:
            additional_points = self.calculate_points(attempt)
            self.gr.score += additional_points
            self.gr.matches.append(attempt.word)
        

class AttemptEvaluation(Attempt):
    def __init__(self, word: str, letters: list, message):
        super().__init__(word, letters)
        self.points = SBGame.calculate_points(self)
        self.timestamp = time.time()
        self.attemptId = uuid4()
        self.message = message
        self.error = False
        self.errorMessage = ""
