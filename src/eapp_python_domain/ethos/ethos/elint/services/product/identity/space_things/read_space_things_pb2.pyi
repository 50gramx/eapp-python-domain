from ethos.elint.entities import space_things_domain_pb2 as _space_things_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.collars import DC499999997_pb2 as _DC499999997_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadThingsSpaceDomainRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ReadThingsSpaceDomainResponse(_message.Message):
    __slots__ = ("domain",)
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    domain: _space_things_domain_pb2.SpaceThingsDomain
    def __init__(self, domain: _Optional[_Union[_space_things_domain_pb2.SpaceThingsDomain, _Mapping]] = ...) -> None: ...

class ReadNodesCollarRequest(_message.Message):
    __slots__ = ("collar_id",)
    COLLAR_ID_FIELD_NUMBER: _ClassVar[int]
    collar_id: str
    def __init__(self, collar_id: _Optional[str] = ...) -> None: ...

class ReadNodesCollarResponse(_message.Message):
    __slots__ = ("collar",)
    COLLAR_FIELD_NUMBER: _ClassVar[int]
    collar: _DC499999997_pb2.DC499999997
    def __init__(self, collar: _Optional[_Union[_DC499999997_pb2.DC499999997, _Mapping]] = ...) -> None: ...
