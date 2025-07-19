from ethos.elint.entities import space_things_domain_pb2 as _space_things_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.collars import DC499999997_pb2 as _DC499999997_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteThingsSpaceDomainRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteThingsSpaceDomainResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class DeleteNodesCollarRequest(_message.Message):
    __slots__ = ("machine_class",)
    MACHINE_CLASS_FIELD_NUMBER: _ClassVar[int]
    machine_class: str
    def __init__(self, machine_class: _Optional[str] = ...) -> None: ...

class DeleteNodesCollarResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
