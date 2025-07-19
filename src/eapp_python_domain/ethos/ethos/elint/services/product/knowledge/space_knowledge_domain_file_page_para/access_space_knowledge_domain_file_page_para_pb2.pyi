from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_file_page_para_pb2 as _space_knowledge_domain_file_page_para_pb2
from ethos.elint.services.product.knowledge.space_knowledge_domain_file_page import access_space_knowledge_domain_file_page_pb2 as _access_space_knowledge_domain_file_page_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceKnowledgeDomainFilePageParaAccessTokenRequest(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page_services_access_auth_details", "space_knowledge_domain_file_page_para")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page_services_access_auth_details: _access_space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePageServicesAccessAuthDetails
    space_knowledge_domain_file_page_para: _space_knowledge_domain_file_page_para_pb2.SpaceKnowledgeDomainFilePagePara
    def __init__(self, space_knowledge_domain_file_page_services_access_auth_details: _Optional[_Union[_access_space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePageServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file_page_para: _Optional[_Union[_space_knowledge_domain_file_page_para_pb2.SpaceKnowledgeDomainFilePagePara, _Mapping]] = ...) -> None: ...

class SpaceKnowledgeDomainFilePageParaAccessTokenResponse(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page_para_services_access_auth_details", "space_knowledge_domain_file_page_para_services_access_done", "space_knowledge_domain_file_page_para_services_access_message")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_SERVICES_ACCESS_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_SERVICES_ACCESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page_para_services_access_auth_details: SpaceKnowledgeDomainFilePageParaServicesAccessAuthDetails
    space_knowledge_domain_file_page_para_services_access_done: bool
    space_knowledge_domain_file_page_para_services_access_message: str
    def __init__(self, space_knowledge_domain_file_page_para_services_access_auth_details: _Optional[_Union[SpaceKnowledgeDomainFilePageParaServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file_page_para_services_access_done: bool = ..., space_knowledge_domain_file_page_para_services_access_message: _Optional[str] = ...) -> None: ...

class ValidateSpaceKnowledgeDomainFilePageParaServicesResponse(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page_para_services_access_validation_done", "space_knowledge_domain_file_page_para_services_access_validation_message")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_SERVICES_ACCESS_VALIDATION_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_SERVICES_ACCESS_VALIDATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page_para_services_access_validation_done: bool
    space_knowledge_domain_file_page_para_services_access_validation_message: str
    def __init__(self, space_knowledge_domain_file_page_para_services_access_validation_done: bool = ..., space_knowledge_domain_file_page_para_services_access_validation_message: _Optional[str] = ...) -> None: ...

class SpaceKnowledgeDomainFilePageParaServicesAccessAuthDetails(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page_para", "space_knowledge_domain_file_page_para_services_access_session_token_details", "requested_at")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_SERVICES_ACCESS_SESSION_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page_para: _space_knowledge_domain_file_page_para_pb2.SpaceKnowledgeDomainFilePagePara
    space_knowledge_domain_file_page_para_services_access_session_token_details: _generic_pb2.PersistentSessionTokenDetails
    requested_at: _timestamp_pb2.Timestamp
    def __init__(self, space_knowledge_domain_file_page_para: _Optional[_Union[_space_knowledge_domain_file_page_para_pb2.SpaceKnowledgeDomainFilePagePara, _Mapping]] = ..., space_knowledge_domain_file_page_para_services_access_session_token_details: _Optional[_Union[_generic_pb2.PersistentSessionTokenDetails, _Mapping]] = ..., requested_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
