from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EAMV7100(_message.Message):
    __slots__ = ("eamvt7100",)
    EAMVT7100_FIELD_NUMBER: _ClassVar[int]
    eamvt7100: str
    def __init__(self, eamvt7100: _Optional[str] = ...) -> None: ...

class EAMV7101(_message.Message):
    __slots__ = ("eamvt7101", "eamvt7102", "eamvt7103", "eamvt7104", "eamvt7105")
    EAMVT7101_FIELD_NUMBER: _ClassVar[int]
    EAMVT7102_FIELD_NUMBER: _ClassVar[int]
    EAMVT7103_FIELD_NUMBER: _ClassVar[int]
    EAMVT7104_FIELD_NUMBER: _ClassVar[int]
    EAMVT7105_FIELD_NUMBER: _ClassVar[int]
    eamvt7101: str
    eamvt7102: str
    eamvt7103: _containers.RepeatedScalarFieldContainer[str]
    eamvt7104: str
    eamvt7105: bool
    def __init__(self, eamvt7101: _Optional[str] = ..., eamvt7102: _Optional[str] = ..., eamvt7103: _Optional[_Iterable[str]] = ..., eamvt7104: _Optional[str] = ..., eamvt7105: bool = ...) -> None: ...

class EAMV7103(_message.Message):
    __slots__ = ("eamvt7111",)
    EAMVT7111_FIELD_NUMBER: _ClassVar[int]
    eamvt7111: _containers.RepeatedCompositeFieldContainer[EAMV7102]
    def __init__(self, eamvt7111: _Optional[_Iterable[_Union[EAMV7102, _Mapping]]] = ...) -> None: ...

class EAMV7102(_message.Message):
    __slots__ = ("eamvt7106", "eamvt7107", "eamvt7108", "eamvt7109", "eamvt7110")
    EAMVT7106_FIELD_NUMBER: _ClassVar[int]
    EAMVT7107_FIELD_NUMBER: _ClassVar[int]
    EAMVT7108_FIELD_NUMBER: _ClassVar[int]
    EAMVT7109_FIELD_NUMBER: _ClassVar[int]
    EAMVT7110_FIELD_NUMBER: _ClassVar[int]
    eamvt7106: str
    eamvt7107: str
    eamvt7108: _containers.RepeatedScalarFieldContainer[str]
    eamvt7109: _containers.RepeatedScalarFieldContainer[str]
    eamvt7110: _timestamp_pb2.Timestamp
    def __init__(self, eamvt7106: _Optional[str] = ..., eamvt7107: _Optional[str] = ..., eamvt7108: _Optional[_Iterable[str]] = ..., eamvt7109: _Optional[_Iterable[str]] = ..., eamvt7110: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EAMV7104(_message.Message):
    __slots__ = ("eamvt7112",)
    EAMVT7112_FIELD_NUMBER: _ClassVar[int]
    eamvt7112: str
    def __init__(self, eamvt7112: _Optional[str] = ...) -> None: ...

class EAMV7105(_message.Message):
    __slots__ = ("eamvt7113", "eamvt7114", "eamvt7115")
    EAMVT7113_FIELD_NUMBER: _ClassVar[int]
    EAMVT7114_FIELD_NUMBER: _ClassVar[int]
    EAMVT7115_FIELD_NUMBER: _ClassVar[int]
    eamvt7113: str
    eamvt7114: str
    eamvt7115: bool
    def __init__(self, eamvt7113: _Optional[str] = ..., eamvt7114: _Optional[str] = ..., eamvt7115: bool = ...) -> None: ...

class EAMV7106(_message.Message):
    __slots__ = ("eamvt7116",)
    EAMVT7116_FIELD_NUMBER: _ClassVar[int]
    eamvt7116: str
    def __init__(self, eamvt7116: _Optional[str] = ...) -> None: ...

class EAMV7107(_message.Message):
    __slots__ = ("eamvt7117", "eamvt7118", "eamvt7119", "eamvt7120", "eamvt7121")
    EAMVT7117_FIELD_NUMBER: _ClassVar[int]
    EAMVT7118_FIELD_NUMBER: _ClassVar[int]
    EAMVT7119_FIELD_NUMBER: _ClassVar[int]
    EAMVT7120_FIELD_NUMBER: _ClassVar[int]
    EAMVT7121_FIELD_NUMBER: _ClassVar[int]
    eamvt7117: str
    eamvt7118: str
    eamvt7119: str
    eamvt7120: str
    eamvt7121: str
    def __init__(self, eamvt7117: _Optional[str] = ..., eamvt7118: _Optional[str] = ..., eamvt7119: _Optional[str] = ..., eamvt7120: _Optional[str] = ..., eamvt7121: _Optional[str] = ...) -> None: ...
