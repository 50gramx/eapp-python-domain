from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.services.product.identity.space import access_space_pb2 as _access_space_pb2
from ethos.elint.services.product.service.space_service import access_space_service_pb2 as _access_space_service_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAccountSpaceServiceRequest(_message.Message):
    __slots__ = ("space_service_access_auth_details", "space_service_name", "requested_at")
    SPACE_SERVICE_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    space_service_access_auth_details: _access_space_pb2.SpaceServicesAccessAuthDetails
    space_service_name: str
    requested_at: _timestamp_pb2.Timestamp
    def __init__(self, space_service_access_auth_details: _Optional[_Union[_access_space_pb2.SpaceServicesAccessAuthDetails, _Mapping]] = ..., space_service_name: _Optional[str] = ..., requested_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateAccountSpaceServiceResponse(_message.Message):
    __slots__ = ("space_service_services_access_auth_details", "create_account_space_service_done", "create_account_space_service_message")
    SPACE_SERVICE_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_ACCOUNT_SPACE_SERVICE_DONE_FIELD_NUMBER: _ClassVar[int]
    CREATE_ACCOUNT_SPACE_SERVICE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_service_services_access_auth_details: _access_space_service_pb2.SpaceServiceServicesAccessAuthDetails
    create_account_space_service_done: bool
    create_account_space_service_message: str
    def __init__(self, space_service_services_access_auth_details: _Optional[_Union[_access_space_service_pb2.SpaceServiceServicesAccessAuthDetails, _Mapping]] = ..., create_account_space_service_done: bool = ..., create_account_space_service_message: _Optional[str] = ...) -> None: ...
