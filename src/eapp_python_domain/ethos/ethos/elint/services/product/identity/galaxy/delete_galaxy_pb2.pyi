from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import universe_pb2 as _universe_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import galaxy_pb2 as _galaxy_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteGalaxyRequest(_message.Message):
    __slots__ = ("galaxy_id",)
    GALAXY_ID_FIELD_NUMBER: _ClassVar[int]
    galaxy_id: str
    def __init__(self, galaxy_id: _Optional[str] = ...) -> None: ...

class DeleteGalaxyResponse(_message.Message):
    __slots__ = ("success", "galaxy")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    GALAXY_FIELD_NUMBER: _ClassVar[int]
    success: bool
    galaxy: _galaxy_pb2.Galaxy
    def __init__(self, success: bool = ..., galaxy: _Optional[_Union[_galaxy_pb2.Galaxy, _Mapping]] = ...) -> None: ...
