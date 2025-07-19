from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.services.product.identity.space import access_space_pb2 as _access_space_pb2
from ethos.elint.services.product.product.space_product import access_space_product_pb2 as _access_space_product_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAccountSpaceProductRequest(_message.Message):
    __slots__ = ("space_services_access_auth_details", "space_product_name", "requested_at")
    SPACE_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    space_services_access_auth_details: _access_space_pb2.SpaceServicesAccessAuthDetails
    space_product_name: str
    requested_at: _timestamp_pb2.Timestamp
    def __init__(self, space_services_access_auth_details: _Optional[_Union[_access_space_pb2.SpaceServicesAccessAuthDetails, _Mapping]] = ..., space_product_name: _Optional[str] = ..., requested_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateAccountSpaceProductResponse(_message.Message):
    __slots__ = ("space_product_services_access_auth_details", "create_account_space_product_done", "create_account_space_product_message")
    SPACE_PRODUCT_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_ACCOUNT_SPACE_PRODUCT_DONE_FIELD_NUMBER: _ClassVar[int]
    CREATE_ACCOUNT_SPACE_PRODUCT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_product_services_access_auth_details: _access_space_product_pb2.SpaceProductServicesAccessAuthDetails
    create_account_space_product_done: bool
    create_account_space_product_message: str
    def __init__(self, space_product_services_access_auth_details: _Optional[_Union[_access_space_product_pb2.SpaceProductServicesAccessAuthDetails, _Mapping]] = ..., create_account_space_product_done: bool = ..., create_account_space_product_message: _Optional[str] = ...) -> None: ...
