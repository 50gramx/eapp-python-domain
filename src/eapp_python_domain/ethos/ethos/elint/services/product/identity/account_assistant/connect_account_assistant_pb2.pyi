from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.identity.account_assistant import access_account_assistant_pb2 as _access_account_assistant_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IsAccountConnectedRequest(_message.Message):
    __slots__ = ("account_assistant_id", "connected_account")
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account_assistant_id: str
    connected_account: _account_assistant_pb2.AccountAssistantConnectedAccount
    def __init__(self, account_assistant_id: _Optional[str] = ..., connected_account: _Optional[_Union[_account_assistant_pb2.AccountAssistantConnectedAccount, _Mapping]] = ...) -> None: ...

class ConnectAccountRequest(_message.Message):
    __slots__ = ("access_auth_details", "connecting_account_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTING_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails
    connecting_account_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails, _Mapping]] = ..., connecting_account_id: _Optional[str] = ...) -> None: ...

class ConnectAccountResponse(_message.Message):
    __slots__ = ("connected_account", "response_meta")
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    connected_account: _account_assistant_pb2.AccountAssistantConnectedAccount
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, connected_account: _Optional[_Union[_account_assistant_pb2.AccountAssistantConnectedAccount, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...
