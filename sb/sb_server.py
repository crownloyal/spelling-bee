#!/usr/bin/env python3

import config
import logging
from concurrent import futures

import grpc
import game_pb2_grpc
from sb_game_registry import SBGameRegistry
from sb_game import SBGame, Attempt

GRPC_VERBOSITY="debug"
GRPC_TRACE="all"

# inherit service class from compiled proto
class SBGameServer(game_pb2_grpc.SBGameService):
    def __init__(self, sbgreg: SBGameRegistry):
        super().__init__()
        # launch game instance for logic and persistence
        self.gr = sbgreg
        self.game = SBGame(self.gr)
        
    def launch(self):
        self.CreateGame(self.gr, None)
        print(self.gr.print_game_status())

    def CreateGame(self, req, context):
        response = self.game.new_game()
        gamestate = self.gr.gamestate()
        return gamestate

    def AttemptGuess(self, req, context):
        print("attempt event triggered")
        word = req
        evaluation = self.game.validate_attempt(
            Attempt(word, self.gr.letters)
        )
        return evaluation

    def GetSBGameState(self, req, context):
        # req is the client state; it *should* differ from the in-server state
        print("Gamestate req in")
        req_time = req
        gamestate = self.gr.gamestate()
        return gamestate

if __name__ == '__main__':
    logging.basicConfig()

    gr = SBGameRegistry()
    gameserver = SBGameServer(gr)
    gameserver.launch()

    # setup server
    rpcserver = grpc.server(futures.ProcessPoolExecutor(max_workers=10))
    game_pb2_grpc.add_SBGameServiceServicer_to_server(gameserver, rpcserver)
    # open grpc port
    rpcserver.add_insecure_port(f"{config.server_host}:{config.server_port}")
    rpcserver.start()
    print(f"Connection open @ {config.server_host}:{config.server_port}")
    rpcserver.wait_for_termination()

