from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_service_domain_pb2 as _space_service_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.services.product.service.space_service import access_space_service_pb2 as _access_space_service_pb2
from ethos.elint.collars import DC499999998_pb2 as _DC499999998_pb2
from ethos.elint.collars import DC499999999_pb2 as _DC499999999_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDC499999998SSDRequest(_message.Message):
    __slots__ = ("auth", "name", "description", "is_isolated", "dc499999998")
    AUTH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ISOLATED_FIELD_NUMBER: _ClassVar[int]
    DC499999998_FIELD_NUMBER: _ClassVar[int]
    auth: _access_space_service_pb2.SpaceServiceServicesAccessAuthDetails
    name: str
    description: str
    is_isolated: bool
    dc499999998: _DC499999998_pb2.DC499999998
    def __init__(self, auth: _Optional[_Union[_access_space_service_pb2.SpaceServiceServicesAccessAuthDetails, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_isolated: bool = ..., dc499999998: _Optional[_Union[_DC499999998_pb2.DC499999998, _Mapping]] = ...) -> None: ...

class CreateDC499999999SSDRequest(_message.Message):
    __slots__ = ("auth", "name", "description", "is_isolated", "dc499999999")
    AUTH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ISOLATED_FIELD_NUMBER: _ClassVar[int]
    DC499999999_FIELD_NUMBER: _ClassVar[int]
    auth: _access_space_service_pb2.SpaceServiceServicesAccessAuthDetails
    name: str
    description: str
    is_isolated: bool
    dc499999999: _DC499999999_pb2.DC499999999
    def __init__(self, auth: _Optional[_Union[_access_space_service_pb2.SpaceServiceServicesAccessAuthDetails, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_isolated: bool = ..., dc499999999: _Optional[_Union[_DC499999999_pb2.DC499999999, _Mapping]] = ...) -> None: ...
