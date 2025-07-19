from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_product_domain_pb2 as _space_product_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.services.product.product.space_product import access_space_product_pb2 as _access_space_product_pb2
from ethos.elint.services.product.product.space_product_domain import access_space_product_domain_pb2 as _access_space_product_domain_pb2
from ethos.elint.collars import DC499999994_pb2 as _DC499999994_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDC499999994SPDRequest(_message.Message):
    __slots__ = ("auth", "name", "description", "is_isolated", "dc499999994")
    AUTH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ISOLATED_FIELD_NUMBER: _ClassVar[int]
    DC499999994_FIELD_NUMBER: _ClassVar[int]
    auth: _access_space_product_pb2.SpaceProductServicesAccessAuthDetails
    name: str
    description: str
    is_isolated: bool
    dc499999994: _DC499999994_pb2.DC499999994
    def __init__(self, auth: _Optional[_Union[_access_space_product_pb2.SpaceProductServicesAccessAuthDetails, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_isolated: bool = ..., dc499999994: _Optional[_Union[_DC499999994_pb2.DC499999994, _Mapping]] = ...) -> None: ...
