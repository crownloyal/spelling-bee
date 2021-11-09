Student ID: R00145347
Name: Dominic M Brause

== Assignment 1 ==
*Course: Distributed Systems*

=Architecture:=

Classes:
SBGameServer - launches instances of SBGame and SBGameRegistry
SBGame - Interacting with SBGameRegistry as a player would
GameRegistry - Game in-memory singleton that holds current game state such as
    - letters
    - solution attempt
    - also utility such as letter rolls
optional: DatabaseManager - Persistent game state, with export option to JSON

External libraries:
oxforddictionaries HTTPS API; API keys in untracked config.py
grpcio
grpcio-tools
protobuf

*Running this madness:*
Compiling the proto definition:
> protoc -I=. --python_out=./sb ./game.proto
, or alternatively
> python3 -m grpc_tools.protoc -I . --grpc_python_out=./sb ./game.proto

Installing dependencies:
> pip3 install -r requirements.txt

launch the server:
> python3 ./sb/server.py

launch the client:
> python3 ./sb/interactive_console.py

Start playing!
