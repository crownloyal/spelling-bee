Student ID: R00145347
Name: Dominic M Brause

== Assignment 1 ==
*Course: Distributed Systems*

=Architecture:=

Classes and Modules:
SBGameServer - launches instances of SBGame and SBGameRegistry

SBGame - Interacting with SBGameRegistry as a player would

SBGameRegistry - Game in-memory singleton that holds current game state such as
    - letters
    - solution attempt
This is a singleton to have multiple clients interact with the same instance instead of spawning a new instance for each 


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

*Running this madness:*
Compiling the proto definition:
> protoc -I=. --python_out=./sb ./game.proto
, or alternatively
> python3 -m grpc_tools.protoc -I . --grpc_python_out=./sb --python_out=./sb ./game.proto

launch the server:
> python3 ./sb/debug-sbserver.py

launch the client:
> python3 ./sb/interactive_console.py

Start playing!

== Available commands ==
.new
Starts a new game with scores reset

.scores
Returns the player name and highest score (in-memory only)

.help
Doesn't really try to help

.exit or .q
closes the interactive console