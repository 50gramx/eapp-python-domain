from ethos.elint.entities import space_pb2 as _space_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceProduct(_message.Message):
    __slots__ = ("space_product_name", "space_product_id", "space_product_admin_account_id", "space", "created_at")
    SPACE_PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    SPACE_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_PRODUCT_ADMIN_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    space_product_name: str
    space_product_id: str
    space_product_admin_account_id: str
    space: _space_pb2.Space
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, space_product_name: _Optional[str] = ..., space_product_id: _Optional[str] = ..., space_product_admin_account_id: _Optional[str] = ..., space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
