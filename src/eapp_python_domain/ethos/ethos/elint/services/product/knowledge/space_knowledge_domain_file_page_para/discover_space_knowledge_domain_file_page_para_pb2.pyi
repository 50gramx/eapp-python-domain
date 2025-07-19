from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_file_page_para_pb2 as _space_knowledge_domain_file_page_para_pb2
from ethos.elint.services.product.knowledge.space_knowledge_domain import access_space_knowledge_domain_pb2 as _access_space_knowledge_domain_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListOfParaIds(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page_para_ids", "response_meta")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_IDS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page_para_ids: _containers.RepeatedScalarFieldContainer[str]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_knowledge_domain_file_page_para_ids: _Optional[_Iterable[str]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetParaTextByIdReq(_message.Message):
    __slots__ = ("access_auth_details", "space_knowledge_domain_file_page_para_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    space_knowledge_domain_file_page_para_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file_page_para_id: _Optional[str] = ...) -> None: ...

class GetParaTextByIdRes(_message.Message):
    __slots__ = ("para_text", "response_meta")
    PARA_TEXT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    para_text: str
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, para_text: _Optional[str] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetParaByIdRequest(_message.Message):
    __slots__ = ("access_auth_details", "space_knowledge_domain_file_page_para_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    space_knowledge_domain_file_page_para_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file_page_para_id: _Optional[str] = ...) -> None: ...

class GetParaByIdResponse(_message.Message):
    __slots__ = ("space_knowledge_domain_file_page_para", "response_meta")
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_file_page_para: _space_knowledge_domain_file_page_para_pb2.SpaceKnowledgeDomainFilePagePara
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_knowledge_domain_file_page_para: _Optional[_Union[_space_knowledge_domain_file_page_para_pb2.SpaceKnowledgeDomainFilePagePara, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetParaImageByIdRequest(_message.Message):
    __slots__ = ("access_auth_details", "space_knowledge_domain_file_page_para_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_PAGE_PARA_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    space_knowledge_domain_file_page_para_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file_page_para_id: _Optional[str] = ...) -> None: ...

class GetParaImageByIdResponse(_message.Message):
    __slots__ = ("image_chunk",)
    IMAGE_CHUNK_FIELD_NUMBER: _ClassVar[int]
    image_chunk: bytes
    def __init__(self, image_chunk: _Optional[bytes] = ...) -> None: ...
