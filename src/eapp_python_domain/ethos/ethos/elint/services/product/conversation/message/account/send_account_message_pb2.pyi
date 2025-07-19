from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.entities import space_knowledge_pb2 as _space_knowledge_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1_1
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1_1_1
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class MessageForAccountAssistant(_message.Message):
    __slots__ = ("access_auth_details", "connected_account_assistant", "space_knowledge_action", "message")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account_assistant: _account_pb2.AccountConnectedAccountAssistant
    space_knowledge_action: _space_knowledge_pb2.SpaceKnowledgeAction
    message: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account_assistant: _Optional[_Union[_account_pb2.AccountConnectedAccountAssistant, _Mapping]] = ..., space_knowledge_action: _Optional[_Union[_space_knowledge_pb2.SpaceKnowledgeAction, str]] = ..., message: _Optional[str] = ...) -> None: ...

class MessageForAccountAssistantSent(_message.Message):
    __slots__ = ("account_assistant_sent_message_id", "is_sent", "sent_at", "received_at")
    ACCOUNT_ASSISTANT_SENT_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SENT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    account_assistant_sent_message_id: str
    is_sent: bool
    sent_at: _timestamp_pb2_1_1_1_1.Timestamp
    received_at: _timestamp_pb2_1_1_1_1.Timestamp
    def __init__(self, account_assistant_sent_message_id: _Optional[str] = ..., is_sent: bool = ..., sent_at: _Optional[_Union[_timestamp_pb2_1_1_1_1.Timestamp, _Mapping]] = ..., received_at: _Optional[_Union[_timestamp_pb2_1_1_1_1.Timestamp, _Mapping]] = ...) -> None: ...

class MessageForAccount(_message.Message):
    __slots__ = ("access_auth_details", "connected_account", "message")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account: _account_pb2.AccountConnectedAccount
    message: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class MessageForAccountSent(_message.Message):
    __slots__ = ("account_sent_message_id", "is_sent", "sent_at", "received_at")
    ACCOUNT_SENT_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SENT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    account_sent_message_id: str
    is_sent: bool
    sent_at: _timestamp_pb2_1_1_1_1.Timestamp
    received_at: _timestamp_pb2_1_1_1_1.Timestamp
    def __init__(self, account_sent_message_id: _Optional[str] = ..., is_sent: bool = ..., sent_at: _Optional[_Union[_timestamp_pb2_1_1_1_1.Timestamp, _Mapping]] = ..., received_at: _Optional[_Union[_timestamp_pb2_1_1_1_1.Timestamp, _Mapping]] = ...) -> None: ...

class FullMessageForAccountSent(_message.Message):
    __slots__ = ("message_for_account_sent", "connected_account", "message")
    MESSAGE_FOR_ACCOUNT_SENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message_for_account_sent: MessageForAccountSent
    connected_account: _account_pb2.AccountConnectedAccount
    message: str
    def __init__(self, message_for_account_sent: _Optional[_Union[MessageForAccountSent, _Mapping]] = ..., connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class SyncAccountSentMessagesResponse(_message.Message):
    __slots__ = ("account_sent_message", "response_meta")
    ACCOUNT_SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_sent_message: AccountSentMessage
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_sent_message: _Optional[_Union[AccountSentMessage, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class SyncAccountConnectedAccountSentMessagesRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account: _account_pb2.AccountConnectedAccount
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ...) -> None: ...

class SyncAccountConnectedAccountSentMessagesResponse(_message.Message):
    __slots__ = ("account_sent_message", "response_meta", "sync_progress")
    ACCOUNT_SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    SYNC_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    account_sent_message: AccountSentMessage
    response_meta: _generic_pb2.ResponseMeta
    sync_progress: float
    def __init__(self, account_sent_message: _Optional[_Union[AccountSentMessage, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., sync_progress: _Optional[float] = ...) -> None: ...

class SyncAccountConnectedAccountAssistantSentMessagesRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account_assistant")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account_assistant: _account_pb2.AccountConnectedAccountAssistant
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account_assistant: _Optional[_Union[_account_pb2.AccountConnectedAccountAssistant, _Mapping]] = ...) -> None: ...

class SyncAccountConnectedAccountAssistantSentMessagesResponse(_message.Message):
    __slots__ = ("account_assistant_sent_message", "response_meta", "sync_progress")
    ACCOUNT_ASSISTANT_SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    SYNC_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    account_assistant_sent_message: AccountAssistantSentMessage
    response_meta: _generic_pb2.ResponseMeta
    sync_progress: float
    def __init__(self, account_assistant_sent_message: _Optional[_Union[AccountAssistantSentMessage, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., sync_progress: _Optional[float] = ...) -> None: ...

class GetLast24ProductNSentMessagesRequest(_message.Message):
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

class GetLast24ProductNSentMessagesResponse(_message.Message):
    __slots__ = ("response_meta", "account_sent_messages", "account_assistant_sent_messages")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_SENT_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_SENT_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    account_sent_messages: _containers.RepeatedCompositeFieldContainer[AccountSentMessage]
    account_assistant_sent_messages: _containers.RepeatedCompositeFieldContainer[AccountAssistantSentMessage]
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., account_sent_messages: _Optional[_Iterable[_Union[AccountSentMessage, _Mapping]]] = ..., account_assistant_sent_messages: _Optional[_Iterable[_Union[AccountAssistantSentMessage, _Mapping]]] = ...) -> None: ...

class GetAccountLastSentMessageRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account_id: _Optional[str] = ...) -> None: ...

class GetAccountLastSentMessageResponse(_message.Message):
    __slots__ = ("response_meta", "last_sent_message")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    LAST_SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    last_sent_message: AccountSentMessage
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., last_sent_message: _Optional[_Union[AccountSentMessage, _Mapping]] = ...) -> None: ...

class GetAccountAssistantLastSentMessageRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account_assistant_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account_assistant_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account_assistant_id: _Optional[str] = ...) -> None: ...

class GetAccountAssistantLastSentMessageResponse(_message.Message):
    __slots__ = ("response_meta", "last_sent_message")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    LAST_SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    last_sent_message: AccountAssistantSentMessage
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., last_sent_message: _Optional[_Union[AccountAssistantSentMessage, _Mapping]] = ...) -> None: ...

