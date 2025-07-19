from ethos.elint.entities import universe_pb2 as _universe_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUniverseRequest(_message.Message):
    __slots__ = ("universe_name", "universe_description")
    UNIVERSE_NAME_FIELD_NUMBER: _ClassVar[int]
    UNIVERSE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    universe_name: str
    universe_description: str
    def __init__(self, universe_name: _Optional[str] = ..., universe_description: _Optional[str] = ...) -> None: ...

class CreateUniverseResponse(_message.Message):
    __slots__ = ("universe_name", "universe_created_at", "universe_description", "universe_updated_at")
    UNIVERSE_NAME_FIELD_NUMBER: _ClassVar[int]
    UNIVERSE_CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UNIVERSE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNIVERSE_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    universe_name: str
    universe_created_at: _timestamp_pb2_1.Timestamp
    universe_description: str
    universe_updated_at: _timestamp_pb2_1.Timestamp
    def __init__(self, universe_name: _Optional[str] = ..., universe_created_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., universe_description: _Optional[str] = ..., universe_updated_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...
