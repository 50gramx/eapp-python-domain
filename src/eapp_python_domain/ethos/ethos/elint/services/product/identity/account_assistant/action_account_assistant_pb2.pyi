from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_knowledge_pb2 as _space_knowledge_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.entities import space_knowledge_domain_pb2 as _space_knowledge_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1_1
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1_1_1
from ethos.elint.services.product.identity.account_assistant import access_account_assistant_pb2 as _access_account_assistant_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActOnAccountMessageRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account", "space_knowledge_action", "message", "act_on_particular_domain", "space_knowledge_domain")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACT_ON_PARTICULAR_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails
    connected_account: _account_assistant_pb2.AccountAssistantConnectedAccount
    space_knowledge_action: _space_knowledge_pb2.SpaceKnowledgeAction
    message: str
    act_on_particular_domain: bool
    space_knowledge_domain: _space_knowledge_domain_pb2.SpaceKnowledgeDomain
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails, _Mapping]] = ..., connected_account: _Optional[_Union[_account_assistant_pb2.AccountAssistantConnectedAccount, _Mapping]] = ..., space_knowledge_action: _Optional[_Union[_space_knowledge_pb2.SpaceKnowledgeAction, str]] = ..., message: _Optional[str] = ..., act_on_particular_domain: bool = ..., space_knowledge_domain: _Optional[_Union[_space_knowledge_domain_pb2.SpaceKnowledgeDomain, _Mapping]] = ...) -> None: ...
