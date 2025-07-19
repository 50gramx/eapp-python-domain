from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_knowledge_domain_pb2 as _space_knowledge_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.services.product.knowledge.space_knowledge import access_space_knowledge_pb2 as _access_space_knowledge_pb2
from ethos.elint.services.product.knowledge.space_knowledge_domain import access_space_knowledge_domain_pb2 as _access_space_knowledge_domain_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAccountWhiteSpaceKnowledgeDomainResponse(_message.Message):
    __slots__ = ("space_knowledge_domain_services_access_auth_details", "create_account_white_space_knowledge_domain_done", "create_account_white_space_knowledge_domain_message")
    SPACE_KNOWLEDGE_DOMAIN_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_ACCOUNT_WHITE_SPACE_KNOWLEDGE_DOMAIN_DONE_FIELD_NUMBER: _ClassVar[int]
    CREATE_ACCOUNT_WHITE_SPACE_KNOWLEDGE_DOMAIN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_services_access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    create_account_white_space_knowledge_domain_done: bool
    create_account_white_space_knowledge_domain_message: str
    def __init__(self, space_knowledge_domain_services_access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., create_account_white_space_knowledge_domain_done: bool = ..., create_account_white_space_knowledge_domain_message: _Optional[str] = ...) -> None: ...

class CreateSpaceKnowledgeDomainRequest(_message.Message):
    __slots__ = ("space_knowledge_services_access_auth_details", "space_knowledge_domain_name", "space_knowledge_domain_description", "space_knowledge_domain_collar_enum", "space_knowledge_domain_isolated")
    SPACE_KNOWLEDGE_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_COLLAR_ENUM_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_ISOLATED_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_services_access_auth_details: _access_space_knowledge_pb2.SpaceKnowledgeServicesAccessAuthDetails
    space_knowledge_domain_name: str
    space_knowledge_domain_description: str
    space_knowledge_domain_collar_enum: _space_knowledge_domain_pb2.SpaceKnowledgeDomainCollarEnum
    space_knowledge_domain_isolated: bool
    def __init__(self, space_knowledge_services_access_auth_details: _Optional[_Union[_access_space_knowledge_pb2.SpaceKnowledgeServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_name: _Optional[str] = ..., space_knowledge_domain_description: _Optional[str] = ..., space_knowledge_domain_collar_enum: _Optional[_Union[_space_knowledge_domain_pb2.SpaceKnowledgeDomainCollarEnum, str]] = ..., space_knowledge_domain_isolated: bool = ...) -> None: ...

class CreateSpaceKnowledgeDomainResponse(_message.Message):
    __slots__ = ("space_knowledge_domain_services_access_auth_details", "response_meta")
    SPACE_KNOWLEDGE_DOMAIN_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_services_access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_knowledge_domain_services_access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...
