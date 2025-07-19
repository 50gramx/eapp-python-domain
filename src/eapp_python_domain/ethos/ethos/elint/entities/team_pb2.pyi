from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import associate_pb2 as _associate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import organisation_pb2 as _organisation_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class Team(_message.Message):
    __slots__ = ("admin_associate", "of_organisation", "team_id", "team_description", "team_members", "team_tags", "created_at")
    ADMIN_ASSOCIATE_FIELD_NUMBER: _ClassVar[int]
    OF_ORGANISATION_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    TEAM_TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    admin_associate: _associate_pb2.Associate
    of_organisation: _organisation_pb2.Organisation
    team_id: int
    team_description: str
    team_members: _containers.RepeatedCompositeFieldContainer[_associate_pb2.Associate]
    team_tags: _containers.RepeatedCompositeFieldContainer[TeamTag]
    created_at: _timestamp_pb2_1_1.Timestamp
    def __init__(self, admin_associate: _Optional[_Union[_associate_pb2.Associate, _Mapping]] = ..., of_organisation: _Optional[_Union[_organisation_pb2.Organisation, _Mapping]] = ..., team_id: _Optional[int] = ..., team_description: _Optional[str] = ..., team_members: _Optional[_Iterable[_Union[_associate_pb2.Associate, _Mapping]]] = ..., team_tags: _Optional[_Iterable[_Union[TeamTag, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2_1_1.Timestamp, _Mapping]] = ...) -> None: ...

class TeamTag(_message.Message):
    __slots__ = ("team_tag_id", "team_tag_name")
    TEAM_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    team_tag_id: str
    team_tag_name: str
    def __init__(self, team_tag_id: _Optional[str] = ..., team_tag_name: _Optional[str] = ...) -> None: ...
