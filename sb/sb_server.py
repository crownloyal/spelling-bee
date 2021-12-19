#!/usr/bin/env python3

import config
import logging
import pickle
from concurrent import futures
import threading

import grpc
import game_pb2
import game_pb2_grpc

from sb_game_registry import SBGameRegistry
from sb_game import AttemptEvaluation, SBGame, Attempt
from sb_socket import SocketClientMixin

# inherit service class from compiled proto
class SBGameServer(game_pb2_grpc.SBGameService, SocketClientMixin):
    def __init__(self, sbgr: SBGameRegistry, game: SBGame) -> None:
        super(SocketClientMixin)
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
            gamecode = state.gamecode,
            )

    def AttemptGuess(self, req, context) -> AttemptEvaluation:
        word = req.word
        gamecode = req.gamecode
        try: 
            game = self.gr.lookup_game_code(gamecode)
        except: 
            return self.CreateGame()
        attempt = Attempt(word, game.letters, gamecode)
        evaluation = self.game.validate_attempt(attempt)

        if evaluation.valid:
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

    def AddUserToGame(self, req, context):
        gamecode = req.gamecode
        user = req.username
        state = self.gr.gamestate(gamecode)
        state.players.append(user)
        return game_pb2.SBGameState(
            players = state.players,
            gameId = state.game_id,
            score = state.score,
            attempts = state.attempts,
            wordlist = state.wordlist,
            createdAt = state.created_at,
            lastUpdate = state.last_update,
            letters = state.letters,
            gamecode = state.gamecode,
            )

    def UploadScore(self, req, context):
        gamecode = req.gamecode
        state = self.gr.gamestate(gamecode)
        self.sock_send_object(state)
        return game_pb2.SBGameState(
            players = state.players,
            gameId = state.game_id,
            score = state.score,
            attempts = state.attempts,
            wordlist = state.wordlist,
            createdAt = state.created_at,
            lastUpdate = state.last_update,
            letters = state.letters,
            gamecode = state.gamecode,
            )

def serve():
    gr = SBGameRegistry()
    game = SBGame(gr)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpcservice = SBGameServer(gr, game)
    game_pb2_grpc.add_SBGameServiceServicer_to_server(rpcservice, server)

    server.add_insecure_port(f"{config.server_host}:{config.server_port}")
    print(f"Lauched on {config.server_host}:{config.server_port}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()