class GetSentMessagesAccountsResponse(_message.Message):
    __slots__ = ("response_meta", "sent_messages_accounts")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    SENT_MESSAGES_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    sent_messages_accounts: _containers.RepeatedCompositeFieldContainer[_account_pb2.Account]
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., sent_messages_accounts: _Optional[_Iterable[_Union[_account_pb2.Account, _Mapping]]] = ...) -> None: ...

class GetSentMessagesAccountAssistantsResponse(_message.Message):
    __slots__ = ("response_meta", "sent_messages_account_assistants")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    SENT_MESSAGES_ACCOUNT_ASSISTANTS_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    sent_messages_account_assistants: _containers.RepeatedCompositeFieldContainer[_account_assistant_pb2.AccountAssistant]
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., sent_messages_account_assistants: _Optional[_Iterable[_Union[_account_assistant_pb2.AccountAssistant, _Mapping]]] = ...) -> None: ...

class AccountAssistantSentMessage(_message.Message):
    __slots__ = ("account_assistant_sent_message_id", "account_assistant_id", "account_assistant_connection_id", "message", "message_space", "message_space_action", "sent_at", "received_at", "message_info")
    ACCOUNT_ASSISTANT_SENT_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SPACE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SPACE_ACTION_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    account_assistant_sent_message_id: str
    account_assistant_id: str
    account_assistant_connection_id: str
    message: str
    message_space: int
    message_space_action: int
    sent_at: _timestamp_pb2_1_1_1_1.Timestamp
    received_at: _timestamp_pb2_1_1_1_1.Timestamp
    message_info: _account_pb2.MessageInfo
    def __init__(self, account_assistant_sent_message_id: _Optional[str] = ..., account_assistant_id: _Optional[str] = ..., account_assistant_connection_id: _Optional[str] = ..., message: _Optional[str] = ..., message_space: _Optional[int] = ..., message_space_action: _Optional[int] = ..., sent_at: _Optional[_Union[_timestamp_pb2_1_1_1_1.Timestamp, _Mapping]] = ..., received_at: _Optional[_Union[_timestamp_pb2_1_1_1_1.Timestamp, _Mapping]] = ..., message_info: _Optional[_Union[_account_pb2.MessageInfo, _Mapping]] = ...) -> None: ...

class AccountSentMessage(_message.Message):
    __slots__ = ("account_sent_message_id", "account_id", "account_connection_id", "message", "sent_at", "received_at", "message_info")
    ACCOUNT_SENT_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    account_sent_message_id: str
    account_id: str
    account_connection_id: str
    message: str
    sent_at: _timestamp_pb2_1_1_1_1.Timestamp
    received_at: _timestamp_pb2_1_1_1_1.Timestamp
    message_info: _account_pb2.MessageInfo
    def __init__(self, account_sent_message_id: _Optional[str] = ..., account_id: _Optional[str] = ..., account_connection_id: _Optional[str] = ..., message: _Optional[str] = ..., sent_at: _Optional[_Union[_timestamp_pb2_1_1_1_1.Timestamp, _Mapping]] = ..., received_at: _Optional[_Union[_timestamp_pb2_1_1_1_1.Timestamp, _Mapping]] = ..., message_info: _Optional[_Union[_account_pb2.MessageInfo, _Mapping]] = ...) -> None: ...

class AccountSentMessagesCountResponse(_message.Message):
    __slots__ = ("account_sent_messages_count", "response_meta")
    ACCOUNT_SENT_MESSAGES_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_sent_messages_count: int
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_sent_messages_count: _Optional[int] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class AccountAssistantSentMessagesCountResponse(_message.Message):
    __slots__ = ("account_assistant_sent_messages_count", "response_meta")
    ACCOUNT_ASSISTANT_SENT_MESSAGES_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_assistant_sent_messages_count: int
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_assistant_sent_messages_count: _Optional[int] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...
