from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_file_pb2 as _space_knowledge_domain_file_pb2
from ethos.elint.services.product.knowledge.space_knowledge_domain import access_space_knowledge_domain_pb2 as _access_space_knowledge_domain_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteSpaceKnowledgeDomainFileRequest(_message.Message):
    __slots__ = ("space_knowledge_domain_services_access_auth_details", "space_knowledge_domain_file")
    SPACE_KNOWLEDGE_DOMAIN_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_services_access_auth_details: _access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails
    space_knowledge_domain_file: _space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile
    def __init__(self, space_knowledge_domain_services_access_auth_details: _Optional[_Union[_access_space_knowledge_domain_pb2.SpaceKnowledgeDomainServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_file: _Optional[_Union[_space_knowledge_domain_file_pb2.SpaceKnowledgeDomainFile, _Mapping]] = ...) -> None: ...
