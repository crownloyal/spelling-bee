#!/usr/bin/env python3

import time
import grpc
import config
import logging
from game_pb2_grpc import SBGameServiceStub
from game_pb2 import StateRequest, SBGameState, Attempt

class SBTerminal:
    def __init__(self):    
        # establish grpc channel
        # inherit from grpc config
        channel = grpc.insecure_channel(f"{config.server_host}:50051")
        print(f"Connecting to server @ {config.server_host}:{config.server_port}")
        self.stub = SBGameServiceStub(channel)
        self.state = SBGameState() 
        # let's use some empty state as placehold

    def ask_user_input(self) -> str:
        user_input = input('Your guess: ')
        user_input_mod = user_input.strip().upper()
        return user_input_mod    

    def try_solution(self, user_input: str) -> None:
        attempt = Attempt(word=user_input, session=0, timestamp=1)
        self.stub.AttemptGuess(attempt)
        self.update_state()

    def update_state(self) -> None:
        timenow = str(time.time())
        req = StateRequest(timestamp=timenow)
        new = self.stub.GetSBGameState(req, None)
        self.state = new
        
    def help(word):
        if(word) == '!highscore':
            # get highscore from grpc
            return
        if word == '!help':
            # get help text
            return
        if word == '!new':
            # shuffle letters
            return
        print('Did not recognize command; try !highscore or !help')

if __name__ == '__main__':
    logging.basicConfig()
    # console game loop
    def wrapper():
        while True:
            print(terminal.state)
            guess = terminal.ask_user_input()
            terminal.try_solution(guess)
        
    terminal = SBTerminal()
    terminal.update_state()
    wrapper()