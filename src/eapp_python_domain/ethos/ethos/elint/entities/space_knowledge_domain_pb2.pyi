from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_pb2 as _space_knowledge_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceKnowledgeDomainCollarEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WHITE_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    BLUE_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    PINK_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    GOLD_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    RED_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    PURPLE_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    NEW_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    NO_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    ORANGE_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    GREEN_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    SCARLET_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    BROWN_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    STEEL_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    BLACK_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    GREY_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
    SKD_I_AM_COLLAR: _ClassVar[SpaceKnowledgeDomainCollarEnum]
WHITE_COLLAR: SpaceKnowledgeDomainCollarEnum
BLUE_COLLAR: SpaceKnowledgeDomainCollarEnum
PINK_COLLAR: SpaceKnowledgeDomainCollarEnum
GOLD_COLLAR: SpaceKnowledgeDomainCollarEnum
RED_COLLAR: SpaceKnowledgeDomainCollarEnum
PURPLE_COLLAR: SpaceKnowledgeDomainCollarEnum
NEW_COLLAR: SpaceKnowledgeDomainCollarEnum
NO_COLLAR: SpaceKnowledgeDomainCollarEnum
ORANGE_COLLAR: SpaceKnowledgeDomainCollarEnum
GREEN_COLLAR: SpaceKnowledgeDomainCollarEnum
SCARLET_COLLAR: SpaceKnowledgeDomainCollarEnum
BROWN_COLLAR: SpaceKnowledgeDomainCollarEnum
STEEL_COLLAR: SpaceKnowledgeDomainCollarEnum
BLACK_COLLAR: SpaceKnowledgeDomainCollarEnum
GREY_COLLAR: SpaceKnowledgeDomainCollarEnum
SKD_I_AM_COLLAR: SpaceKnowledgeDomainCollarEnum

class SpaceKnowledgeDomain(_message.Message):
    __slots__ = ("space_knowledge_domain_id", "space_knowledge_domain_name", "space_knowledge_domain_description", "space_knowledge_domain_collar_enum", "space_knowledge_domain_isolated", "space_knowledge", "created_at", "last_updated_at")
    SPACE_KNOWLEDGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_COLLAR_ENUM_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_ISOLATED_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain_id: str
    space_knowledge_domain_name: str
    space_knowledge_domain_description: str
    space_knowledge_domain_collar_enum: SpaceKnowledgeDomainCollarEnum
    space_knowledge_domain_isolated: bool
    space_knowledge: _space_knowledge_pb2.SpaceKnowledge
    created_at: _timestamp_pb2_1.Timestamp
    last_updated_at: _timestamp_pb2_1.Timestamp
    def __init__(self, space_knowledge_domain_id: _Optional[str] = ..., space_knowledge_domain_name: _Optional[str] = ..., space_knowledge_domain_description: _Optional[str] = ..., space_knowledge_domain_collar_enum: _Optional[_Union[SpaceKnowledgeDomainCollarEnum, str]] = ..., space_knowledge_domain_isolated: bool = ..., space_knowledge: _Optional[_Union[_space_knowledge_pb2.SpaceKnowledge, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class SpaceKnowledgeDomainInferringAccount(_message.Message):
    __slots__ = ("inferring_account_id", "space_knowledge_id", "account_id", "inferred_at")
    INFERRING_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INFERRED_AT_FIELD_NUMBER: _ClassVar[int]
    inferring_account_id: str
    space_knowledge_id: str
    account_id: str
    inferred_at: _timestamp_pb2_1.Timestamp
    def __init__(self, inferring_account_id: _Optional[str] = ..., space_knowledge_id: _Optional[str] = ..., account_id: _Optional[str] = ..., inferred_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class RankedAnswer(_message.Message):
    __slots__ = ("context_id", "para_rank", "answer")
    CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
    PARA_RANK_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    context_id: str
    para_rank: float
    answer: str
    def __init__(self, context_id: _Optional[str] = ..., para_rank: _Optional[float] = ..., answer: _Optional[str] = ...) -> None: ...
