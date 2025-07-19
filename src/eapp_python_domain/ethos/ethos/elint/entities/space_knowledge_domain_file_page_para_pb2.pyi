from ethos.elint.entities import space_knowledge_domain_file_page_pb2 as _space_knowledge_domain_file_page_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceKnowledgeDomainFilePagePara(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page_para_id", "space_knowledge_domain_file_page", "page_contour_dimensions", "para_tags", "created_at", "last_updated_at", "last_accessed_at")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_CONTOUR_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    PARA_TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_AT_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page_para_id: str
    space_knowledge_domain_file_page: _space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage
    page_contour_dimensions: PageContourDimensions
    para_tags: _containers.RepeatedCompositeFieldContainer[ParaTag]
    created_at: _timestamp_pb2.Timestamp
    last_updated_at: _timestamp_pb2.Timestamp
    last_accessed_at: _timestamp_pb2.Timestamp
    def __init__(self, space_knowledge_domain_file_page_para_id: _Optional[str] = ..., space_knowledge_domain_file_page: _Optional[_Union[_space_knowledge_domain_file_page_pb2.SpaceKnowledgeDomainFilePage, _Mapping]] = ..., page_contour_dimensions: _Optional[_Union[PageContourDimensions, _Mapping]] = ..., para_tags: _Optional[_Iterable[_Union[ParaTag, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_accessed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ParaText(_message.Message):
    __slots__ = ("para_id", "para_text")
    PARA_ID_FIELD_NUMBER: _ClassVar[int]
    PARA_TEXT_FIELD_NUMBER: _ClassVar[int]
    para_id: str
    para_text: str
    def __init__(self, para_id: _Optional[str] = ..., para_text: _Optional[str] = ...) -> None: ...

class PageContourDimensions(_message.Message):
    __slots__ = ("x", "y", "w", "h")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    w: int
    h: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., w: _Optional[int] = ..., h: _Optional[int] = ...) -> None: ...

class ParaTag(_message.Message):
    __slots__ = ("para_tag_id", "para_tag_name")
    PARA_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    PARA_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    para_tag_id: str
    para_tag_name: str
    def __init__(self, para_tag_id: _Optional[str] = ..., para_tag_name: _Optional[str] = ...) -> None: ...
