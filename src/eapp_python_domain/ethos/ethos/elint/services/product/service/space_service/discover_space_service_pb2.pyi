from ethos.elint.entities import space_service_pb2 as _space_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_service_domain_pb2 as _space_service_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1_1
from ethos.elint.services.product.service.space_service import access_space_service_pb2 as _access_space_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSpaceServiceDomainsResponse(_message.Message):
    __slots__ = ("space_service_domains", "response_meta")
    SPACE_SERVICE_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_service_domains: _containers.RepeatedCompositeFieldContainer[_space_service_domain_pb2.SpaceServiceDomain]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_service_domains: _Optional[_Iterable[_Union[_space_service_domain_pb2.SpaceServiceDomain, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetSpaceServiceDomainByIdRequest(_message.Message):
    __slots__ = ("access_auth", "space_service_domain_id")
    ACCESS_AUTH_FIELD_NUMBER: _ClassVar[int]
    SPACE_SERVICE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth: _access_space_service_pb2.SpaceServiceServicesAccessAuthDetails
    space_service_domain_id: str
    def __init__(self, access_auth: _Optional[_Union[_access_space_service_pb2.SpaceServiceServicesAccessAuthDetails, _Mapping]] = ..., space_service_domain_id: _Optional[str] = ...) -> None: ...

class GetSpaceServiceDomainByIdResponse(_message.Message):
    __slots__ = ("space_service_domain", "response_meta")
    SPACE_SERVICE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_service_domain: _space_service_domain_pb2.SpaceServiceDomain
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_service_domain: _Optional[_Union[_space_service_domain_pb2.SpaceServiceDomain, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetDomainsByCollarCodeRequest(_message.Message):
    __slots__ = ("access_auth", "collar_code")
    ACCESS_AUTH_FIELD_NUMBER: _ClassVar[int]
    COLLAR_CODE_FIELD_NUMBER: _ClassVar[int]
    access_auth: _access_space_service_pb2.SpaceServiceServicesAccessAuthDetails
    collar_code: str
    def __init__(self, access_auth: _Optional[_Union[_access_space_service_pb2.SpaceServiceServicesAccessAuthDetails, _Mapping]] = ..., collar_code: _Optional[str] = ...) -> None: ...

class GetDomainsByCollarCodeResponse(_message.Message):
    __slots__ = ("space_service_domains", "response_meta")
    SPACE_SERVICE_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    space_service_domains: _containers.RepeatedCompositeFieldContainer[_space_service_domain_pb2.SpaceServiceDomain]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, space_service_domains: _Optional[_Iterable[_Union[_space_service_domain_pb2.SpaceServiceDomain, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...
