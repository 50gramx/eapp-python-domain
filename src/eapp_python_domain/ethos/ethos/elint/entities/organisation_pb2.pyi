from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import community_pb2 as _community_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import galaxy_pb2 as _galaxy_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class Organisation(_message.Message):
    __slots__ = ("analytics_id", "id", "name", "galaxy", "admin", "associated_community", "postal_address", "incorporated_at", "is_active", "is_billing_active", "created_at")
    ANALYTICS_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GALAXY_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    POSTAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INCORPORATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_BILLING_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    analytics_id: str
    id: str
    name: OrganisationName
    galaxy: _galaxy_pb2.Galaxy
    admin: _account_pb2.Account
    associated_community: _community_pb2.Community
    postal_address: OrganisationPostalAddress
    incorporated_at: _timestamp_pb2_1_1_1.Timestamp
    is_active: bool
    is_billing_active: bool
    created_at: _timestamp_pb2_1_1_1.Timestamp
    def __init__(self, analytics_id: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[_Union[OrganisationName, _Mapping]] = ..., galaxy: _Optional[_Union[_galaxy_pb2.Galaxy, _Mapping]] = ..., admin: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., associated_community: _Optional[_Union[_community_pb2.Community, _Mapping]] = ..., postal_address: _Optional[_Union[OrganisationPostalAddress, _Mapping]] = ..., incorporated_at: _Optional[_Union[_timestamp_pb2_1_1_1.Timestamp, _Mapping]] = ..., is_active: bool = ..., is_billing_active: bool = ..., created_at: _Optional[_Union[_timestamp_pb2_1_1_1.Timestamp, _Mapping]] = ...) -> None: ...

class OrganisationName(_message.Message):
    __slots__ = ("legal_name", "assistant_name")
    LEGAL_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSISTANT_NAME_FIELD_NUMBER: _ClassVar[int]
    legal_name: str
    assistant_name: str
    def __init__(self, legal_name: _Optional[str] = ..., assistant_name: _Optional[str] = ...) -> None: ...

class OrganisationPostalAddress(_message.Message):
    __slots__ = ("address_line_1", "address_line_2", "city", "state_province_or_region", "zip_or_postal_code")
    ADDRESS_LINE_1_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE_2_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_PROVINCE_OR_REGION_FIELD_NUMBER: _ClassVar[int]
    ZIP_OR_POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    address_line_1: str
    address_line_2: str
    city: str
    state_province_or_region: str
    zip_or_postal_code: str
    def __init__(self, address_line_1: _Optional[str] = ..., address_line_2: _Optional[str] = ..., city: _Optional[str] = ..., state_province_or_region: _Optional[str] = ..., zip_or_postal_code: _Optional[str] = ...) -> None: ...
