from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_file_page_pb2 as _space_knowledge_domain_file_page_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_knowledge_domain_file_page_para_pb2 as _space_knowledge_domain_file_page_para_pb2
from ethos.elint.services.product.knowledge.space_knowledge_domain import access_space_knowledge_domain_pb2 as _access_space_knowledge_domain_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadPageQuestionRequest(_message.Message):
    __slots__ = ("access_auth_details", "page", "question")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    page: _space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage
    question: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., page: _Optional[_Union[_space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage, _Mapping]] = ..., question: _Optional[str] = ...) -> None: ...

class ReadPageQuestionResponse(_message.Message):
    __slots__ = ("page_answer", "response_meta")
    PAGE_ANSWER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    page_answer: PageAnswer
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, page_answer: _Optional[_Union[PageAnswer, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ReadParaQuestionRequest(_message.Message):
    __slots__ = ("access_auth_details", "para", "question")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PARA_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    para: _space_knowledge_domain_file_page_para_pb2.SpaceKnowledgeDomainFilePagePara
    question: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., para: _Optional[_Union[_space_knowledge_domain_file_page_para_pb2.SpaceKnowledgeDomainFilePagePara, _Mapping]] = ..., question: _Optional[str] = ...) -> None: ...

class ReadParaQuestionResponse(_message.Message):
    __slots__ = ("para_answer", "response_meta")
    PARA_ANSWER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    para_answer: ParaAnswer
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, para_answer: _Optional[_Union[ParaAnswer, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class PageAnswer(_message.Message):
    __slots__ = ("answer", "page_text")
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TEXT_FIELD_NUMBER: _ClassVar[int]
    answer: str
    page_text: str
    def __init__(self, answer: _Optional[str] = ..., page_text: _Optional[str] = ...) -> None: ...

class ParaAnswer(_message.Message):
    __slots__ = ("answer", "para_text")
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    PARA_TEXT_FIELD_NUMBER: _ClassVar[int]
    answer: str
    para_text: str
    def __init__(self, answer: _Optional[str] = ..., para_text: _Optional[str] = ...) -> None: ...
