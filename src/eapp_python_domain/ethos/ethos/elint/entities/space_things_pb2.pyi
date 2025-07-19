from ethos.elint.entities import space_pb2 as _space_pb2
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceThings(_message.Message):
    __slots__ = ("name", "id", "admin", "space", "created_at")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    admin: _account_pb2.Account
    space: _space_pb2.Space
    created_at: _timestamp_pb2_1.Timestamp
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., admin: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...
