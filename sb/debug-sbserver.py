#!/usr/bin/env python3

import config
import logging
from concurrent import futures

import grpc
import game_pb2
import game_pb2_grpc

from sb_game_registry import SBGameRegistry
from sb_game import SBGame, Attempt

# inherit service class from compiled proto
class SBGameServer(game_pb2_grpc.SBGameService):
    def __init__(self, sbgr: SBGameRegistry, game: SBGame) -> None:
        super().__init__()
        self.gr = sbgr
        self.game = game

    def GetSBGameState(self, req, context):
        state = self.gr.gamestate()
        return game_pb2.SBGameState(
            player=state.player,
            session=state.session,
            score=state.score,
            tries=state.tries,
            wordlist=state.wordlist,
            timestamp=state.timestamp
            )
    
    def launch(self):
        self.CreateGame()
        print(self.gr.print_game_status())
        print("   ^ First letter required!")

    def CreateGame(self):
        self.gr.create_game()
        state = self.gr.gamestate()
        return game_pb2.SBGameState(
            player=state.player,
            session=state.session,
            score=state.score,
            tries=state.tries,
            wordlist=state.wordlist,
            timestamp=state.timestamp
            )

    def AttemptGuess(self, req, context):
        try:
            evaluation = self.game.validate_attempt(
                Attempt(req.word, self.gr.letters)
                )
        except:
            return game_pb2.AttemptEvaluation(
                valid = evaluation.valid,
                message = evaluation.message,
                word = evaluation.word,
                points = evaluation.points,
                timestamp = evaluation.timestamp,
                attemptId = evaluation.attemptId
                error = evaluation.error
                errorMessage = evaluation.errorMessage
            )

        return game_pb2.AttemptEvaluation(
            valid = evaluation.valid,
            message = evaluation.message,
            word = evaluation.word,
            points = evaluation.points,
            timestamp = evaluation.timestamp,
            attemptId = evaluation.attemptId
            error = False
            errorMessage = ""
        )


def serve():
    gr = SBGameRegistry()
    game = SBGame(gr)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpcservice = SBGameServer(gr, game)
    game_pb2_grpc.add_SBGameServiceServicer_to_server(rpcservice, server)

    rpcservice.launch()

    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()