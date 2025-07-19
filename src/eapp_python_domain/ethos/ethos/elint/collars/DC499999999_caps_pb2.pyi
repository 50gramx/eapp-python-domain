from ethos.elint.entities import space_service_pb2 as _space_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.collars import DC499999999_pb2 as _DC499999999_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.service.space_service_domain import access_space_service_domain_pb2 as _access_space_service_domain_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthWithDeployment(_message.Message):
    __slots__ = ("auth", "deployment")
    AUTH_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    auth: _access_space_service_domain_pb2.SpaceServiceDomainServicesAccessAuthDetails
    deployment: _DC499999999_pb2.Deployment
    def __init__(self, auth: _Optional[_Union[_access_space_service_domain_pb2.SpaceServiceDomainServicesAccessAuthDetails, _Mapping]] = ..., deployment: _Optional[_Union[_DC499999999_pb2.Deployment, _Mapping]] = ...) -> None: ...

class RepeatedDC499999999(_message.Message):
    __slots__ = ("meta", "collars")
    META_FIELD_NUMBER: _ClassVar[int]
    COLLARS_FIELD_NUMBER: _ClassVar[int]
    meta: _generic_pb2.ResponseMeta
    collars: _containers.RepeatedCompositeFieldContainer[_DC499999999_pb2.DC499999999]
    def __init__(self, meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., collars: _Optional[_Iterable[_Union[_DC499999999_pb2.DC499999999, _Mapping]]] = ...) -> None: ...

class SSDAuthWithCollarID(_message.Message):
    __slots__ = ("auth", "collar_id")
    AUTH_FIELD_NUMBER: _ClassVar[int]
    COLLAR_ID_FIELD_NUMBER: _ClassVar[int]
    auth: _access_space_service_domain_pb2.SpaceServiceDomainServicesAccessAuthDetails
    collar_id: str
    def __init__(self, auth: _Optional[_Union[_access_space_service_domain_pb2.SpaceServiceDomainServicesAccessAuthDetails, _Mapping]] = ..., collar_id: _Optional[str] = ...) -> None: ...
