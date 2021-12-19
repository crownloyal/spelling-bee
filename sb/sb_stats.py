#!/usr/bin/env python3

import threading
from sb_socket import SocketServerMixin
from sb_game_registry import SBGameState

class StatsServer(SocketServerMixin):
    def __init__(self):
        super().__init__()
        self.leaderboard = []
        self.listen_loop()

    def add_to_leaderboard(self, data: SBGameState) -> None:
        self.leaderboard.append(data.score)

    def print_stats(self) -> str:
        print(self.leaderboard)

    def print_stats_top5(self) -> str:
        return 

    def listen_loop(self):
        self.listen()
        while True:
            for clientid in self.clients_active:
                print(f"INFO: Attempting connection to {clientid}")
                print(f"INFO: {self.clients_active[clientid]}")
                data = self.sock_receive_message(self.clients_active[clientid])
                self.add_to_leaderboard(data)
            self.clients_active.clear()
            self.print_stats()

if __name__ == '__main__':
    server = StatsServer()