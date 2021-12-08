#!/usr/bin/env python3

from os import stat
import config
import logging
from concurrent import futures

import grpc
import game_pb2
import game_pb2_grpc

from sb_game_registry import SBGameRegistry
from sb_game import AttemptEvaluation, SBGame, Attempt

# inherit service class from compiled proto
class SBGameServer(game_pb2_grpc.SBGameService):
    def __init__(self, sbgr: SBGameRegistry, game: SBGame) -> None:
        super().__init__()
        self.gr = sbgr
        self.game = game

    def GetSBGameState(self, req, context):
        state = self.gr.gamestate(req.gamecode)
        return game_pb2.SBGameState(
            players = state.players,
            gameId = state.game_id,
            score = state.score,
            attempts = state.attempts,
            wordlist = state.wordlist,
            lastUpdate = state.last_update,
            letters = state.letters,
            gamecode = state.gamecode,
            )
    
    def CreateGame(self, req, context):
        game = self.gr.create_game(req.adminUUID, req.adminPlayer)
        state = self.gr.gamestate(game.gamecode)
        return game_pb2.SBGameState(
            players = state.players,
            gameId = state.game_id,
            score = state.score,
            attempts = state.attempts,
            wordlist = state.wordlist,
            createdAt = state.created_at,
            lastUpdate = state.last_update,
            letters = state.letters,
            matches = state.matches,
            gamecode = state.gamecode,
            )

    def AttemptGuess(self, req, context) -> AttemptEvaluation:
        word = req.word
        attempt = Attempt(word, self.gr.letters)
        evaluation = self.game.validate_attempt(attempt)

        if evaluation.valid is True:
            self.game.process_valid_attempt(evaluation)

        return game_pb2.AttemptEvaluation(
            valid = evaluation.valid,
            word = evaluation.word,
            points = evaluation.points,
            timestamp = evaluation.timestamp,
            attemptId = evaluation.attemptId,
            message = evaluation.message,
        )
  
    def GetHighscores(self, req, context):
        return game_pb2.SBHighScores(
            player = self.gr.players,
            score = self.gr.highscore
        )

def serve():
    gr = SBGameRegistry()
    game = SBGame(gr)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpcservice = SBGameServer(gr, game)
    game_pb2_grpc.add_SBGameServiceServicer_to_server(rpcservice, server)

    server.add_insecure_port(f"{config.server_host}:{config.server_port}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()