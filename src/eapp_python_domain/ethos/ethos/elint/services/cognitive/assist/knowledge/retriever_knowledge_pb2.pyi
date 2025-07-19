from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_file_page_pb2 as _space_knowledge_domain_file_page_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_knowledge_domain_file_page_para_pb2 as _space_knowledge_domain_file_page_para_pb2
from ethos.elint.services.product.knowledge.space_knowledge_domain import access_space_knowledge_domain_pb2 as _access_space_knowledge_domain_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RetrieveClosestPagesReq(_message.Message):
    __slots__ = ("access_auth_details", "message", "retrieve_page_count")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_PAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    message: str
    retrieve_page_count: int
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., message: _Optional[str] = ..., retrieve_page_count: _Optional[int] = ...) -> None: ...

class RetrieveClosestParasRequest(_message.Message):
    __slots__ = ("access_auth_details", "message", "retrieve_para_count")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_PARA_COUNT_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    message: str
    retrieve_para_count: int
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., message: _Optional[str] = ..., retrieve_para_count: _Optional[int] = ...) -> None: ...

class ClosestPages(_message.Message):
    __slots__ = ("ranked_pages", "response_meta")
    RANKED_PAGES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    ranked_pages: _containers.RepeatedCompositeFieldContainer[RankedPage]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, ranked_pages: _Optional[_Iterable[_Union[RankedPage, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ClosestParas(_message.Message):
    __slots__ = ("ranked_paras", "response_meta")
    RANKED_PARAS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    ranked_paras: _containers.RepeatedCompositeFieldContainer[RankedPara]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, ranked_paras: _Optional[_Iterable[_Union[RankedPara, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class RankedPage(_message.Message):
    __slots__ = ("page", "page_rank")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_RANK_FIELD_NUMBER: _ClassVar[int]
    page: _space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage
    page_rank: float
    def __init__(self, page: _Optional[_Union[_space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage, _Mapping]] = ..., page_rank: _Optional[float] = ...) -> None: ...

class RankedPara(_message.Message):
    __slots__ = ("para", "para_rank")
    PARA_FIELD_NUMBER: _ClassVar[int]
    PARA_RANK_FIELD_NUMBER: _ClassVar[int]
    para: _space_knowledge_domain_file_page_para_pb2.SpaceKnowledgeDomainFilePagePara
    para_rank: float
    def __init__(self, para: _Optional[_Union[_space_knowledge_domain_file_page_para_pb2.SpaceKnowledgeDomainFilePagePara, _Mapping]] = ..., para_rank: _Optional[float] = ...) -> None: ...
