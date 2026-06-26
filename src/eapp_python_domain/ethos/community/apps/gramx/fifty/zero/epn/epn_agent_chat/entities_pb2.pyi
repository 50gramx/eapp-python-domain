from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EAMV6001(_message.Message):
    __slots__ = ("eamvt6001", "eamvt6002", "eamvt6003")
    EAMVT6001_FIELD_NUMBER: _ClassVar[int]
    EAMVT6002_FIELD_NUMBER: _ClassVar[int]
    EAMVT6003_FIELD_NUMBER: _ClassVar[int]
    eamvt6001: str
    eamvt6002: str
    eamvt6003: str
    def __init__(self, eamvt6001: _Optional[str] = ..., eamvt6002: _Optional[str] = ..., eamvt6003: _Optional[str] = ...) -> None: ...

class EAMV6002(_message.Message):
    __slots__ = ("eamvt6004", "eamvt6005", "eamvt6006", "eamvt6007")
    EAMVT6004_FIELD_NUMBER: _ClassVar[int]
    EAMVT6005_FIELD_NUMBER: _ClassVar[int]
    EAMVT6006_FIELD_NUMBER: _ClassVar[int]
    EAMVT6007_FIELD_NUMBER: _ClassVar[int]
    eamvt6004: EAMV6003
    eamvt6005: EAMV6004
    eamvt6006: EAMV6005
    eamvt6007: EAMV6006
    def __init__(self, eamvt6004: _Optional[_Union[EAMV6003, _Mapping]] = ..., eamvt6005: _Optional[_Union[EAMV6004, _Mapping]] = ..., eamvt6006: _Optional[_Union[EAMV6005, _Mapping]] = ..., eamvt6007: _Optional[_Union[EAMV6006, _Mapping]] = ...) -> None: ...

class EAMV6003(_message.Message):
    __slots__ = ("eamvt6008",)
    EAMVT6008_FIELD_NUMBER: _ClassVar[int]
    eamvt6008: str
    def __init__(self, eamvt6008: _Optional[str] = ...) -> None: ...

class EAMV6004(_message.Message):
    __slots__ = ("eamvt6009", "eamvt6010", "eamvt6011")
    EAMVT6009_FIELD_NUMBER: _ClassVar[int]
    EAMVT6010_FIELD_NUMBER: _ClassVar[int]
    EAMVT6011_FIELD_NUMBER: _ClassVar[int]
    eamvt6009: str
    eamvt6010: str
    eamvt6011: str
    def __init__(self, eamvt6009: _Optional[str] = ..., eamvt6010: _Optional[str] = ..., eamvt6011: _Optional[str] = ...) -> None: ...

class EAMV6005(_message.Message):
    __slots__ = ("eamvt6012", "eamvt6013", "eamvt6014")
    EAMVT6012_FIELD_NUMBER: _ClassVar[int]
    EAMVT6013_FIELD_NUMBER: _ClassVar[int]
    EAMVT6014_FIELD_NUMBER: _ClassVar[int]
    eamvt6012: str
    eamvt6013: str
    eamvt6014: bool
    def __init__(self, eamvt6012: _Optional[str] = ..., eamvt6013: _Optional[str] = ..., eamvt6014: bool = ...) -> None: ...

class EAMV6006(_message.Message):
    __slots__ = ("eamvt6015", "eamvt6016")
    EAMVT6015_FIELD_NUMBER: _ClassVar[int]
    EAMVT6016_FIELD_NUMBER: _ClassVar[int]
    eamvt6015: str
    eamvt6016: str
    def __init__(self, eamvt6015: _Optional[str] = ..., eamvt6016: _Optional[str] = ...) -> None: ...
