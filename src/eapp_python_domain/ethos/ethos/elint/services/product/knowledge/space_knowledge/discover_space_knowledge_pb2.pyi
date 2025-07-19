from ethos.elint.entities import space_knowledge_pb2 as _space_knowledge_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_pb2 as _space_knowledge_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1_1
from ethos.elint.services.product.knowledge.space_knowledge import access_space_knowledge_pb2 as _access_space_knowledge_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetInferredSpaceKnowledgeDomainsResponse(_message.Message):
    __slots__ = ("space_knowledge_inferred_domain", "response_meta")
    SPACE_KNOWLEDGE_INFERRED_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_inferred_domain: _containers.RepeatedCompositeFieldContainer[_space_knowledge_pb2.SpaceKnowledgeInferredDomain]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_knowledge_inferred_domain: _Optional[_Iterable[_Union[_space_knowledge_pb2.SpaceKnowledgeInferredDomain, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetSpaceKnowledgeDomainsResponse(_message.Message):
    __slots__ = ("space_knowledge_domains", "response_meta")
    SPACE_KNOWLEDGE_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domains: _containers.RepeatedCompositeFieldContainer[_space_knowledge_domain_pb2.SpaceKnowledgeDomain]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_knowledge_domains: _Optional[_Iterable[_Union[_space_knowledge_domain_pb2.SpaceKnowledgeDomain, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetSpaceKnowledgeDomainByIdRequest(_message.Message):
    __slots__ = ("access_auth", "space_knowledge_domain_id")
    ACCESS_AUTH_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth: _access_space_knowledge_pb2.SpaceKnowledgeServicesAccessAuthDetails
    space_knowledge_domain_id: str
    def __init__(self, access_auth: _Optional[_Union[_access_space_knowledge_pb2.SpaceKnowledgeServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_domain_id: _Optional[str] = ...) -> None: ...

class GetSpaceKnowledgeDomainByIdResponse(_message.Message):
    __slots__ = ("space_knowledge_domain", "response_meta")
    SPACE_KNOWLEDGE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain: _space_knowledge_domain_pb2.SpaceKnowledgeDomain
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_knowledge_domain: _Optional[_Union[_space_knowledge_domain_pb2.SpaceKnowledgeDomain, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...
