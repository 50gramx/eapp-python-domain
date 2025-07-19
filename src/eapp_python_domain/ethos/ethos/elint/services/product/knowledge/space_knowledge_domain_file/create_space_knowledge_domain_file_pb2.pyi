from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_knowledge_domain_pb2 as _space_knowledge_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.entities import space_knowledge_domain_file_pb2 as _space_knowledge_domain_file_pb2
from ethos.elint.services.product.knowledge.space_knowledge_domain import access_space_knowledge_domain_pb2 as _access_space_knowledge_domain_pb2
from ethos.elint.services.product.knowledge.space_knowledge_domain_file import access_space_knowledge_domain_file_pb2 as _access_space_knowledge_domain_file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadSpaceKnowledgeDomainFileRequest(_message.Message):
    __slots__ = ("space_knowledge_domain_services_access_auth_details", "space_knowledge_domain_file_name", "space_knowledge_domain_file_size", "space_knowledge_domain_file_extension_type", "space_knowledge_domain_file_tags", "file_buffer")
    SPACE_KNOWLEDGE_DOMAIN_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_EXTENSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_TAGS_FIELD_NUMBER: _ClassVar[int]
    FILE_BUFFER_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_services_access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    space_knowledge_domain_file_name: str
    space_knowledge_domain_file_size: int
    space_knowledge_domain_file_extension_type: _space_knowledge_domain_file_pb2.ExtentionType
    space_knowledge_domain_file_tags: _containers.RepeatedCompositeFieldContainer[_space_knowledge_domain_file_pb2.FileTag]
    file_buffer: bytes
    def __init__(self, space_knowledge_domain_services_access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file_name: _Optional[str] = ..., space_knowledge_domain_file_size: _Optional[int] = ..., space_knowledge_domain_file_extension_type: _Optional[_Union[_space_knowledge_domain_file_pb2.ExtentionType, str]] = ..., space_knowledge_domain_file_tags: _Optional[_Iterable[_Union[_space_knowledge_domain_file_pb2.FileTag, _Mapping]]] = ..., file_buffer: _Optional[bytes] = ...) -> None: ...

class UploadSpaceKnowledgeDomainFileResponse(_message.Message):
    __slots__ = ("space_knowledge_domain_file_service_access_auth_details", "length", "space_knowledge_domain_file_upload_done", "space_knowledge_domain_file_upload_message")
    SPACE_KNOWLEDGE_DOMAIN_FILE_SERVICE_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_UPLOAD_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_UPLOAD_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_service_access_auth_details: _access_space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFileServicesAccessAuthDetails
    length: int
    space_knowledge_domain_file_upload_done: bool
    space_knowledge_domain_file_upload_message: str
    def __init__(self, space_knowledge_domain_file_service_access_auth_details: _Optional[_Union[_access_space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFileServicesAccessAuthDetails, _Mapping]] = ..., length: _Optional[int] = ..., space_knowledge_domain_file_upload_done: bool = ..., space_knowledge_domain_file_upload_message: _Optional[str] = ...) -> None: ...
