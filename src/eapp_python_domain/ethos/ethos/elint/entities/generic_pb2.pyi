from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class PictureSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    x20: _ClassVar[PictureSize]
    x29: _ClassVar[PictureSize]
    x40: _ClassVar[PictureSize]
    x60: _ClassVar[PictureSize]
    x76: _ClassVar[PictureSize]
    x83p5: _ClassVar[PictureSize]

class PictureScale(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    x1: _ClassVar[PictureScale]
    x2: _ClassVar[PictureScale]
    x3: _ClassVar[PictureScale]
x20: PictureSize
x29: PictureSize
x40: PictureSize
x60: PictureSize
x76: PictureSize
x83p5: PictureSize
x1: PictureScale
x2: PictureScale
x3: PictureScale

class PersistentSessionTokenDetails(_message.Message):
    __slots__ = ("session_token", "session_scope", "generated_at", "last_used_at", "valid_till")
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SESSION_SCOPE_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    VALID_TILL_FIELD_NUMBER: _ClassVar[int]
    session_token: str
    session_scope: str
    generated_at: _timestamp_pb2.Timestamp
    last_used_at: _timestamp_pb2.Timestamp
    valid_till: _timestamp_pb2.Timestamp
    def __init__(self, session_token: _Optional[str] = ..., session_scope: _Optional[str] = ..., generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_till: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TemporarySessionTokenDetails(_message.Message):
    __slots__ = ("session_token", "session_scope", "generated_at", "valid_till")
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SESSION_SCOPE_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    VALID_TILL_FIELD_NUMBER: _ClassVar[int]
    session_token: str
    session_scope: str
    generated_at: _timestamp_pb2.Timestamp
    valid_till: _timestamp_pb2.Timestamp
    def __init__(self, session_token: _Optional[str] = ..., session_scope: _Optional[str] = ..., generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_till: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PersistentTokenDetails(_message.Message):
    __slots__ = ("token", "generated_at", "last_used_at", "valid_till")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    VALID_TILL_FIELD_NUMBER: _ClassVar[int]
    token: str
    generated_at: _timestamp_pb2.Timestamp
    last_used_at: _timestamp_pb2.Timestamp
    valid_till: _timestamp_pb2.Timestamp
    def __init__(self, token: _Optional[str] = ..., generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_till: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TemporaryTokenDetails(_message.Message):
    __slots__ = ("token", "generated_at", "valid_till")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    VALID_TILL_FIELD_NUMBER: _ClassVar[int]
    token: str
    generated_at: _timestamp_pb2.Timestamp
    valid_till: _timestamp_pb2.Timestamp
    def __init__(self, token: _Optional[str] = ..., generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_till: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ResponseMeta(_message.Message):
    __slots__ = ("meta_done", "meta_message")
    META_DONE_FIELD_NUMBER: _ClassVar[int]
    META_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    meta_done: bool
    meta_message: str
    def __init__(self, meta_done: bool = ..., meta_message: _Optional[str] = ...) -> None: ...
