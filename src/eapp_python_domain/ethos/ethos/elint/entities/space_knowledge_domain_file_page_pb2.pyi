from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_file_pb2 as _space_knowledge_domain_file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceKnowledgeDomainFilePage(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page_id", "space_knowledge_domain_file_page_count", "space_knowledge_domain_file", "page_tags", "created_at", "last_updated_at", "last_accessed_at")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_AT_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page_id: str
    space_knowledge_domain_file_page_count: int
    space_knowledge_domain_file: _space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile
    page_tags: _containers.RepeatedCompositeFieldContainer[PageTag]
    created_at: _timestamp_pb2.Timestamp
    last_updated_at: _timestamp_pb2.Timestamp
    last_accessed_at: _timestamp_pb2.Timestamp
    def __init__(self, space_knowledge_domain_file_page_id: _Optional[str] = ..., space_knowledge_domain_file_page_count: _Optional[int] = ..., space_knowledge_domain_file: _Optional[_Union[_space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile, _Mapping]] = ..., page_tags: _Optional[_Iterable[_Union[PageTag, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_accessed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PageTag(_message.Message):
    __slots__ = ("page_tag_id", "page_tag_name")
    PAGE_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    page_tag_id: str
    page_tag_name: str
    def __init__(self, page_tag_id: _Optional[str] = ..., page_tag_name: _Optional[str] = ...) -> None: ...
