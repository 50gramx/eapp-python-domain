from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import universe_pb2 as _universe_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import galaxy_pb2 as _galaxy_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateGalaxyRequest(_message.Message):
    __slots__ = ("galaxy_id", "galaxy_name", "universe", "domain", "galaxy_description")
    GALAXY_ID_FIELD_NUMBER: _ClassVar[int]
    GALAXY_NAME_FIELD_NUMBER: _ClassVar[int]
    UNIVERSE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    GALAXY_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    galaxy_id: str
    galaxy_name: str
    universe: _universe_pb2.Universe
    domain: str
    galaxy_description: str
    def __init__(self, galaxy_id: _Optional[str] = ..., galaxy_name: _Optional[str] = ..., universe: _Optional[_Union[_universe_pb2.Universe, _Mapping]] = ..., domain: _Optional[str] = ..., galaxy_description: _Optional[str] = ...) -> None: ...

class UpdateGalaxyResponse(_message.Message):
    __slots__ = ("galaxy",)
    GALAXY_FIELD_NUMBER: _ClassVar[int]
    galaxy: _galaxy_pb2.Galaxy
    def __init__(self, galaxy: _Optional[_Union[_galaxy_pb2.Galaxy, _Mapping]] = ...) -> None: ...
