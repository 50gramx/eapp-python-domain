from ethos.elint.entities import space_things_domain_pb2 as _space_things_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.collars import DC499999997_pb2 as _DC499999997_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateThingsSpaceDomainRequest(_message.Message):
    __slots__ = ("name", "description", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    properties: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class UpdateThingsSpaceDomainResponse(_message.Message):
    __slots__ = ("domain",)
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    domain: _space_things_domain_pb2.SpaceThingsDomain
    def __init__(self, domain: _Optional[_Union[_space_things_domain_pb2.SpaceThingsDomain, _Mapping]] = ...) -> None: ...

class UpdateNodesCollarRequest(_message.Message):
    __slots__ = ("machine_class", "vcpu", "ram_gib")
    MACHINE_CLASS_FIELD_NUMBER: _ClassVar[int]
    VCPU_FIELD_NUMBER: _ClassVar[int]
    RAM_GIB_FIELD_NUMBER: _ClassVar[int]
    machine_class: str
    vcpu: int
    ram_gib: int
    def __init__(self, machine_class: _Optional[str] = ..., vcpu: _Optional[int] = ..., ram_gib: _Optional[int] = ...) -> None: ...

class UpdateNodesCollarResponse(_message.Message):
    __slots__ = ("collar",)
    COLLAR_FIELD_NUMBER: _ClassVar[int]
    collar: _DC499999997_pb2.DC499999997
    def __init__(self, collar: _Optional[_Union[_DC499999997_pb2.DC499999997, _Mapping]] = ...) -> None: ...
