#!/usr/bin/env python3

import grpc
import config
import game_pb2
from game_pb2_grpc import SBGameServicerStub

class SBTerminal:
    def __init__(self):    
        # establish grpc channel
        channel = grpc.insecure_channel(f"{config.client_host}:{config.client_port}")
        self.stub = SBGameServicerStub(channel) # inherit from grpc config

    def ask_user_input():
        user_input = input('Your guess: ')
        user_input = user_input.strip().upper()
        return user_input    

    def try_solution(self, user_input: str):
        attempt = game_pb2.Attempt(word=user_input, session=0, timestamp=1)
        response = self.stub.attemptGuess(attempt)
        print(response.value)
        return response.value
        

    def help(word):
        if(word) is 'highscore':
            # get highscore from grpc
            return
        if word is 'help':
            # get help text
            return
        print('Did not recognize command; try !highscore or !help')