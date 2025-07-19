from ethos.elint.entities import space_pb2 as _space_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceService(_message.Message):
    __slots__ = ("space_service_name", "space_service_id", "space_service_admin_account_id", "space", "created_at")
    SPACE_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICE_ADMIN_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    space_service_name: str
    space_service_id: str
    space_service_admin_account_id: str
    space: _space_pb2.Space
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, space_service_name: _Optional[str] = ..., space_service_id: _Optional[str] = ..., space_service_admin_account_id: _Optional[str] = ..., space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
