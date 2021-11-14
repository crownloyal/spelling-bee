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
        # let's use some empty state as placeholder

    def ask_user_input(self) -> str:
        user_input = input('Your guess: ')
        user_input_mod = user_input.strip().upper()
        return user_input_mod    

    def try_solution(self, user_input: str) -> None:
        if len(user_input) == 0:
            print("You haven't entered anything; try again.")
            return
        elif user_input[0] == ".":
            self.help_module(user_input)
        else:
            attempt = Attempt(word=user_input, session=0, timestamp=1)
            validated_attempt = self.stub.AttemptGuess(attempt)
            if validated_attempt.message:
                print(validated_attempt.message)
            self.state = self.update_state()

    def update_state(self) -> None:
        timenow = str(time.time())
        req = StateRequest(timestamp=timenow)
        new = self.stub.GetSBGameState(req, None)
        return new

    def print_state(self):
        print("")
        print("= = = = =")
        print("INFO")
        print("Player:", self.state.player)
        print("Score:", self.state.score, "/ Avg:", self.state.score/self.state.tries if self.state.tries else 0) # sheesh python, I'll never like you but this kinda neat
        print("Tries:", self.state.tries)
        print("Solved:", self.state.wordlist)
        print("Letters:", self.state.letters)
        print("           ^ First letter required!")
        print("= = = = =")
        print("")
        
    def help_module(self, word):
        if word == '.SCORES':
            highscores = self.stub.GetHighscores(StateRequest(), None)
            print(highscores)
        elif word == '.HELP':
            print("If you don't know this game, we can't help you.")
            return
        elif word == '.NEW':
            return self.stub.CreateGame(StateRequest(), None)
        elif word == '.EXIT' or word == '.Q':
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
            terminal.print_state()
            guess = terminal.ask_user_input()
            terminal.try_solution(guess)
            terminal.state = terminal.update_state()
    
    terminal = SBTerminal()
    terminal.state = terminal.update_state()
    wrapper()