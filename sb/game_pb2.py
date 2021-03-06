# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='sb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ngame.proto\x12\x02sb\"3\n\x06Player\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07session\x18\x03 \x01(\x05\"<\n\x07\x41ttempt\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x10\n\x08gamecode\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x05\"w\n\x11\x41ttemptEvaluation\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x0c\n\x04word\x18\x02 \x01(\t\x12\x0e\n\x06points\x18\x03 \x01(\x05\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x11\n\tattemptId\x18\x05 \x01(\t\x12\x0f\n\x07message\x18\x06 \x01(\t\"3\n\x0cStateRequest\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x10\n\x08gamecode\x18\x02 \x01(\t\"\xe1\x01\n\x0bSBGameState\x12\x0f\n\x07players\x18\x01 \x03(\t\x12\x0e\n\x06gameId\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x05\x12\x10\n\x08\x61ttempts\x18\x04 \x01(\x05\x12\x10\n\x08wordlist\x18\x05 \x03(\t\x12\x11\n\tcreatedAt\x18\x06 \x01(\t\x12\x12\n\nlastUpdate\x18\x07 \x01(\t\x12\r\n\x05\x65rror\x18\x08 \x01(\x08\x12\x14\n\x0c\x65rrorMessage\x18\t \x01(\t\x12\x0f\n\x07letters\x18\n \x03(\t\x12\x0f\n\x07matches\x18\x0b \x03(\t\x12\x10\n\x08gamecode\x18\x0c \x01(\t\"`\n\x0cSBHighScores\x12\x0e\n\x06player\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x03\x12\x0f\n\x07game_id\x18\x03 \x01(\x03\x12\x0f\n\x07letters\x18\x04 \x03(\t\x12\x0f\n\x07matches\x18\x05 \x03(\t\"8\n\x0eNewGameRequest\x12\x13\n\x0b\x61\x64minPlayer\x18\x01 \x01(\t\x12\x11\n\tadminUUID\x18\x02 \x01(\t\"L\n\x0cGameResponse\x12\x15\n\ractivePlayers\x18\x01 \x01(\x05\x12\x13\n\x0buserSession\x18\x02 \x01(\t\x12\x10\n\x08gamecode\x18\x03 \x01(\t\"J\n\x0fJoinGameRequest\x12\x10\n\x08gamecode\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x13\n\x0buserSession\x18\x03 \x01(\t2\xcf\x02\n\rSBGameService\x12\x33\n\nCreateGame\x12\x12.sb.NewGameRequest\x1a\x0f.sb.SBGameState\"\x00\x12\x34\n\x0c\x41ttemptGuess\x12\x0b.sb.Attempt\x1a\x15.sb.AttemptEvaluation\"\x00\x12\x35\n\x0eGetSBGameState\x12\x10.sb.StateRequest\x1a\x0f.sb.SBGameState\"\x00\x12/\n\rGetHighscores\x12\n.sb.Player\x1a\x10.sb.SBHighScores\"\x00\x12\x37\n\rAddUserToGame\x12\x13.sb.JoinGameRequest\x1a\x0f.sb.SBGameState\"\x00\x12\x32\n\x0bUploadScore\x12\x10.sb.StateRequest\x1a\x0f.sb.SBGameState\"\x00\x62\x06proto3'
)




_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='sb.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sb.Player.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='sb.Player.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session', full_name='sb.Player.session', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=69,
)


_ATTEMPT = _descriptor.Descriptor(
  name='Attempt',
  full_name='sb.Attempt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='sb.Attempt.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gamecode', full_name='sb.Attempt.gamecode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sb.Attempt.timestamp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=131,
)


_ATTEMPTEVALUATION = _descriptor.Descriptor(
  name='AttemptEvaluation',
  full_name='sb.AttemptEvaluation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid', full_name='sb.AttemptEvaluation.valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='word', full_name='sb.AttemptEvaluation.word', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='points', full_name='sb.AttemptEvaluation.points', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sb.AttemptEvaluation.timestamp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attemptId', full_name='sb.AttemptEvaluation.attemptId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='sb.AttemptEvaluation.message', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=252,
)


_STATEREQUEST = _descriptor.Descriptor(
  name='StateRequest',
  full_name='sb.StateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sb.StateRequest.timestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gamecode', full_name='sb.StateRequest.gamecode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=305,
)


_SBGAMESTATE = _descriptor.Descriptor(
  name='SBGameState',
  full_name='sb.SBGameState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='players', full_name='sb.SBGameState.players', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gameId', full_name='sb.SBGameState.gameId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='sb.SBGameState.score', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attempts', full_name='sb.SBGameState.attempts', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wordlist', full_name='sb.SBGameState.wordlist', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createdAt', full_name='sb.SBGameState.createdAt', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastUpdate', full_name='sb.SBGameState.lastUpdate', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='sb.SBGameState.error', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errorMessage', full_name='sb.SBGameState.errorMessage', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='letters', full_name='sb.SBGameState.letters', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matches', full_name='sb.SBGameState.matches', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gamecode', full_name='sb.SBGameState.gamecode', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=533,
)


_SBHIGHSCORES = _descriptor.Descriptor(
  name='SBHighScores',
  full_name='sb.SBHighScores',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='sb.SBHighScores.player', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='sb.SBHighScores.score', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='game_id', full_name='sb.SBHighScores.game_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='letters', full_name='sb.SBHighScores.letters', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matches', full_name='sb.SBHighScores.matches', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=631,
)


