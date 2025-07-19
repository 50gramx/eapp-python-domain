from ethos.elint.entities import team_pb2 as _team_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class TeamAssistant(_message.Message):
    __slots__ = ("id", "name", "team", "created_at", "last_assisted_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ASSISTED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    team: _team_pb2.Team
    created_at: _timestamp_pb2_1.Timestamp
    last_assisted_at: _timestamp_pb2_1.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., team: _Optional[_Union[_team_pb2.Team, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., last_assisted_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class TeamAssistantConnectedAssociate(_message.Message):
    __slots__ = ("associate_connection_id", "associate_id", "connected_at")
    ASSOCIATE_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_AT_FIELD_NUMBER: _ClassVar[int]
    associate_connection_id: str
    associate_id: str
    connected_at: _timestamp_pb2_1.Timestamp
    def __init__(self, associate_connection_id: _Optional[str] = ..., associate_id: _Optional[str] = ..., connected_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...
