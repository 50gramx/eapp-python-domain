from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_knowledge_pb2 as _space_knowledge_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class MessageFromAccount(_message.Message):
    __slots__ = ("account_assistant_id", "connected_account", "space_knowledge_action", "message", "account_received_message_id")
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_RECEIVED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    account_assistant_id: str
    connected_account: _account_assistant_pb2.AccountAssistantConnectedAccount
    space_knowledge_action: _space_knowledge_pb2.SpaceKnowledgeAction
    message: str
    account_received_message_id: str
    def __init__(self, account_assistant_id: _Optional[str] = ..., connected_account: _Optional[_Union[_account_assistant_pb2.AccountAssistantConnectedAccount, _Mapping]] = ..., space_knowledge_action: _Optional[_Union[_space_knowledge_pb2.SpaceKnowledgeAction, str]] = ..., message: _Optional[str] = ..., account_received_message_id: _Optional[str] = ...) -> None: ...

class MessageFromAccountReceived(_message.Message):
    __slots__ = ("is_received", "received_at")
    IS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    is_received: bool
    received_at: _timestamp_pb2_1_1.Timestamp
    def __init__(self, is_received: bool = ..., received_at: _Optional[_Union[_timestamp_pb2_1_1.Timestamp, _Mapping]] = ...) -> None: ...
