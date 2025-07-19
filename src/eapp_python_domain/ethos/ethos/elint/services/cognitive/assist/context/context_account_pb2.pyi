from ethos.elint.entities import space_knowledge_pb2 as _space_knowledge_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.services.product.identity.account_assistant import access_account_assistant_pb2 as _access_account_assistant_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountMessage(_message.Message):
    __slots__ = ("access_auth_details", "message")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails
    message: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class AccountMessageContext(_message.Message):
    __slots__ = ("knowledge_contextual_actions", "response_meta")
    KNOWLEDGE_CONTEXTUAL_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    knowledge_contextual_actions: _containers.RepeatedCompositeFieldContainer[KnowledgeContextualAction]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, knowledge_contextual_actions: _Optional[_Iterable[_Union[KnowledgeContextualAction, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class KnowledgeContextualAction(_message.Message):
    __slots__ = ("knowledge_context_action_id", "knowledge_space_action", "knowledge_context_confidence")
    KNOWLEDGE_CONTEXT_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_SPACE_ACTION_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_CONTEXT_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    knowledge_context_action_id: str
    knowledge_space_action: _space_knowledge_pb2.SpaceKnowledgeAction
    knowledge_context_confidence: float
    def __init__(self, knowledge_context_action_id: _Optional[str] = ..., knowledge_space_action: _Optional[_Union[_space_knowledge_pb2.SpaceKnowledgeAction, str]] = ..., knowledge_context_confidence: _Optional[float] = ...) -> None: ...
