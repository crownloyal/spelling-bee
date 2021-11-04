Student ID: R00145347
Name: Dominic M Brause

== Assignment 1 ==
*Course: Distributed Systems*

=Architecture:=

Classes: 
SBGame - Game logic
GameRegistry - Game in-memory singleton
DatabaseManager - Persistent game state, with export option to JSON
Player 

External

*Running this madness:*
Compiling the proto definition:
> protoc -I=. --python_out=./sb ./gam
e.proto
, or alternatively
> python3 -m grpc_tools.protoc -I . -
-grpc_python_out=./sb ./game.proto

launch the server:
> python3 ./sb/server.py

launch the client:
> python3 ./sb/interactive_console.py

Start playing!