#!/usr/bin/env python3

import time
import grpc
import config
import logging
from uuid import uuid4
from game_pb2_grpc import SBGameServiceStub
from game_pb2 import StateRequest, NewGameRequest, JoinGameRequest, Attempt, Player
from sb_game_registry import SBGameState

class SBTerminal():
    def __init__(self, user):
        super()
        # establish grpc channel
        # inherit from grpc config
        channel = grpc.insecure_channel(f"{config.server_host}:{config.server_port}")
        print(f"Connecting to server @ {config.server_host}:{config.server_port}")
        self.stub = SBGameServiceStub(channel)
        self.state = {} 
        self.exit = True
        self.uuid = str(uuid4())
        self.username = user

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
            attempt = Attempt(word=user_input, gamecode=self.state.gamecode, timestamp=1)
            validated_attempt = self.stub.AttemptGuess(attempt)
            if validated_attempt.message:
                print(validated_attempt.message)
            self.state = self.update_state(self.state.gamecode)

    def update_state(self, gamecode) -> SBGameState:
        timenow = str(time.time())
        req = StateRequest(timestamp=timenow, gamecode=gamecode)
        new_state = self.stub.GetSBGameState(req, None)
        return self.map_state(new_state)

    def map_state(self, state_response) -> SBGameState:
        return SBGameState(
                players = state_response.players,
                game_id = state_response.gameId,
                score = state_response.score,
                attempts = state_response.attempts,
                letters = state_response.letters,
                wordlist = state_response.wordlist,
                created_at = state_response.createdAt,
                last_update = state_response.lastUpdate,
                gamecode = state_response.gamecode
            )

    def new_game(self) -> SBGameState:
        req = NewGameRequest(
            adminPlayer = self.username, 
            adminUUID = self.uuid
        )
        new_state = self.stub.CreateGame(req, None)
        return self.map_state(new_state)
        
    def join_game(self, gamecode) -> None:
        if gamecode:
            try:
                req = JoinGameRequest(gamecode=gamecode, username=self.username)
                state_response = self.stub.AddUserToGame(req, None)
                self.state = self.map_state(state_response)
                return #early
            except Exception as ex: 
                print("Couldn't find game, generating new one")
                print("Exception:", ex)
        self.state = self.new_game()

    def loop(self) -> None:
        while self.exit:
            self.state.print()
            guess = self.ask_user_input()
            self.try_solution(guess)
            self.state = self.update_state(gamecode=self.state.gamecode)
        
    def upload_score(self) -> None:
        try:
            req = StateRequest(gamecode=self.state.gamecode)
            self.stub.UploadScore(req)
        except Exception as ex:
            print("Error uploading score. Please try again")
            print(ex)


    def help_module(self, word) -> None:
        if word == '.SCORES':
            highscores = self.stub.GetHighscores(Player(), None)
            print(highscores)
        elif word == '.UPLOAD' or word == '.U':
            self.upload_score()
        elif word == '.HELP':
            print("If you don't know this game, we can't help you.")
        elif word == '.NEW':
            self.state = self.new_game()
        elif word == '.EXIT' or word == '.Q':
            print("Quitting...")
            # optional: save state in DB
            self.exit = False
        else:
            print('Did not recognize command; try .SCORES or .HELP')

if __name__ == '__main__':
    logging.basicConfig()
    
    player = input('Your name: ')
    gamecode = input('Join game: ')

    terminal = SBTerminal(player)
    terminal.join_game(gamecode)

    # console game loop
    terminal.loop()
