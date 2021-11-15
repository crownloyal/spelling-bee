Student ID: R00145347
Name: Dominic M Brause

== Assignment 1 ==
*Course: Distributed Systems*

=Architecture:=

Classes and Modules:
SBGameServer/debug-sbserver - launches instances of SBGame and SBGameRegistry, and pulls them together for a working spelling bee game
Also launches grpc server

SBGame - Interacting with SBGameRegistry as a player would
Sets up connection to the oxford dictionary api

SBGameRegistry - Game in-memory singleton that holds current game state such as
    - letters
    - solution attempt
This is a *singleton* to have multiple clients interact with the same instance instead of spawning a new instance for each 

Config files and utility such as API keys and constats are stored in 
config and config_game respectively

optional: DatabaseManager - Persistent game state, with export option to JSON

External libraries:
oxforddictionaries HTTPS API; API keys in untracked config.py
grpcio
grpcio-tools
protobuf

Installing above dependencies:
> pip3 install -r requirements.txt

*Running:*
Compiling the proto definition:
> protoc -I=. --python_out=./sb ./game.proto
, or alternatively
> python3 -m grpc_tools.protoc -I . --grpc_python_out=./sb --python_out=./sb ./game.proto

launch the server:
> python3 ./sb/sb_server.py

launch the client:
> python3 ./sb/interactive_console.py

Start playing!

== Available commands ==
.new
Starts a new game with scores reset
This is especially useful if RNG decides to give you no vowels

.scores
Returns the player name and highest score (in-memory only)

.help
Doesn't really try to help

.exit or .q
closes the interactive console

GRPC is being used (as per proto file):
- Transmit current game state from server to client
- Transmit word/attempt from client to server
- Transmit evaluation of word/attempt from server to client
- Transmit current highscore stats

Improvement opportunities:
- Multiplayer (coop or battle)
- Time limit
- Data persistence
- streaming highscores (top 5)


Note:
Depending on the env, I ran into issues importing standard libs like request or ABC; ensuring correct chmod permission on the /usr/ folders seems to fix it