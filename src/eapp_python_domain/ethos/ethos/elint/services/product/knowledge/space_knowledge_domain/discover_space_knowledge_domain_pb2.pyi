from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_knowledge_domain_pb2 as _space_knowledge_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.entities import space_knowledge_domain_file_pb2 as _space_knowledge_domain_file_pb2
from ethos.elint.services.product.knowledge.space_knowledge_domain import access_space_knowledge_domain_pb2 as _access_space_knowledge_domain_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAllDomainFilesResponse(_message.Message):
    __slots__ = ("files",)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[_space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile]
    def __init__(self, files: _Optional[_Iterable[_Union[_space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile, _Mapping]]] = ...) -> None: ...

class GetBestAnswersRequest(_message.Message):
    __slots__ = ("access_auth_details", "best_answers_count", "question")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BEST_ANSWERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    best_answers_count: int
    question: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., best_answers_count: _Optional[int] = ..., question: _Optional[str] = ...) -> None: ...

class GetBestAnswersResponse(_message.Message):
    __slots__ = ("ranked_answers", "response_meta")
    RANKED_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    ranked_answers: _containers.RepeatedCompositeFieldContainer[_space_knowledge_domain_pb2.RankedAnswer]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, ranked_answers: _Optional[_Iterable[_Union[_space_knowledge_domain_pb2.RankedAnswer, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class RetrieveMessageContextPagesRequest(_message.Message):
    __slots__ = ("access_auth_details", "message")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    message: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class RetrieveMessageContextPagesResponse(_message.Message):
    __slots__ = ("context_page", "response_meta")
    CONTEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    context_page: _containers.RepeatedCompositeFieldContainer[ContextPage]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, context_page: _Optional[_Iterable[_Union[ContextPage, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class IsMessageContextInDomainRequest(_message.Message):
    __slots__ = ("access_auth_details", "message")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    message: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class IsMessageContextInDomainResponse(_message.Message):
    __slots__ = ("message_context_in_domain", "message_context_score", "response_meta")
    MESSAGE_CONTEXT_IN_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_CONTEXT_SCORE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    message_context_in_domain: bool
    message_context_score: int
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, message_context_in_domain: bool = ..., message_context_score: _Optional[int] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetInferredDomainsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FileCountResponse(_message.Message):
    __slots__ = ("file_count", "response_meta")
    FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    file_count: int
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, file_count: _Optional[int] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class PageCountResponse(_message.Message):
    __slots__ = ("page_count", "response_meta")
    PAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    page_count: int
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, page_count: _Optional[int] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ContextPage(_message.Message):
    __slots__ = ("page_rank", "page_id", "page_score")
    PAGE_RANK_FIELD_NUMBER: _ClassVar[int]
    PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SCORE_FIELD_NUMBER: _ClassVar[int]
    page_rank: int
    page_id: str
    page_score: int
    def __init__(self, page_rank: _Optional[int] = ..., page_id: _Optional[str] = ..., page_score: _Optional[int] = ...) -> None: ...
