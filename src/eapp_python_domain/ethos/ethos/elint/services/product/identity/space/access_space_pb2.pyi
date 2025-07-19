from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_pb2 as _space_pb2
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from ethos.elint.services.product.identity.account_assistant import access_account_assistant_pb2 as _access_account_assistant_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceAccessTokenResponse(_message.Message):
    __slots__ = ("space_services_access_auth_details", "space_services_access_done", "space_services_access_message")
    SPACE_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICES_ACCESS_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICES_ACCESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_services_access_auth_details: SpaceServicesAccessAuthDetails
    space_services_access_done: bool
    space_services_access_message: str
    def __init__(self, space_services_access_auth_details: _Optional[_Union[SpaceServicesAccessAuthDetails, _Mapping]] = ..., space_services_access_done: bool = ..., space_services_access_message: _Optional[str] = ...) -> None: ...

class ValidateSpaceServicesResponse(_message.Message):
    __slots__ = ("space_service_access_validation_done", "space_service_access_validation_message")
    SPACE_SERVICE_ACCESS_VALIDATION_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICE_ACCESS_VALIDATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_service_access_validation_done: bool
    space_service_access_validation_message: str
    def __init__(self, space_service_access_validation_done: bool = ..., space_service_access_validation_message: _Optional[str] = ...) -> None: ...

class SpaceServicesAccessAuthDetails(_message.Message):
    __slots__ = ("space", "space_services_access_session_token_details", "requested_at")
    SPACE_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICES_ACCESS_SESSION_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    space: _space_pb2.Space
    space_services_access_session_token_details: _generic_pb2.PersistentSessionTokenDetails
    requested_at: _timestamp_pb2.Timestamp
    def __init__(self, space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., space_services_access_session_token_details: _Optional[_Union[_generic_pb2.PersistentSessionTokenDetails, _Mapping]] = ..., requested_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
