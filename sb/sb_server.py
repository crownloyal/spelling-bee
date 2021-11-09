#!/usr/bin/env python3

import grpc
import config
from concurrent import futures

from game_pb2_grpc import SBGameServicer, add_SBGameServicerServicer_to_server
from sb_game_registry import SBGameRegistry

from sb_game import SBGame

# inherit service class from compiled proto
class SBGameServer(SBGameServicer, SBGameRegistry):
    def __init__(self, SBGameServicer, SBGameRegistry):
        # setup server
        self.server = grpc.server(futures.ProcessPoolExecutor(max_workers=1))
        add_SBGameServicerServicer_to_server(SBGameServicer, self.server)
        # establish grpc connection
        self.server.add_insecure_port(f"{config.server_host}:{config.server_port}")
        self.GameSingleton = SBGame(SBGameRegistry)
        
    def launch(self, registry: SBGameRegistry):
        self.server.start()
        self.create_game(registry, None)
        # start() doesn't block so we need a sleep loop
        # https://grpc.io/docs/languages/python/basics/        
        print(registry.print_game_status())
        self.server.wait_for_termination()

    def create_game(self, req, context):
        response = self.GameSingleton.new_game()
        return response

    def attempt_guess(self, req, context):
        evaluation = self.GameSingleton.validate_attempt(req)
        return evaluation

    def get_SBGameState(self, req, context):
        return gr.gamestate()

gr = SBGameRegistry()
server = SBGameServer(SBGameServicer(), gr)
server.launch(gr)
