from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_file_page_pb2 as _space_knowledge_domain_file_page_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.knowledge.space_knowledge_domain_file import access_space_knowledge_domain_file_pb2 as _access_space_knowledge_domain_file_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExtractPagesFromFileResponse(_message.Message):
    __slots__ = ("total_pages_count", "extracted_pages_count", "meta_done", "meta_message")
    TOTAL_PAGES_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXTRACTED_PAGES_COUNT_FIELD_NUMBER: _ClassVar[int]
    META_DONE_FIELD_NUMBER: _ClassVar[int]
    META_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    total_pages_count: int
    extracted_pages_count: int
    meta_done: bool
    meta_message: str
    def __init__(self, total_pages_count: _Optional[int] = ..., extracted_pages_count: _Optional[int] = ..., meta_done: bool = ..., meta_message: _Optional[str] = ...) -> None: ...

class ExtractTextFromPageResponse(_message.Message):
    __slots__ = ("meta_done", "meta_message")
    META_DONE_FIELD_NUMBER: _ClassVar[int]
    META_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    meta_done: bool
    meta_message: str
    def __init__(self, meta_done: bool = ..., meta_message: _Optional[str] = ...) -> None: ...
