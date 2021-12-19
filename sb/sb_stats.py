#!/usr/bin/env python3

import time
import threading
from sb_socket import SocketServerMixin
from sb_game_registry import SBGameState

class StatsServer(SocketServerMixin):
    def __init__(self):
        super().__init__()
        self.leaderboard = []
        looper = threading.Thread(target=self.listen_loop)
        looper.start()

    def add_to_leaderboard(self, data: SBGameState) -> None:
        self.leaderboard.append((data.players, data.score))

    def print_stats(self) -> str:
        print(self.leaderboard)

    def print_stats_top5(self) -> str:
        return 

    def listen(self):
        clientsocket, address = self.socket_server.accept()
        print(f"INFO: Connection from {address} has been established")
        self.clients_active[address] = {}
        self.clients_active[address]["socket"] = clientsocket
        self.clients_active[address]["visited"] = False

    def listen_loop(self):
        while True:
            self.listen()
            working_copy = dict(self.clients_active)
            if len(working_copy) <= 0:
                time.sleep(5)
                continue # Let's keep the console spam at a minimum

            for client_id in working_copy:
                print(f"INFO: Attempting connection to {client_id}")                
                if self.clients_active[client_id]["visited"] == False:
                    self.clients_active[client_id]["visited"] = True
                    data = self.sock_receive_message(self.clients_active[client_id]["socket"])
                    self.add_to_leaderboard(data)
                
                # if self.clients_active[client_id]["visited"] == True:
                #     del self.clients_active[client_id]
                # Multi-RPC needs some management, not this time
                
            self.print_stats()
            time.sleep(5)

if __name__ == '__main__':
    server = StatsServer()