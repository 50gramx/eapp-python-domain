from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import machine_pb2 as _machine_pb2
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListAllMachinesResponse(_message.Message):
    __slots__ = ("machines", "response_meta")
    MACHINES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    machines: _containers.RepeatedCompositeFieldContainer[_machine_pb2.Machine]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, machines: _Optional[_Iterable[_Union[_machine_pb2.Machine, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...
