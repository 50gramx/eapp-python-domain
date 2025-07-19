from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_product_pb2 as _space_product_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.collars import DC499999994_pb2 as _DC499999994_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceProductDomain(_message.Message):
    __slots__ = ("id", "name", "description", "is_isolated", "space_product", "created_at", "last_updated_at", "dc499999994")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ISOLATED_FIELD_NUMBER: _ClassVar[int]
    SPACE_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DC499999994_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    is_isolated: bool
    space_product: _space_product_pb2.SpaceProduct
    created_at: _timestamp_pb2_1.Timestamp
    last_updated_at: _timestamp_pb2_1.Timestamp
    dc499999994: _DC499999994_pb2.DC499999994
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_isolated: bool = ..., space_product: _Optional[_Union[_space_product_pb2.SpaceProduct, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., dc499999994: _Optional[_Union[_DC499999994_pb2.DC499999994, _Mapping]] = ...) -> None: ...
