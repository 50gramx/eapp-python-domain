from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from ethos.elint.services.product.identity.account_assistant import access_account_assistant_pb2 as _access_account_assistant_pb2
from ethos.elint.services.product.conversation.message.account import receive_account_message_pb2 as _receive_account_message_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1_1
from ethos.elint.services.product.conversation.message.account import send_account_message_pb2 as _send_account_message_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAccountAndAssistantConversationsRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account_assistant", "is_account_connected", "connected_account")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    IS_ACCOUNT_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account_assistant: _account_pb2.AccountConnectedAccountAssistant
    is_account_connected: bool
    connected_account: _account_pb2.AccountConnectedAccount
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account_assistant: _Optional[_Union[_account_pb2.AccountConnectedAccountAssistant, _Mapping]] = ..., is_account_connected: bool = ..., connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ...) -> None: ...

class GetAccountAndAssistantConversationsResponse(_message.Message):
    __slots__ = ("account_and_assistant_conversations_messages", "response_meta")
    ACCOUNT_AND_ASSISTANT_CONVERSATIONS_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_and_assistant_conversations_messages: _containers.RepeatedCompositeFieldContainer[AccountAndAssistantConversationsMessages]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_and_assistant_conversations_messages: _Optional[_Iterable[_Union[AccountAndAssistantConversationsMessages, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class AccountAndAssistantConversationsMessages(_message.Message):
    __slots__ = ("is_message_entity_account_assistant", "is_message_sent", "account_assistant_received_message", "account_received_message", "account_assistant_sent_message", "account_sent_message")
    IS_MESSAGE_ENTITY_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    IS_MESSAGE_SENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_RECEIVED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_RECEIVED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    is_message_entity_account_assistant: bool
    is_message_sent: bool
    account_assistant_received_message: _receive_account_message_pb2.AccountAssistantReceivedMessage
    account_received_message: _receive_account_message_pb2.AccountReceivedMessage
    account_assistant_sent_message: _send_account_message_pb2.AccountAssistantSentMessage
    account_sent_message: _send_account_message_pb2.AccountSentMessage
    def __init__(self, is_message_entity_account_assistant: bool = ..., is_message_sent: bool = ..., account_assistant_received_message: _Optional[_Union[_receive_account_message_pb2.AccountAssistantReceivedMessage, _Mapping]] = ..., account_received_message: _Optional[_Union[_receive_account_message_pb2.AccountReceivedMessage, _Mapping]] = ..., account_assistant_sent_message: _Optional[_Union[_send_account_message_pb2.AccountAssistantSentMessage, _Mapping]] = ..., account_sent_message: _Optional[_Union[_send_account_message_pb2.AccountSentMessage, _Mapping]] = ...) -> None: ...

class GetLast24ProductNConversationMessagesRequest(_message.Message):
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

class GetLast24ProductNConversationMessagesResponse(_message.Message):
    __slots__ = ("response_meta", "conversation_messages")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    conversation_messages: _containers.RepeatedCompositeFieldContainer[ConversationMessage]
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., conversation_messages: _Optional[_Iterable[_Union[ConversationMessage, _Mapping]]] = ...) -> None: ...

class GetAccountLastMessageRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account_id: _Optional[str] = ...) -> None: ...

class GetAccountLastMessageResponse(_message.Message):
    __slots__ = ("response_meta", "is_message_sent", "account_received_message", "account_sent_message")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    IS_MESSAGE_SENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_RECEIVED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    is_message_sent: bool
    account_received_message: _receive_account_message_pb2.AccountReceivedMessage
    account_sent_message: _send_account_message_pb2.AccountSentMessage
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., is_message_sent: bool = ..., account_received_message: _Optional[_Union[_receive_account_message_pb2.AccountReceivedMessage, _Mapping]] = ..., account_sent_message: _Optional[_Union[_send_account_message_pb2.AccountSentMessage, _Mapping]] = ...) -> None: ...

class GetAccountAssistantLastMessageRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account_assistant_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account_assistant_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account_assistant_id: _Optional[str] = ...) -> None: ...

