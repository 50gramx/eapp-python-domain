from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountAssistantAccessTokenResponse(_message.Message):
    __slots__ = ("account_assistant_services_access_auth_details", "meta")
    ACCOUNT_ASSISTANT_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    account_assistant_services_access_auth_details: AccountAssistantServicesAccessAuthDetails
    meta: _generic_pb2.ResponseMeta
    def __init__(self, account_assistant_services_access_auth_details: _Optional[_Union[AccountAssistantServicesAccessAuthDetails, _Mapping]] = ..., meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class AccountAssistantAccessTokenWithMasterConnectionRequest(_message.Message):
    __slots__ = ("account_assistant_id", "connected_account")
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account_assistant_id: str
    connected_account: _account_assistant_pb2.AccountAssistantConnectedAccount
    def __init__(self, account_assistant_id: _Optional[str] = ..., connected_account: _Optional[_Union[_account_assistant_pb2.AccountAssistantConnectedAccount, _Mapping]] = ...) -> None: ...

class AccessMeta(_message.Message):
    __slots__ = ("access_done", "access_message")
    ACCESS_DONE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    access_done: bool
    access_message: str
    def __init__(self, access_done: bool = ..., access_message: _Optional[str] = ...) -> None: ...

class ValidateAccessMeta(_message.Message):
    __slots__ = ("validation_done", "validation_message")
    VALIDATION_DONE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    validation_done: bool
    validation_message: str
    def __init__(self, validation_done: bool = ..., validation_message: _Optional[str] = ...) -> None: ...

class AccountAssistantServicesAccessAuthDetails(_message.Message):
    __slots__ = ("account_assistant", "account_assistant_services_access_session_token_details", "requested_at")
    ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_SERVICES_ACCESS_SESSION_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    account_assistant: _account_assistant_pb2.AccountAssistant
    account_assistant_services_access_session_token_details: _generic_pb2.PersistentSessionTokenDetails
    requested_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account_assistant: _Optional[_Union[_account_assistant_pb2.AccountAssistant, _Mapping]] = ..., account_assistant_services_access_session_token_details: _Optional[_Union[_generic_pb2.PersistentSessionTokenDetails, _Mapping]] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...
