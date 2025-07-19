from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_file_pb2 as _space_knowledge_domain_file_pb2
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.knowledge.space_knowledge_domain import access_space_knowledge_domain_pb2 as _access_space_knowledge_domain_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFileByIDRequest(_message.Message):
    __slots__ = ("skd_auth", "file_id")
    SKD_AUTH_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    skd_auth: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    file_id: str
    def __init__(self, skd_auth: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., file_id: _Optional[str] = ...) -> None: ...

class FileExistsByIDRequest(_message.Message):
    __slots__ = ("account_knowledge_domain_file_access_meta", "file_id")
    ACCOUNT_KNOWLEDGE_DOMAIN_FILE_ACCESS_META_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    account_knowledge_domain_file_access_meta: _account_pb2.AccountSpaceKnowledgeDomainFileAccessMeta
    file_id: str
    def __init__(self, account_knowledge_domain_file_access_meta: _Optional[_Union[_account_pb2.AccountSpaceKnowledgeDomainFileAccessMeta, _Mapping]] = ..., file_id: _Optional[str] = ...) -> None: ...

class FileExistsByIDResponse(_message.Message):
    __slots__ = ("file_exists",)
    FILE_EXISTS_FIELD_NUMBER: _ClassVar[int]
    file_exists: bool
    def __init__(self, file_exists: bool = ...) -> None: ...

class DownloadRequest(_message.Message):
    __slots__ = ("skd_auth", "file")
    SKD_AUTH_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    skd_auth: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    file: _space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile
    def __init__(self, skd_auth: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., file: _Optional[_Union[_space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile, _Mapping]] = ...) -> None: ...

class DownloadResponse(_message.Message):
    __slots__ = ("file_buffer",)
    FILE_BUFFER_FIELD_NUMBER: _ClassVar[int]
    file_buffer: bytes
    def __init__(self, file_buffer: _Optional[bytes] = ...) -> None: ...
