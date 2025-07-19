from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class AccountAssistant(_message.Message):
    __slots__ = ("account_assistant_id", "account_assistant_name_code", "account_assistant_name", "account", "created_at", "last_assisted_at")
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_NAME_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ASSISTED_AT_FIELD_NUMBER: _ClassVar[int]
    account_assistant_id: str
    account_assistant_name_code: int
    account_assistant_name: str
    account: _account_pb2.Account
    created_at: _timestamp_pb2_1.Timestamp
    last_assisted_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account_assistant_id: _Optional[str] = ..., account_assistant_name_code: _Optional[int] = ..., account_assistant_name: _Optional[str] = ..., account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., last_assisted_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class AccountAssistantConnectedAccount(_message.Message):
    __slots__ = ("account_connection_id", "account_id", "connected_at")
    ACCOUNT_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_AT_FIELD_NUMBER: _ClassVar[int]
    account_connection_id: str
    account_id: str
    connected_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account_connection_id: _Optional[str] = ..., account_id: _Optional[str] = ..., connected_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class AccountAssistantConnectedAccountAssistant(_message.Message):
    __slots__ = ("account_assistant_connection_id", "account_assistant_id", "connected_at")
    ACCOUNT_ASSISTANT_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_AT_FIELD_NUMBER: _ClassVar[int]
    account_assistant_connection_id: str
    account_assistant_id: str
    connected_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account_assistant_connection_id: _Optional[str] = ..., account_assistant_id: _Optional[str] = ..., connected_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class AccountAssistantMeta(_message.Message):
    __slots__ = ("account_assistant_id", "account_assistant_name_code", "account_assistant_name", "account_id")
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_NAME_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_assistant_id: str
    account_assistant_name_code: int
    account_assistant_name: str
    account_id: str
    def __init__(self, account_assistant_id: _Optional[str] = ..., account_assistant_name_code: _Optional[int] = ..., account_assistant_name: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...
