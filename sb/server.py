#!/usr/bin/env python3

import time
import grpc
import config
from concurrent import futures

from game_pb2 import Attempt
from game_pb2_grpc import SBGameServicer, add_SBGameServicerServicer_to_server
from sb_game import SBGame

# inherit service class from compiled proto
class SBGameServer(SBGameServicer):

    def __init__(self):
        # setup server
        self.server = grpc.server(futures.ProcessPoolExecutor(max_workers=8))
        add_SBGameServicerServicer_to_server(SBGameServer, self.server)
        # establish grpc connection
        self.server.add_insecure_port(f"{config.server_host}:{config.server_port}")
        self.GameSingleton = SBGame()
        
    def launch(self):
        self.server.start()
        # start() doesn't block so we need a sleep loop
        # https://grpc.io/docs/languages/python/basics/
        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            self.server.stop(0);

    def createGame(self, req, context):
        player = req
        response = self.GameSingleton.create_game(player)
        return response

    def attemptGuess(self, req, context):
        evaluation = self.GameSingleton.validate_attempt(req)
        return evaluation


    

