from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import any_pb2 as _any_pb2
from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.identity.account_assistant import access_account_assistant_pb2 as _access_account_assistant_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class MessageForAccount(_message.Message):
    __slots__ = ("access_auth_details", "connected_account", "message", "message_source_space_id", "message_source_space_type_id", "message_source_space_domain_id", "message_source_space_domain_action", "message_source_space_domain_action_context_id", "message_source")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_DOMAIN_ACTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_DOMAIN_ACTION_CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails
    connected_account: _account_assistant_pb2.AccountAssistantConnectedAccount
    message: str
    message_source_space_id: str
    message_source_space_type_id: str
    message_source_space_domain_id: str
    message_source_space_domain_action: int
    message_source_space_domain_action_context_id: str
    message_source: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails, _Mapping]] = ..., connected_account: _Optional[_Union[_account_assistant_pb2.AccountAssistantConnectedAccount, _Mapping]] = ..., message: _Optional[str] = ..., message_source_space_id: _Optional[str] = ..., message_source_space_type_id: _Optional[str] = ..., message_source_space_domain_id: _Optional[str] = ..., message_source_space_domain_action: _Optional[int] = ..., message_source_space_domain_action_context_id: _Optional[str] = ..., message_source: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class MessageForAccountSent(_message.Message):
    __slots__ = ("account_sent_message_id", "is_sent", "sent_at", "received_at")
    ACCOUNT_SENT_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SENT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    account_sent_message_id: str
    is_sent: bool
    sent_at: _timestamp_pb2_1.Timestamp
    received_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account_sent_message_id: _Optional[str] = ..., is_sent: bool = ..., sent_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., received_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...
