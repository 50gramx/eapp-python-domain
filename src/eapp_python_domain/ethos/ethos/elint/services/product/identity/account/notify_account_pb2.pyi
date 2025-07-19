from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NewReceivedMessageFromAccountAssistantRequest(_message.Message):
    __slots__ = ("account_id", "connecting_account_assistant_id", "message")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTING_ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    connecting_account_assistant_id: str
    message: str
    def __init__(self, account_id: _Optional[str] = ..., connecting_account_assistant_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class NewReceivedMessageFromAccountRequest(_message.Message):
    __slots__ = ("account_id", "connecting_account_id", "message")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTING_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    connecting_account_id: str
    message: str
    def __init__(self, account_id: _Optional[str] = ..., connecting_account_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class AccountConnectedAccountNotificationRequest(_message.Message):
    __slots__ = ("account", "connecting_account_connected_account")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CONNECTING_ACCOUNT_CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: _account_pb2.Account
    connecting_account_connected_account: _account_pb2.AccountConnectedAccount
    def __init__(self, account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., connecting_account_connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ...) -> None: ...

class UpdateAccountDeviceDetailsRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_device_details")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_device_details: _account_pb2.AccountDeviceDetails
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_device_details: _Optional[_Union[_account_pb2.AccountDeviceDetails, _Mapping]] = ...) -> None: ...
