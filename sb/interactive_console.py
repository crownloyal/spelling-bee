#!/usr/bin/env python3

import time
import grpc
import config
import logging
from game_pb2_grpc import SBGameServiceStub
from game_pb2 import StateRequest, Attempt
from sb_game_registry import SBGameState

class SBTerminal:
    def __init__(self):    
        # establish grpc channel
        # inherit from grpc config
        channel = grpc.insecure_channel(f"{config.server_host}:{config.server_port}")
        print(f"Connecting to server @ {config.server_host}:{config.server_port}")
        self.stub = SBGameServiceStub(channel)
        self.state = SBGameState() 
        self.exit = True
        # let's use some empty state as placehold

    def ask_user_input(self) -> str:
        user_input = input('Your guess: ')
        user_input_mod = user_input.strip().upper()
        return user_input_mod    

    def try_solution(self, user_input: str) -> None:
        if user_input[0] == ".":
            self.help_module(user_input)
        else:
            attempt = Attempt(word=user_input, session=0, timestamp=1)
            self.stub.AttemptGuess(attempt)
            self.state = self.update_state()

    def update_state(self) -> None:
        timenow = str(time.time())
        req = StateRequest(timestamp=timenow)
        new = self.stub.GetSBGameState(req, None)
        return new
        
    def help_module(self, word):
        if word == '.SCORES':
        # get highscore from grpc
            return
        elif word == '.HELP':
            print("If you don't know this game, we can't help you.")
            return
        elif word == '.NEW':
            return self.stub.CreateGame(StateRequest(), None)
        elif word == '.EXIT':
            print("Quitting...")
            # optional: save state in DB
            self.exit = False
        else:
            print('Did not recognize command; try $SCORES or $HELP')

if __name__ == '__main__':
    logging.basicConfig()
    # console game loop
    def wrapper():
        while terminal.exit:
            print(terminal.state)
            print(terminal.state.letters)

            guess = terminal.ask_user_input()
            terminal.try_solution(guess)
            terminal.state = terminal.update_state()

        
    terminal = SBTerminal()
    terminal.state = terminal.update_state()
    wrapper()