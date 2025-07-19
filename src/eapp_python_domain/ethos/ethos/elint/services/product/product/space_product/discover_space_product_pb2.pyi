from ethos.elint.entities import space_product_pb2 as _space_product_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_product_domain_pb2 as _space_product_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1_1
from ethos.elint.services.product.product.space_product import access_space_product_pb2 as _access_space_product_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSpaceProductDomainsResponse(_message.Message):
    __slots__ = ("space_product_domains", "response_meta")
    SPACE_PRODUCT_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_product_domains: _containers.RepeatedCompositeFieldContainer[_space_product_domain_pb2.SpaceProductDomain]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_product_domains: _Optional[_Iterable[_Union[_space_product_domain_pb2.SpaceProductDomain, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetSpaceProductDomainByIdRequest(_message.Message):
    __slots__ = ("access_auth", "space_product_domain_id")
    ACCESS_AUTH_FIELD_NUMBER: _ClassVar[int]
    SPACE_PRODUCT_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth: _access_space_product_pb2.SpaceProductServicesAccessAuthDetails
    space_product_domain_id: str
    def __init__(self, access_auth: _Optional[_Union[_access_space_product_pb2.SpaceProductServicesAccessAuthDetails, _Mapping]] = ..., space_product_domain_id: _Optional[str] = ...) -> None: ...

class GetSpaceProductDomainByIdResponse(_message.Message):
    __slots__ = ("space_product_domain", "response_meta")
    SPACE_PRODUCT_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_product_domain: _space_product_domain_pb2.SpaceProductDomain
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_product_domain: _Optional[_Union[_space_product_domain_pb2.SpaceProductDomain, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetDomainsByCollarCodeRequest(_message.Message):
    __slots__ = ("access_auth", "collar_code")
    ACCESS_AUTH_FIELD_NUMBER: _ClassVar[int]
    COLLAR_CODE_FIELD_NUMBER: _ClassVar[int]
    access_auth: _access_space_product_pb2.SpaceProductServicesAccessAuthDetails
    collar_code: str
    def __init__(self, access_auth: _Optional[_Union[_access_space_product_pb2.SpaceProductServicesAccessAuthDetails, _Mapping]] = ..., collar_code: _Optional[str] = ...) -> None: ...

class GetDomainsByCollarCodeResponse(_message.Message):
    __slots__ = ("space_product_domains", "response_meta")
    SPACE_PRODUCT_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_product_domains: _containers.RepeatedCompositeFieldContainer[_space_product_domain_pb2.SpaceProductDomain]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_product_domains: _Optional[_Iterable[_Union[_space_product_domain_pb2.SpaceProductDomain, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...
