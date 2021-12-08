#!/usr/bin/env python3

from sb_game import Player
from sb_game_registry import SBGameState

class HighScore:
    def __init__(self, player: Player, score: int) -> None:
        self.player = player
        self.score = score

class StatsServer:
    def __init__(self):
        self.leaderboard = []

    def add_to_leaderboard(self, score: HighScore) -> None:
        self.leaderboard.append(score)

    def print_stats(self) -> str:
        return str(self.leaderboard)

    def print_stats_top5(self) -> str:
        return str()


if __name__ == '__main__':
    server = StatsServer()
    server.run()