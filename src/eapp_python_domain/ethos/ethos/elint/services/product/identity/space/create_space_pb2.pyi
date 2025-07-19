from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_pb2 as _space_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAccountSpaceRequest(_message.Message):
    __slots__ = ("account", "space_accessibility_type", "space_isolation_type", "requested_at")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SPACE_ACCESSIBILITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ISOLATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    account: _account_pb2.Account
    space_accessibility_type: _space_pb2.SpaceAccessibilityType
    space_isolation_type: _space_pb2.SpaceIsolationType
    requested_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., space_accessibility_type: _Optional[_Union[_space_pb2.SpaceAccessibilityType, str]] = ..., space_isolation_type: _Optional[_Union[_space_pb2.SpaceIsolationType, str]] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class CreateAccountSpaceResponse(_message.Message):
    __slots__ = ("space", "create_account_space_done", "create_account_space_message")
    SPACE_FIELD_NUMBER: _ClassVar[int]
    CREATE_ACCOUNT_SPACE_DONE_FIELD_NUMBER: _ClassVar[int]
    CREATE_ACCOUNT_SPACE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space: _space_pb2.Space
    create_account_space_done: bool
    create_account_space_message: str
    def __init__(self, space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., create_account_space_done: bool = ..., create_account_space_message: _Optional[str] = ...) -> None: ...
