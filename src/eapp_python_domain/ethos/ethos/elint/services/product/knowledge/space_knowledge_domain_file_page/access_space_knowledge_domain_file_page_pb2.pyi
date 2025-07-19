from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_file_page_pb2 as _space_knowledge_domain_file_page_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.knowledge.space_knowledge_domain_file import access_space_knowledge_domain_file_pb2 as _access_space_knowledge_domain_file_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceKnowledgeDomainFilePageAccessTokenRequest(_message.Message):
    __slots__ = ("space_knowledge_domain_file_services_access_auth_details", "space_knowledge_domain_file_page")
    SPACE_KNOWLEDGE_DOMAIN_FILE_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_services_access_auth_details: _access_space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFileServicesAccessAuthDetails
    space_knowledge_domain_file_page: _space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage
    def __init__(self, space_knowledge_domain_file_services_access_auth_details: _Optional[_Union[_access_space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFileServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file_page: _Optional[_Union[_space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage, _Mapping]] = ...) -> None: ...

class SpaceKnowledgeDomainFilePageAccessTokenResponse(_message.Message):
    __slots__ = ("access_auth_details", "access_done", "access_message")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_DONE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: SpaceKnowledgeDomainFilePageServicesAccessAuthDetails
    access_done: bool
    access_message: str
    def __init__(self, access_auth_details: _Optional[_Union[SpaceKnowledgeDomainFilePageServicesAccessAuthDetails, _Mapping]] = ..., access_done: bool = ..., access_message: _Optional[str] = ...) -> None: ...

class ValidateSpaceKnowledgeDomainFilePageServicesResponse(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page_services_access_validation_done", "space_knowledge_domain_file_page_services_access_validation_message")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_SERVICES_ACCESS_VALIDATION_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_SERVICES_ACCESS_VALIDATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page_services_access_validation_done: bool
    space_knowledge_domain_file_page_services_access_validation_message: str
    def __init__(self, space_knowledge_domain_file_page_services_access_validation_done: bool = ..., space_knowledge_domain_file_page_services_access_validation_message: _Optional[str] = ...) -> None: ...

class SpaceKnowledgeDomainFilePageServicesAccessAuthDetails(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page", "space_knowledge_domain_file_page_services_access_session_token_details", "requested_at")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_SERVICES_ACCESS_SESSION_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page: _space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage
    space_knowledge_domain_file_page_services_access_session_token_details: _generic_pb2.PersistentSessionTokenDetails
    requested_at: _timestamp_pb2_1.Timestamp
    def __init__(self, space_knowledge_domain_file_page: _Optional[_Union[_space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage, _Mapping]] = ..., space_knowledge_domain_file_page_services_access_session_token_details: _Optional[_Union[_generic_pb2.PersistentSessionTokenDetails, _Mapping]] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...
