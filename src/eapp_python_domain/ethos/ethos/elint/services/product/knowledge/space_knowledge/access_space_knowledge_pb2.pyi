from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_knowledge_pb2 as _space_knowledge_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.services.product.identity.space import access_space_pb2 as _access_space_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceKnowledgeAccessTokenResponse(_message.Message):
    __slots__ = ("space_knowledge_services_access_auth_details", "space_knowledge_services_access_done", "space_knowledge_services_access_message")
    SPACE_KNOWLEDGE_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_SERVICES_ACCESS_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_SERVICES_ACCESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_services_access_auth_details: SpaceKnowledgeServicesAccessAuthDetails
    space_knowledge_services_access_done: bool
    space_knowledge_services_access_message: str
    def __init__(self, space_knowledge_services_access_auth_details: _Optional[_Union[SpaceKnowledgeServicesAccessAuthDetails, _Mapping]] = ..., space_knowledge_services_access_done: bool = ..., space_knowledge_services_access_message: _Optional[str] = ...) -> None: ...

class ValidateSpaceKnowledgeServicesResponse(_message.Message):
    __slots__ = ("space_knowledge_services_access_validation_done", "space_knowledge_services_access_validation_message")
    SPACE_KNOWLEDGE_SERVICES_ACCESS_VALIDATION_DONE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_SERVICES_ACCESS_VALIDATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_services_access_validation_done: bool
    space_knowledge_services_access_validation_message: str
    def __init__(self, space_knowledge_services_access_validation_done: bool = ..., space_knowledge_services_access_validation_message: _Optional[str] = ...) -> None: ...

class SpaceKnowledgeServicesAccessAuthDetails(_message.Message):
    __slots__ = ("space_knowledge", "space_knowledge_services_access_session_token_details", "requested_at")
    SPACE_KNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_SERVICES_ACCESS_SESSION_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    space_knowledge: _space_knowledge_pb2.SpaceKnowledge
    space_knowledge_services_access_session_token_details: _generic_pb2.PersistentSessionTokenDetails
    requested_at: _timestamp_pb2_1_1.Timestamp
    def __init__(self, space_knowledge: _Optional[_Union[_space_knowledge_pb2.SpaceKnowledge, _Mapping]] = ..., space_knowledge_services_access_session_token_details: _Optional[_Union[_generic_pb2.PersistentSessionTokenDetails, _Mapping]] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1_1.Timestamp, _Mapping]] = ...) -> None: ...
