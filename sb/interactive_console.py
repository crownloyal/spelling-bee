#!/usr/bin/env python3

import grpc
import config
from game_pb2_grpc import SBGameServicerStub
from game_pb2 import SBGameState, Attempt

class SBTerminal:
    def __init__(self):    
        # establish grpc channel
        # inherit from grpc config
        channel = grpc.insecure_channel(f"{config.server_host}:{config.server_port}")
        self.stub = SBGameServicerStub(channel)
        self.state = SBGameState()

    def ask_user_input(self) -> str:
        user_input = input('Your guess: ')
        user_input_mod = user_input.strip().upper()
        return user_input_mod    

    def try_solution(self, user_input: str) -> None:
        attempt = Attempt(word=user_input, session=0, timestamp=1)
        response = self.stub.attempt_guess(attempt)
        print(response.value)
        self.update_state(self)

    async def update_state(self) -> None:
        self.state = await self.stub.get_SBGameState(self.state)
        
    def help(word):
        if(word) == 'highscore':
            # get highscore from grpc
            return
        if word == 'help':
            # get help text
            return
        print('Did not recognize command; try !highscore or !help')

terminal = SBTerminal()
terminal.update_state()

# console game loop
while True:
    print(terminal.state)
    guess = terminal.ask_user_input()
    terminal.try_solution(guess)
    