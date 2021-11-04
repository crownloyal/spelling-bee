from uuid import uuid4
from google.protobuf import descriptor
from game_pb2 import Attempt, AttemptEvaluation, SBGameState
from game_registry import create_game, get_session
from database_manager import lookup_lastGame
from oxforddictionaries.words import OxfordDictionaries

o = OxfordDictionaries

class Attempt:
    def __init__(self):
        pass

class Player:

    def __init__(self):
        self.id = uuid4()
        self.name = 'name'
        self.session = get_session(self)

class SBGame:

    def __init__(self):
        pass

    def new_game(player: Player):
        create_game(player)
        # make new database entry for user
        # create new game session
        # create new random letters
        # grpc
        return True
    
    def get_session(player: Player):
        session = lookup_lastGame(player)
        print(session)

    def validate_attempt(attempt: Attempt):
        print(attempt)
        result = o.get_info_about_word(Attempt).json()
        if result is not None:
            return result
        else:
            return Exception('Not a valid word!')

    def attempt_solution(attempt: Attempt):
        return SBGame.validate_attempt(attempt.word)
