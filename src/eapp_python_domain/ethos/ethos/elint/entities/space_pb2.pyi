from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import galaxy_pb2 as _galaxy_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KNOWLEDGE: _ClassVar[SpaceKind]
    PRODUCT: _ClassVar[SpaceKind]
    SERVICE: _ClassVar[SpaceKind]
    THING: _ClassVar[SpaceKind]

class SpaceAccessibilityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOSED: _ClassVar[SpaceAccessibilityType]
    OPEN: _ClassVar[SpaceAccessibilityType]

class SpaceIsolationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOT_ISOLATED: _ClassVar[SpaceIsolationType]
    ISOLATED: _ClassVar[SpaceIsolationType]

class SpaceEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCOUNT: _ClassVar[SpaceEntityType]
    TEAM: _ClassVar[SpaceEntityType]
KNOWLEDGE: SpaceKind
PRODUCT: SpaceKind
SERVICE: SpaceKind
THING: SpaceKind
CLOSED: SpaceAccessibilityType
OPEN: SpaceAccessibilityType
NOT_ISOLATED: SpaceIsolationType
ISOLATED: SpaceIsolationType
ACCOUNT: SpaceEntityType
TEAM: SpaceEntityType

class Space(_message.Message):
    __slots__ = ("galaxy", "space_id", "space_accessibility_type", "space_isolation_type", "space_entity_type", "space_admin_id", "space_created_at")
    GALAXY_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ACCESSIBILITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ISOLATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ADMIN_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    galaxy: _galaxy_pb2.Galaxy
    space_id: str
    space_accessibility_type: SpaceAccessibilityType
    space_isolation_type: SpaceIsolationType
    space_entity_type: SpaceEntityType
    space_admin_id: str
    space_created_at: _timestamp_pb2.Timestamp
    def __init__(self, galaxy: _Optional[_Union[_galaxy_pb2.Galaxy, _Mapping]] = ..., space_id: _Optional[str] = ..., space_accessibility_type: _Optional[_Union[SpaceAccessibilityType, str]] = ..., space_isolation_type: _Optional[_Union[SpaceIsolationType, str]] = ..., space_entity_type: _Optional[_Union[SpaceEntityType, str]] = ..., space_admin_id: _Optional[str] = ..., space_created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
