from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityDomainCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOMAIN_CODE_UNDEFINED: _ClassVar[CommunityDomainCode]
    DOMAIN_CODE_LEGAL: _ClassVar[CommunityDomainCode]
    DOMAIN_CODE_AUTOMATION: _ClassVar[CommunityDomainCode]
    DOMAIN_CODE_EDUCATION: _ClassVar[CommunityDomainCode]
    DOMAIN_CODE_MEDICAL: _ClassVar[CommunityDomainCode]
DOMAIN_CODE_UNDEFINED: CommunityDomainCode
DOMAIN_CODE_LEGAL: CommunityDomainCode
DOMAIN_CODE_AUTOMATION: CommunityDomainCode
DOMAIN_CODE_EDUCATION: CommunityDomainCode
DOMAIN_CODE_MEDICAL: CommunityDomainCode

class Community(_message.Message):
    __slots__ = ("community_domain_code", "recognised_at", "associated_organisations_count")
    COMMUNITY_DOMAIN_CODE_FIELD_NUMBER: _ClassVar[int]
    RECOGNISED_AT_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_ORGANISATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    community_domain_code: CommunityDomainCode
    recognised_at: _timestamp_pb2.Timestamp
    associated_organisations_count: int
    def __init__(self, community_domain_code: _Optional[_Union[CommunityDomainCode, str]] = ..., recognised_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., associated_organisations_count: _Optional[int] = ...) -> None: ...
