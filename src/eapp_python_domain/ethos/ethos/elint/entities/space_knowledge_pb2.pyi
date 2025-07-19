from ethos.elint.entities import space_pb2 as _space_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceKnowledgeAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASK_QUESTION: _ClassVar[SpaceKnowledgeAction]
    SHOW_URL_PAGE: _ClassVar[SpaceKnowledgeAction]
ASK_QUESTION: SpaceKnowledgeAction
SHOW_URL_PAGE: SpaceKnowledgeAction

class SpaceKnowledge(_message.Message):
    __slots__ = ("space_knowledge_name", "space_knowledge_id", "space_knowledge_admin_account_id", "space", "created_at")
    SPACE_KNOWLEDGE_NAME_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_ADMIN_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_name: str
    space_knowledge_id: str
    space_knowledge_admin_account_id: str
    space: _space_pb2.Space
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, space_knowledge_name: _Optional[str] = ..., space_knowledge_id: _Optional[str] = ..., space_knowledge_admin_account_id: _Optional[str] = ..., space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SpaceKnowledgeInferredDomain(_message.Message):
    __slots__ = ("inferred_domain_id", "space_knowledge_id", "space_knowledge_domain_id", "inferred_at")
    INFERRED_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    INFERRED_AT_FIELD_NUMBER: _ClassVar[int]
    inferred_domain_id: str
    space_knowledge_id: str
    space_knowledge_domain_id: str
    inferred_at: _timestamp_pb2.Timestamp
    def __init__(self, inferred_domain_id: _Optional[str] = ..., space_knowledge_id: _Optional[str] = ..., space_knowledge_domain_id: _Optional[str] = ..., inferred_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
