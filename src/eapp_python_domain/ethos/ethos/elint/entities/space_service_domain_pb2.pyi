from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_service_pb2 as _space_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.collars import DC500000000_pb2 as _DC500000000_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.collars import DC499999999_pb2 as _DC499999999_pb2
from ethos.elint.collars import DC499999998_pb2 as _DC499999998_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceServiceDomain(_message.Message):
    __slots__ = ("id", "name", "description", "is_isolated", "space_service", "created_at", "last_updated_at", "dc500000000", "dc499999999", "dc499999998")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ISOLATED_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DC500000000_FIELD_NUMBER: _ClassVar[int]
    DC499999999_FIELD_NUMBER: _ClassVar[int]
    DC499999998_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    is_isolated: bool
    space_service: _space_service_pb2.SpaceService
    created_at: _timestamp_pb2_1_1.Timestamp
    last_updated_at: _timestamp_pb2_1_1.Timestamp
    dc500000000: _DC500000000_pb2.DC500000000
    dc499999999: _DC499999999_pb2.DC499999999
    dc499999998: _DC499999998_pb2.DC499999998
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_isolated: bool = ..., space_service: _Optional[_Union[_space_service_pb2.SpaceService, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2_1_1.Timestamp, _Mapping]] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2_1_1.Timestamp, _Mapping]] = ..., dc500000000: _Optional[_Union[_DC500000000_pb2.DC500000000, _Mapping]] = ..., dc499999999: _Optional[_Union[_DC499999999_pb2.DC499999999, _Mapping]] = ..., dc499999998: _Optional[_Union[_DC499999998_pb2.DC499999998, _Mapping]] = ...) -> None: ...
