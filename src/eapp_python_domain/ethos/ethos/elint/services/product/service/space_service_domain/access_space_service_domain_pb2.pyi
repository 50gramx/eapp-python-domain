from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_service_domain_pb2 as _space_service_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.service.space_service import access_space_service_pb2 as _access_space_service_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceServiceDomainAccessTokenRequest(_message.Message):
    __slots__ = ("space_service_services_access_auth_details", "space_service_domain")
    SPACE_SERVICE_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    space_service_services_access_auth_details: _access_space_service_pb2.SpaceServiceServicesAccessAuthDetails
    space_service_domain: _space_service_domain_pb2.SpaceServiceDomain
    def __init__(self, space_service_services_access_auth_details: _Optional[_Union[_access_space_service_pb2.SpaceServiceServicesAccessAuthDetails, _Mapping]] = ..., space_service_domain: _Optional[_Union[_space_service_domain_pb2.SpaceServiceDomain, _Mapping]] = ...) -> None: ...

class SpaceServiceDomainAccessTokenResponse(_message.Message):
    __slots__ = ("space_service_domain_services_access_auth_details", "space_service_domain_services_access_done", "space_service_domain_services_access_message")
    SPACE_SERVICE_DOMAIN_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICE_DOMAIN_SERVICES_ACCESS_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICE_DOMAIN_SERVICES_ACCESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_service_domain_services_access_auth_details: SpaceServiceDomainServicesAccessAuthDetails
    space_service_domain_services_access_done: bool
    space_service_domain_services_access_message: str
    def __init__(self, space_service_domain_services_access_auth_details: _Optional[_Union[SpaceServiceDomainServicesAccessAuthDetails, _Mapping]] = ..., space_service_domain_services_access_done: bool = ..., space_service_domain_services_access_message: _Optional[str] = ...) -> None: ...

class ValidateSpaceServiceDomainServicesResponse(_message.Message):
    __slots__ = ("space_service_domain_services_access_validation_done", "space_service_domain_services_access_validation_message")
    SPACE_SERVICE_DOMAIN_SERVICES_ACCESS_VALIDATION_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICE_DOMAIN_SERVICES_ACCESS_VALIDATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_service_domain_services_access_validation_done: bool
    space_service_domain_services_access_validation_message: str
    def __init__(self, space_service_domain_services_access_validation_done: bool = ..., space_service_domain_services_access_validation_message: _Optional[str] = ...) -> None: ...

class SpaceServiceDomainServicesAccessAuthDetails(_message.Message):
    __slots__ = ("space_service_domain", "space_service_domain_services_access_session_token_details", "requested_at")
    SPACE_SERVICE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICE_DOMAIN_SERVICES_ACCESS_SESSION_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    space_service_domain: _space_service_domain_pb2.SpaceServiceDomain
    space_service_domain_services_access_session_token_details: _generic_pb2.PersistentSessionTokenDetails
    requested_at: _timestamp_pb2_1.Timestamp
    def __init__(self, space_service_domain: _Optional[_Union[_space_service_domain_pb2.SpaceServiceDomain, _Mapping]] = ..., space_service_domain_services_access_session_token_details: _Optional[_Union[_generic_pb2.PersistentSessionTokenDetails, _Mapping]] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...