class GetAccountAssistantLastMessageResponse(_message.Message):
    __slots__ = ("response_meta", "is_message_sent", "account_assistant_received_message", "account_assistant_sent_message")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    IS_MESSAGE_SENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_RECEIVED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    is_message_sent: bool
    account_assistant_received_message: _receive_account_message_pb2.AccountAssistantReceivedMessage
    account_assistant_sent_message: _send_account_message_pb2.AccountAssistantSentMessage
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., is_message_sent: bool = ..., account_assistant_received_message: _Optional[_Union[_receive_account_message_pb2.AccountAssistantReceivedMessage, _Mapping]] = ..., account_assistant_sent_message: _Optional[_Union[_send_account_message_pb2.AccountAssistantSentMessage, _Mapping]] = ...) -> None: ...

class GetConversedAccountsResponse(_message.Message):
    __slots__ = ("response_meta", "conversed_accounts")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    CONVERSED_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    conversed_accounts: _containers.RepeatedCompositeFieldContainer[_account_pb2.Account]
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., conversed_accounts: _Optional[_Iterable[_Union[_account_pb2.Account, _Mapping]]] = ...) -> None: ...

class GetConversedAccountAssistantsResponse(_message.Message):
    __slots__ = ("response_meta", "conversed_account_assistants")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    CONVERSED_ACCOUNT_ASSISTANTS_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    conversed_account_assistants: _containers.RepeatedCompositeFieldContainer[_account_assistant_pb2.AccountAssistant]
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., conversed_account_assistants: _Optional[_Iterable[_Union[_account_assistant_pb2.AccountAssistant, _Mapping]]] = ...) -> None: ...

class GetConversedAccountAndAssistantsResponse(_message.Message):
    __slots__ = ("response_meta", "conversed_entity_with_last_conversation_message")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    CONVERSED_ENTITY_WITH_LAST_CONVERSATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    conversed_entity_with_last_conversation_message: _containers.RepeatedCompositeFieldContainer[ConversedEntityWithLastConversationMessage]
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., conversed_entity_with_last_conversation_message: _Optional[_Iterable[_Union[ConversedEntityWithLastConversationMessage, _Mapping]]] = ...) -> None: ...

class ConversedEntityWithLastConversationMessage(_message.Message):
    __slots__ = ("conversed_account", "conversed_account_assistant", "last_conversation_message")
    CONVERSED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CONVERSED_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    LAST_CONVERSATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    conversed_account: _account_pb2.Account
    conversed_account_assistant: _account_assistant_pb2.AccountAssistant
    last_conversation_message: ConversationMessage
    def __init__(self, conversed_account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., conversed_account_assistant: _Optional[_Union[_account_assistant_pb2.AccountAssistant, _Mapping]] = ..., last_conversation_message: _Optional[_Union[ConversationMessage, _Mapping]] = ...) -> None: ...

class ConversationMessage(_message.Message):
    __slots__ = ("is_message_entity_account_assistant", "is_message_sent", "account_assistant_received_message", "account_received_message", "account_assistant_sent_message", "account_sent_message")
    IS_MESSAGE_ENTITY_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    IS_MESSAGE_SENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_RECEIVED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_RECEIVED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    is_message_entity_account_assistant: bool
    is_message_sent: bool
    account_assistant_received_message: _receive_account_message_pb2.AccountAssistantReceivedMessage
    account_received_message: _receive_account_message_pb2.AccountReceivedMessage
    account_assistant_sent_message: _send_account_message_pb2.AccountAssistantSentMessage
    account_sent_message: _send_account_message_pb2.AccountSentMessage
    def __init__(self, is_message_entity_account_assistant: bool = ..., is_message_sent: bool = ..., account_assistant_received_message: _Optional[_Union[_receive_account_message_pb2.AccountAssistantReceivedMessage, _Mapping]] = ..., account_received_message: _Optional[_Union[_receive_account_message_pb2.AccountReceivedMessage, _Mapping]] = ..., account_assistant_sent_message: _Optional[_Union[_send_account_message_pb2.AccountAssistantSentMessage, _Mapping]] = ..., account_sent_message: _Optional[_Union[_send_account_message_pb2.AccountSentMessage, _Mapping]] = ...) -> None: ...
