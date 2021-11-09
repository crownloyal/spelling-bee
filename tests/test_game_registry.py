#!/usr/bin/env python3

# fix pathing
import sys
sys.path.append('..')

from sb.game_registry import GameRegistry


gr = GameRegistry()

# check for rolls
letters = gr.roll_multiple_unique_letters(7)
print(letters)