from ethos.elint.entities import space_knowledge_domain_pb2 as _space_knowledge_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExtentionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PNG: _ClassVar[ExtentionType]
    JPEG: _ClassVar[ExtentionType]
    PDF: _ClassVar[ExtentionType]
    TEXT: _ClassVar[ExtentionType]
PNG: ExtentionType
JPEG: ExtentionType
PDF: ExtentionType
TEXT: ExtentionType

class FileTag(_message.Message):
    __slots__ = ("file_tag_id", "file_tag_name")
    FILE_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    file_tag_id: str
    file_tag_name: str
    def __init__(self, file_tag_id: _Optional[str] = ..., file_tag_name: _Optional[str] = ...) -> None: ...

class SpaceKnowledgeDomainFile(_message.Message):
    __slots__ = ("space_knowledge_domain_file_name", "space_knowledge_domain_file_size", "space_knowledge_domain_file_id", "space_knowledge_domain_file_extension_type", "space_knowledge_domain", "space_knowledge_domain_file_tags", "created_at", "last_updated_at", "last_accessed_at")
    SPACE_KNOWLEDGE_DOMAIN_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_EXTENSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_AT_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_name: str
    space_knowledge_domain_file_size: int
    space_knowledge_domain_file_id: str
    space_knowledge_domain_file_extension_type: ExtentionType
    space_knowledge_domain: _space_knowledge_domain_pb2.SpaceKnowledgeDomain
    space_knowledge_domain_file_tags: _containers.RepeatedCompositeFieldContainer[FileTag]
    created_at: _timestamp_pb2.Timestamp
    last_updated_at: _timestamp_pb2.Timestamp
    last_accessed_at: _timestamp_pb2.Timestamp
    def __init__(self, space_knowledge_domain_file_name: _Optional[str] = ..., space_knowledge_domain_file_size: _Optional[int] = ..., space_knowledge_domain_file_id: _Optional[str] = ..., space_knowledge_domain_file_extension_type: _Optional[_Union[ExtentionType, str]] = ..., space_knowledge_domain: _Optional[_Union[_space_knowledge_domain_pb2.SpaceKnowledgeDomain, _Mapping]] = ..., space_knowledge_domain_file_tags: _Optional[_Iterable[_Union[FileTag, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_accessed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
