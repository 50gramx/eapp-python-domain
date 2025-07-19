from ethos.elint.entities import space_service_pb2 as _space_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.collars import DC499999994_pb2 as _DC499999994_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.knowledge.space_knowledge import access_space_knowledge_pb2 as _access_space_knowledge_pb2
from ethos.elint.services.product.product.space_product_domain import access_space_product_domain_pb2 as _access_space_product_domain_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthWithSkincareProduct(_message.Message):
    __slots__ = ("spd_auth", "sk_auth", "skincare_product")
    SPD_AUTH_FIELD_NUMBER: _ClassVar[int]
    SK_AUTH_FIELD_NUMBER: _ClassVar[int]
    SKINCARE_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    spd_auth: _access_space_product_domain_pb2.SpaceProductDomainServicesAccessAuthDetails
    sk_auth: _access_space_knowledge_pb2.SpaceKnowledgeServicesAccessAuthDetails
    skincare_product: _DC499999994_pb2.SkincareProduct
    def __init__(self, spd_auth: _Optional[_Union[_access_space_product_domain_pb2.SpaceProductDomainServicesAccessAuthDetails, _Mapping]] = ..., sk_auth: _Optional[_Union[_access_space_knowledge_pb2.SpaceKnowledgeServicesAccessAuthDetails, _Mapping]] = ..., skincare_product: _Optional[_Union[_DC499999994_pb2.SkincareProduct, _Mapping]] = ...) -> None: ...

class RepeatedDC499999994(_message.Message):
    __slots__ = ("meta", "collars")
    META_FIELD_NUMBER: _ClassVar[int]
    COLLARS_FIELD_NUMBER: _ClassVar[int]
    meta: _generic_pb2.ResponseMeta
    collars: _containers.RepeatedCompositeFieldContainer[_DC499999994_pb2.DC499999994]
    def __init__(self, meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., collars: _Optional[_Iterable[_Union[_DC499999994_pb2.DC499999994, _Mapping]]] = ...) -> None: ...

class SPDAuthWithCollarID(_message.Message):
    __slots__ = ("auth", "sk_auth", "collar_id")
    AUTH_FIELD_NUMBER: _ClassVar[int]
    SK_AUTH_FIELD_NUMBER: _ClassVar[int]
    COLLAR_ID_FIELD_NUMBER: _ClassVar[int]
    auth: _access_space_product_domain_pb2.SpaceProductDomainServicesAccessAuthDetails
    sk_auth: _access_space_knowledge_pb2.SpaceKnowledgeServicesAccessAuthDetails
    collar_id: str
    def __init__(self, auth: _Optional[_Union[_access_space_product_domain_pb2.SpaceProductDomainServicesAccessAuthDetails, _Mapping]] = ..., sk_auth: _Optional[_Union[_access_space_knowledge_pb2.SpaceKnowledgeServicesAccessAuthDetails, _Mapping]] = ..., collar_id: _Optional[str] = ...) -> None: ...
