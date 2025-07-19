from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_file_page_pb2 as _space_knowledge_domain_file_page_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.knowledge.space_knowledge_domain import access_space_knowledge_domain_pb2 as _access_space_knowledge_domain_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListOfPageIds(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page_ids", "response_meta")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page_ids: _containers.RepeatedScalarFieldContainer[str]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_knowledge_domain_file_page_ids: _Optional[_Iterable[str]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetPageTextByIdReq(_message.Message):
    __slots__ = ("access_auth_details", "space_knowledge_domain_file_page_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    space_knowledge_domain_file_page_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file_page_id: _Optional[str] = ...) -> None: ...

class GetPageTextByIdRes(_message.Message):
    __slots__ = ("page_text", "meta")
    PAGE_TEXT_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    page_text: str
    meta: _generic_pb2.ResponseMeta
    def __init__(self, page_text: _Optional[str] = ..., meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetPageByIdRequest(_message.Message):
    __slots__ = ("access_auth_details", "space_knowledge_domain_file_page_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    space_knowledge_domain_file_page_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file_page_id: _Optional[str] = ...) -> None: ...

class GetPageByIdResponse(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page", "response_meta")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page: _space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_knowledge_domain_file_page: _Optional[_Union[_space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...
