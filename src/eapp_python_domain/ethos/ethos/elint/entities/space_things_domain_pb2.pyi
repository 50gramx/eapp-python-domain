from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_things_pb2 as _space_things_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.collars import DC499999997_pb2 as _DC499999997_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceThingsDomain(_message.Message):
    __slots__ = ("id", "name", "description", "is_isolated", "space_things", "created_at", "last_updated_at", "dc499999997")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ISOLATED_FIELD_NUMBER: _ClassVar[int]
    SPACE_THINGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DC499999997_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    is_isolated: bool
    space_things: _space_things_pb2.SpaceThings
    created_at: _timestamp_pb2_1_1.Timestamp
    last_updated_at: _timestamp_pb2_1_1.Timestamp
    dc499999997: _DC499999997_pb2.DC499999997
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_isolated: bool = ..., space_things: _Optional[_Union[_space_things_pb2.SpaceThings, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2_1_1.Timestamp, _Mapping]] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2_1_1.Timestamp, _Mapping]] = ..., dc499999997: _Optional[_Union[_DC499999997_pb2.DC499999997, _Mapping]] = ...) -> None: ...
