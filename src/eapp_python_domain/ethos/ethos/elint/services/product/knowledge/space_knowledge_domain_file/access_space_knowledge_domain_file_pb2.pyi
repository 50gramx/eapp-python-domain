from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_knowledge_domain_file_pb2 as _space_knowledge_domain_file_pb2
from ethos.elint.services.product.knowledge.space_knowledge_domain import access_space_knowledge_domain_pb2 as _access_space_knowledge_domain_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceKnowledgeDomainFileAccessTokenRequest(_message.Message):
    __slots__ = ("space_knowledge_domain_services_access_auth_details", "space_knowledge_domain_file")
    SPACE_KNOWLEDGE_DOMAIN_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_services_access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    space_knowledge_domain_file: _space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile
    def __init__(self, space_knowledge_domain_services_access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file: _Optional[_Union[_space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile, _Mapping]] = ...) -> None: ...

class SpaceKnowledgeDomainFileAccessTokenResponse(_message.Message):
    __slots__ = ("space_knowledge_domain_file_services_access_auth_details", "space_knowledge_domain_file_services_access_done", "space_knowledge_domain_file_services_access_message")
    SPACE_KNOWLEDGE_DOMAIN_FILE_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_SERVICES_ACCESS_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_SERVICES_ACCESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_services_access_auth_details: SpaceKnowledgeDomainFileServicesAccessAuthDetails
    space_knowledge_domain_file_services_access_done: bool
    space_knowledge_domain_file_services_access_message: str
    def __init__(self, space_knowledge_domain_file_services_access_auth_details: _Optional[_Union[SpaceKnowledgeDomainFileServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file_services_access_done: bool = ..., space_knowledge_domain_file_services_access_message: _Optional[str] = ...) -> None: ...

class ValidateSpaceKnowledgeDomainFileServicesResponse(_message.Message):
    __slots__ = ("space_knowledge_domain_file_services_access_validation_done", "space_knowledge_domain_file_services_access_validation_message")
    SPACE_KNOWLEDGE_DOMAIN_FILE_SERVICES_ACCESS_VALIDATION_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_SERVICES_ACCESS_VALIDATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_services_access_validation_done: bool
    space_knowledge_domain_file_services_access_validation_message: str
    def __init__(self, space_knowledge_domain_file_services_access_validation_done: bool = ..., space_knowledge_domain_file_services_access_validation_message: _Optional[str] = ...) -> None: ...

class SpaceKnowledgeDomainFileServicesAccessAuthDetails(_message.Message):
    __slots__ = ("space_knowledge_domain_file", "space_knowledge_domain_file_services_access_session_token_details", "requested_at")
    SPACE_KNOWLEDGE_DOMAIN_FILE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_SERVICES_ACCESS_SESSION_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file: _space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile
    space_knowledge_domain_file_services_access_session_token_details: _generic_pb2.PersistentSessionTokenDetails
    requested_at: _timestamp_pb2_1.Timestamp
    def __init__(self, space_knowledge_domain_file: _Optional[_Union[_space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile, _Mapping]] = ..., space_knowledge_domain_file_services_access_session_token_details: _Optional[_Union[_generic_pb2.PersistentSessionTokenDetails, _Mapping]] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...
