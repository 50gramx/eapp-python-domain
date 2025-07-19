from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import any_pb2 as _any_pb2
from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1_1
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class MessageFromAccountAssistant(_message.Message):
    __slots__ = ("account_id", "connected_account_assistant", "message", "message_source_space_id", "message_source_space_type_id", "message_source_space_domain_id", "message_source_space_domain_action", "message_source_space_domain_action_context_id", "message_source", "account_assistant_received_message_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_DOMAIN_ACTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_DOMAIN_ACTION_CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_RECEIVED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    connected_account_assistant: _account_pb2.AccountConnectedAccountAssistant
    message: str
    message_source_space_id: str
    message_source_space_type_id: str
    message_source_space_domain_id: str
    message_source_space_domain_action: int
    message_source_space_domain_action_context_id: str
    message_source: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    account_assistant_received_message_id: str
    def __init__(self, account_id: _Optional[str] = ..., connected_account_assistant: _Optional[_Union[_account_pb2.AccountConnectedAccountAssistant, _Mapping]] = ..., message: _Optional[str] = ..., message_source_space_id: _Optional[str] = ..., message_source_space_type_id: _Optional[str] = ..., message_source_space_domain_id: _Optional[str] = ..., message_source_space_domain_action: _Optional[int] = ..., message_source_space_domain_action_context_id: _Optional[str] = ..., message_source: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., account_assistant_received_message_id: _Optional[str] = ...) -> None: ...

class MessageFromAccountAssistantReceived(_message.Message):
    __slots__ = ("is_received", "received_at")
    IS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    is_received: bool
    received_at: _timestamp_pb2_1_1_1.Timestamp
    def __init__(self, is_received: bool = ..., received_at: _Optional[_Union[_timestamp_pb2_1_1_1.Timestamp, _Mapping]] = ...) -> None: ...

class MessageFromAccount(_message.Message):
    __slots__ = ("account_id", "connected_account", "message", "account_received_message_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_RECEIVED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    connected_account: _account_pb2.AccountConnectedAccount
    message: str
    account_received_message_id: str
    def __init__(self, account_id: _Optional[str] = ..., connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ..., message: _Optional[str] = ..., account_received_message_id: _Optional[str] = ...) -> None: ...

class MessageFromAccountReceived(_message.Message):
    __slots__ = ("is_received", "received_at")
    IS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    is_received: bool
    received_at: _timestamp_pb2_1_1_1.Timestamp
    def __init__(self, is_received: bool = ..., received_at: _Optional[_Union[_timestamp_pb2_1_1_1.Timestamp, _Mapping]] = ...) -> None: ...

class SyncAccountReceivedMessagesResponse(_message.Message):
    __slots__ = ("account_received_message", "response_meta")
    ACCOUNT_RECEIVED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_received_message: AccountReceivedMessage
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_received_message: _Optional[_Union[AccountReceivedMessage, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class SyncAccountConnectedAccountReceivedMessagesRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account: _account_pb2.AccountConnectedAccount
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ...) -> None: ...

class SyncAccountConnectedAccountReceivedMessagesResponse(_message.Message):
    __slots__ = ("account_received_message", "response_meta", "sync_progress")
    ACCOUNT_RECEIVED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    SYNC_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    account_received_message: AccountReceivedMessage
    response_meta: _generic_pb2.ResponseMeta
    sync_progress: float
    def __init__(self, account_received_message: _Optional[_Union[AccountReceivedMessage, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., sync_progress: _Optional[float] = ...) -> None: ...

class SyncAccountConnectedAccountAssistantReceivedMessagesRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account_assistant")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account_assistant: _account_pb2.AccountConnectedAccountAssistant
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account_assistant: _Optional[_Union[_account_pb2.AccountConnectedAccountAssistant, _Mapping]] = ...) -> None: ...

class SyncAccountConnectedAccountAssistantReceivedMessagesResponse(_message.Message):
    __slots__ = ("account_assistant_received_message", "response_meta", "sync_progress")
    ACCOUNT_ASSISTANT_RECEIVED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    SYNC_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    account_assistant_received_message: AccountAssistantReceivedMessage
    response_meta: _generic_pb2.ResponseMeta
    sync_progress: float
    def __init__(self, account_assistant_received_message: _Optional[_Union[AccountAssistantReceivedMessage, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., sync_progress: _Optional[float] = ...) -> None: ...

class ListenForReceivedAccountAssistantMessagesRequest(_message.Message):
    __slots__ = ("access_auth_details",)
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ...) -> None: ...

class ListenForReceivedAccountAssistantMessagesResponse(_message.Message):
    __slots__ = ("messages_from_account_assistant", "response_meta")
    MESSAGES_FROM_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    messages_from_account_assistant: _containers.RepeatedCompositeFieldContainer[MessageFromAccountAssistant]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, messages_from_account_assistant: _Optional[_Iterable[_Union[MessageFromAccountAssistant, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ListenForReceivedAccountMessagesRequest(_message.Message):
    __slots__ = ("access_auth_details",)
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ...) -> None: ...

class ListenForReceivedAccountMessagesResponse(_message.Message):
    __slots__ = ("messages_from_account", "response_meta")
    MESSAGES_FROM_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    messages_from_account: _containers.RepeatedCompositeFieldContainer[MessageFromAccount]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, messages_from_account: _Optional[_Iterable[_Union[MessageFromAccount, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ListenForReceivedAccountSpeedMessagesResponse(_message.Message):
    __slots__ = ("messages_from_account", "response_meta")
    MESSAGES_FROM_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    messages_from_account: MessageFromAccount
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, messages_from_account: _Optional[_Union[MessageFromAccount, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ListenForReceivedAccountAssistantSpeedMessagesResponse(_message.Message):
    __slots__ = ("message_from_account_assistant", "response_meta")
    MESSAGE_FROM_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    message_from_account_assistant: MessageFromAccountAssistant
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, message_from_account_assistant: _Optional[_Union[MessageFromAccountAssistant, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetLast24ProductNReceivedMessagesRequest(_message.Message):
    __slots__ = ("access_auth_details", "product_n", "message_entity_enum", "connected_account_assistant", "connected_account")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_N_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ENTITY_ENUM_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    product_n: int
    message_entity_enum: _account_pb2.MessageEntity
    connected_account_assistant: _account_pb2.AccountConnectedAccountAssistant
    connected_account: _account_pb2.AccountConnectedAccount
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., product_n: _Optional[int] = ..., message_entity_enum: _Optional[_Union[_account_pb2.MessageEntity, str]] = ..., connected_account_assistant: _Optional[_Union[_account_pb2.AccountConnectedAccountAssistant, _Mapping]] = ..., connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ...) -> None: ...

class GetLast24ProductNReceivedMessagesResponse(_message.Message):
    __slots__ = ("response_meta", "account_received_messages", "account_assistant_received_messages")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_RECEIVED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_RECEIVED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    account_received_messages: _containers.RepeatedCompositeFieldContainer[AccountReceivedMessage]
    account_assistant_received_messages: _containers.RepeatedCompositeFieldContainer[AccountAssistantReceivedMessage]
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., account_received_messages: _Optional[_Iterable[_Union[AccountReceivedMessage, _Mapping]]] = ..., account_assistant_received_messages: _Optional[_Iterable[_Union[AccountAssistantReceivedMessage, _Mapping]]] = ...) -> None: ...

class GetAccountLastReceivedMessageRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account_id: _Optional[str] = ...) -> None: ...

class GetAccountLastReceivedMessageResponse(_message.Message):
    __slots__ = ("response_meta", "last_received_message")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    LAST_RECEIVED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    last_received_message: AccountReceivedMessage
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., last_received_message: _Optional[_Union[AccountReceivedMessage, _Mapping]] = ...) -> None: ...

class GetAccountAssistantLastReceivedMessageRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account_assistant_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account_assistant_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account_assistant_id: _Optional[str] = ...) -> None: ...

class GetAccountAssistantLastReceivedMessageResponse(_message.Message):
    __slots__ = ("response_meta", "last_received_message")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    LAST_RECEIVED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    last_received_message: AccountAssistantReceivedMessage
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., last_received_message: _Optional[_Union[AccountAssistantReceivedMessage, _Mapping]] = ...) -> None: ...

class GetReceivedMessagesAccountsResponse(_message.Message):
    __slots__ = ("response_meta", "received_messages_accounts")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_MESSAGES_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    received_messages_accounts: _containers.RepeatedCompositeFieldContainer[_account_pb2.Account]
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., received_messages_accounts: _Optional[_Iterable[_Union[_account_pb2.Account, _Mapping]]] = ...) -> None: ...

class GetReceivedMessagesAccountAssistantsResponse(_message.Message):
    __slots__ = ("response_meta", "received_messages_account_assistants")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_MESSAGES_ACCOUNT_ASSISTANTS_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    received_messages_account_assistants: _containers.RepeatedCompositeFieldContainer[_account_assistant_pb2.AccountAssistant]
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., received_messages_account_assistants: _Optional[_Iterable[_Union[_account_assistant_pb2.AccountAssistant, _Mapping]]] = ...) -> None: ...

class AccountAssistantReceivedMessage(_message.Message):
    __slots__ = ("account_assistant_received_message_id", "account_assistant_id", "account_assistant_connection_id", "message", "message_source_space_id", "message_source_space_type_id", "message_source_space_domain_id", "message_source_space_domain_action", "message_source_space_domain_action_context_id", "received_at")
    ACCOUNT_ASSISTANT_RECEIVED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_DOMAIN_ACTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SOURCE_SPACE_DOMAIN_ACTION_CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    account_assistant_received_message_id: str
    account_assistant_id: str
    account_assistant_connection_id: str
    message: str
    message_source_space_id: str
    message_source_space_type_id: str
    message_source_space_domain_id: str
    message_source_space_domain_action: int
    message_source_space_domain_action_context_id: str
    received_at: _timestamp_pb2_1_1_1.Timestamp
    def __init__(self, account_assistant_received_message_id: _Optional[str] = ..., account_assistant_id: _Optional[str] = ..., account_assistant_connection_id: _Optional[str] = ..., message: _Optional[str] = ..., message_source_space_id: _Optional[str] = ..., message_source_space_type_id: _Optional[str] = ..., message_source_space_domain_id: _Optional[str] = ..., message_source_space_domain_action: _Optional[int] = ..., message_source_space_domain_action_context_id: _Optional[str] = ..., received_at: _Optional[_Union[_timestamp_pb2_1_1_1.Timestamp, _Mapping]] = ...) -> None: ...

class AccountReceivedMessage(_message.Message):
    __slots__ = ("account_received_message_id", "account_id", "account_connection_id", "message", "received_at")
    ACCOUNT_RECEIVED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    account_received_message_id: str
    account_id: str
    account_connection_id: str
    message: str
    received_at: _timestamp_pb2_1_1_1.Timestamp
    def __init__(self, account_received_message_id: _Optional[str] = ..., account_id: _Optional[str] = ..., account_connection_id: _Optional[str] = ..., message: _Optional[str] = ..., received_at: _Optional[_Union[_timestamp_pb2_1_1_1.Timestamp, _Mapping]] = ...) -> None: ...

class AccountReceivedMessagesCountResponse(_message.Message):
    __slots__ = ("account_received_messages_count", "response_meta")
    ACCOUNT_RECEIVED_MESSAGES_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_received_messages_count: int
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_received_messages_count: _Optional[int] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class AccountAssistantReceivedMessagesCountResponse(_message.Message):
    __slots__ = ("account_assistant_received_messages_count", "response_meta")
    ACCOUNT_ASSISTANT_RECEIVED_MESSAGES_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_assistant_received_messages_count: int
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_assistant_received_messages_count: _Optional[int] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...