_NEWGAMEREQUEST = _descriptor.Descriptor(
  name='NewGameRequest',
  full_name='sb.NewGameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adminPlayer', full_name='sb.NewGameRequest.adminPlayer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adminUUID', full_name='sb.NewGameRequest.adminUUID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=633,
  serialized_end=689,
)


_GAMERESPONSE = _descriptor.Descriptor(
  name='GameResponse',
  full_name='sb.GameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activePlayers', full_name='sb.GameResponse.activePlayers', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userSession', full_name='sb.GameResponse.userSession', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gamecode', full_name='sb.GameResponse.gamecode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=691,
  serialized_end=767,
)


_JOINGAMEREQUEST = _descriptor.Descriptor(
  name='JoinGameRequest',
  full_name='sb.JoinGameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gamecode', full_name='sb.JoinGameRequest.gamecode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='sb.JoinGameRequest.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userSession', full_name='sb.JoinGameRequest.userSession', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=769,
  serialized_end=843,
)

DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['Attempt'] = _ATTEMPT
DESCRIPTOR.message_types_by_name['AttemptEvaluation'] = _ATTEMPTEVALUATION
DESCRIPTOR.message_types_by_name['StateRequest'] = _STATEREQUEST
DESCRIPTOR.message_types_by_name['SBGameState'] = _SBGAMESTATE
DESCRIPTOR.message_types_by_name['SBHighScores'] = _SBHIGHSCORES
DESCRIPTOR.message_types_by_name['NewGameRequest'] = _NEWGAMEREQUEST
DESCRIPTOR.message_types_by_name['GameResponse'] = _GAMERESPONSE
DESCRIPTOR.message_types_by_name['JoinGameRequest'] = _JOINGAMEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:sb.Player)
  })
_sym_db.RegisterMessage(Player)

Attempt = _reflection.GeneratedProtocolMessageType('Attempt', (_message.Message,), {
  'DESCRIPTOR' : _ATTEMPT,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:sb.Attempt)
  })
_sym_db.RegisterMessage(Attempt)

AttemptEvaluation = _reflection.GeneratedProtocolMessageType('AttemptEvaluation', (_message.Message,), {
  'DESCRIPTOR' : _ATTEMPTEVALUATION,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:sb.AttemptEvaluation)
  })
_sym_db.RegisterMessage(AttemptEvaluation)

StateRequest = _reflection.GeneratedProtocolMessageType('StateRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATEREQUEST,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:sb.StateRequest)
  })
_sym_db.RegisterMessage(StateRequest)

SBGameState = _reflection.GeneratedProtocolMessageType('SBGameState', (_message.Message,), {
  'DESCRIPTOR' : _SBGAMESTATE,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:sb.SBGameState)
  })
_sym_db.RegisterMessage(SBGameState)

SBHighScores = _reflection.GeneratedProtocolMessageType('SBHighScores', (_message.Message,), {
  'DESCRIPTOR' : _SBHIGHSCORES,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:sb.SBHighScores)
  })
_sym_db.RegisterMessage(SBHighScores)

NewGameRequest = _reflection.GeneratedProtocolMessageType('NewGameRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWGAMEREQUEST,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:sb.NewGameRequest)
  })
_sym_db.RegisterMessage(NewGameRequest)

GameResponse = _reflection.GeneratedProtocolMessageType('GameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GAMERESPONSE,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:sb.GameResponse)
  })
_sym_db.RegisterMessage(GameResponse)

JoinGameRequest = _reflection.GeneratedProtocolMessageType('JoinGameRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOINGAMEREQUEST,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:sb.JoinGameRequest)
  })
_sym_db.RegisterMessage(JoinGameRequest)



_SBGAMESERVICE = _descriptor.ServiceDescriptor(
  name='SBGameService',
  full_name='sb.SBGameService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=846,
  serialized_end=1181,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateGame',
    full_name='sb.SBGameService.CreateGame',
    index=0,
    containing_service=None,
    input_type=_NEWGAMEREQUEST,
    output_type=_SBGAMESTATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AttemptGuess',
    full_name='sb.SBGameService.AttemptGuess',
    index=1,
    containing_service=None,
    input_type=_ATTEMPT,
    output_type=_ATTEMPTEVALUATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSBGameState',
    full_name='sb.SBGameService.GetSBGameState',
    index=2,
    containing_service=None,
    input_type=_STATEREQUEST,
    output_type=_SBGAMESTATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetHighscores',
    full_name='sb.SBGameService.GetHighscores',
    index=3,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_SBHIGHSCORES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddUserToGame',
    full_name='sb.SBGameService.AddUserToGame',
    index=4,
    containing_service=None,
    input_type=_JOINGAMEREQUEST,
    output_type=_SBGAMESTATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UploadScore',
    full_name='sb.SBGameService.UploadScore',
    index=5,
    containing_service=None,
    input_type=_STATEREQUEST,
    output_type=_SBGAMESTATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SBGAMESERVICE)

DESCRIPTOR.services_by_name['SBGameService'] = _SBGAMESERVICE

# @@protoc_insertion_point(module_scope)
