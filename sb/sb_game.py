#!/usr/bin/env python3

from grpc import CallCredentials
import config_game
from uuid import uuid4
from game_pb2 import Attempt
from sb_game_registry import SBGameRegistry
from oxforddictionaries.words import OxfordDictionaries

o = OxfordDictionaries

class Attempt:
    def __init__(self, word, letters):
        self.word = word
        self.letters = letters
        validation = False
        if letters in word:
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

    def validate_attempt(self, attempt: Attempt):
        self.gr.attempts += 1

        if attempt.valid is False:
            return Exception('Word has non-matching letters')
        if attempt.word in self.gr.matches:
            return Exception('Word already part of the solution set')
        if len(attempt.word) < config_game.MIN_WORD_LENGTH:
            return Exception('Guessed word is too short. Minimum length:',str(config_game.MIN_WORD_LENGTH),'\n')
        if attempt.word[0] not in self.gr.letters[0]:
            return Exception('Must include letter:', self.gr.letters[0],'\n')

        result = o.get_info_about_word(Attempt).json()
        if result is None:
            return Exception('Not a valid word!')
        return result
        
    def calculate_points(attempt: Attempt):
        # simple scoring algorithm, for now
	    return len(attempt.word) - config_game.MIN_WORD_LENGTH + 1

    def process_valid_attempt(self, attempt: Attempt):
        additional_points = self.calculate_points(attempt)
        self.gr.score += additional_points
        self.gr.matches.push(attempt.word)
