from ethos.elint.entities import space_knowledge_domain_file_page_pb2 as _space_knowledge_domain_file_page_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GeneratePageQuestionRequest(_message.Message):
    __slots__ = ("page",)
    PAGE_FIELD_NUMBER: _ClassVar[int]
    page: _space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage
    def __init__(self, page: _Optional[_Union[_space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage, _Mapping]] = ...) -> None: ...

class GeneratePageQuestionResponse(_message.Message):
    __slots__ = ("questions",)
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    questions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, questions: _Optional[_Iterable[str]] = ...) -> None: ...
