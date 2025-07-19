from ethos.elint.entities import universe_pb2 as _universe_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OpenGalaxyTierEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FREE_TIER: _ClassVar[OpenGalaxyTierEnum]
    BASIC_TIER: _ClassVar[OpenGalaxyTierEnum]
    STANDARD_TIER: _ClassVar[OpenGalaxyTierEnum]
    PROFESSIONAL_TIER: _ClassVar[OpenGalaxyTierEnum]
FREE_TIER: OpenGalaxyTierEnum
BASIC_TIER: OpenGalaxyTierEnum
STANDARD_TIER: OpenGalaxyTierEnum
PROFESSIONAL_TIER: OpenGalaxyTierEnum

class Galaxy(_message.Message):
    __slots__ = ("galaxy_id", "galaxy_name", "universe", "galaxy_created_at", "galaxy_updated_at", "domain", "galaxy_description")
    GALAXY_ID_FIELD_NUMBER: _ClassVar[int]
    GALAXY_NAME_FIELD_NUMBER: _ClassVar[int]
    UNIVERSE_FIELD_NUMBER: _ClassVar[int]
    GALAXY_CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    GALAXY_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    GALAXY_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    galaxy_id: str
    galaxy_name: str
    universe: _universe_pb2.Universe
    galaxy_created_at: _timestamp_pb2.Timestamp
    galaxy_updated_at: _timestamp_pb2.Timestamp
    domain: str
    galaxy_description: str
    def __init__(self, galaxy_id: _Optional[str] = ..., galaxy_name: _Optional[str] = ..., universe: _Optional[_Union[_universe_pb2.Universe, _Mapping]] = ..., galaxy_created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., galaxy_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., domain: _Optional[str] = ..., galaxy_description: _Optional[str] = ...) -> None: ...
