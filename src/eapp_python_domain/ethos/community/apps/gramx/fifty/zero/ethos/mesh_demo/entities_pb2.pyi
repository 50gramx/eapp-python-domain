from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EAMV8002(_message.Message):
    __slots__ = ("eamvt8004",)
    EAMVT8004_FIELD_NUMBER: _ClassVar[int]
    eamvt8004: str
    def __init__(self, eamvt8004: _Optional[str] = ...) -> None: ...

class EAMV8001(_message.Message):
    __slots__ = ("eamvt8001", "eamvt8002", "eamvt8003", "eamvt8028", "eamvt8029", "eamvt8007", "eamvt8008", "eamvt8009", "eamvt8010", "eamvt8011", "eamvt8012", "eamvt8013", "eamvt8014", "eamvt8015", "eamvt8016", "eamvt8017", "eamvt8018", "eamvt8019", "eamvt8020", "eamvt8021", "eamvt8022", "eamvt8023", "eamvt8024", "eamvt8025", "eamvt8030", "eamvt8031")
    EAMVT8001_FIELD_NUMBER: _ClassVar[int]
    EAMVT8002_FIELD_NUMBER: _ClassVar[int]
    EAMVT8003_FIELD_NUMBER: _ClassVar[int]
    EAMVT8028_FIELD_NUMBER: _ClassVar[int]
    EAMVT8029_FIELD_NUMBER: _ClassVar[int]
    EAMVT8007_FIELD_NUMBER: _ClassVar[int]
    EAMVT8008_FIELD_NUMBER: _ClassVar[int]
    EAMVT8009_FIELD_NUMBER: _ClassVar[int]
    EAMVT8010_FIELD_NUMBER: _ClassVar[int]
    EAMVT8011_FIELD_NUMBER: _ClassVar[int]
    EAMVT8012_FIELD_NUMBER: _ClassVar[int]
    EAMVT8013_FIELD_NUMBER: _ClassVar[int]
    EAMVT8014_FIELD_NUMBER: _ClassVar[int]
    EAMVT8015_FIELD_NUMBER: _ClassVar[int]
    EAMVT8016_FIELD_NUMBER: _ClassVar[int]
    EAMVT8017_FIELD_NUMBER: _ClassVar[int]
    EAMVT8018_FIELD_NUMBER: _ClassVar[int]
    EAMVT8019_FIELD_NUMBER: _ClassVar[int]
    EAMVT8020_FIELD_NUMBER: _ClassVar[int]
    EAMVT8021_FIELD_NUMBER: _ClassVar[int]
    EAMVT8022_FIELD_NUMBER: _ClassVar[int]
    EAMVT8023_FIELD_NUMBER: _ClassVar[int]
    EAMVT8024_FIELD_NUMBER: _ClassVar[int]
    EAMVT8025_FIELD_NUMBER: _ClassVar[int]
    EAMVT8030_FIELD_NUMBER: _ClassVar[int]
    EAMVT8031_FIELD_NUMBER: _ClassVar[int]
    eamvt8001: str
    eamvt8002: str
    eamvt8003: str
    eamvt8028: float
    eamvt8029: float
    eamvt8007: int
    eamvt8008: bool
    eamvt8009: bytes
    eamvt8010: EAMV8003
    eamvt8011: int
    eamvt8012: int
    eamvt8013: int
    eamvt8014: int
    eamvt8015: int
    eamvt8016: int
    eamvt8017: int
    eamvt8018: int
    eamvt8019: int
    eamvt8020: _timestamp_pb2.Timestamp
    eamvt8021: _duration_pb2.Duration
    eamvt8022: _empty_pb2.Empty
    eamvt8023: _struct_pb2.Struct
    eamvt8024: _any_pb2.Any
    eamvt8025: _field_mask_pb2.FieldMask
    eamvt8030: _struct_pb2.ListValue
    eamvt8031: EAMV8002
    def __init__(self, eamvt8001: _Optional[str] = ..., eamvt8002: _Optional[str] = ..., eamvt8003: _Optional[str] = ..., eamvt8028: _Optional[float] = ..., eamvt8029: _Optional[float] = ..., eamvt8007: _Optional[int] = ..., eamvt8008: bool = ..., eamvt8009: _Optional[bytes] = ..., eamvt8010: _Optional[_Union[EAMV8003, _Mapping]] = ..., eamvt8011: _Optional[int] = ..., eamvt8012: _Optional[int] = ..., eamvt8013: _Optional[int] = ..., eamvt8014: _Optional[int] = ..., eamvt8015: _Optional[int] = ..., eamvt8016: _Optional[int] = ..., eamvt8017: _Optional[int] = ..., eamvt8018: _Optional[int] = ..., eamvt8019: _Optional[int] = ..., eamvt8020: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., eamvt8021: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., eamvt8022: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., eamvt8023: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., eamvt8024: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., eamvt8025: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., eamvt8030: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., eamvt8031: _Optional[_Union[EAMV8002, _Mapping]] = ...) -> None: ...

class EAMV8003(_message.Message):
    __slots__ = ("eamvt8005", "eamvt8032")
    EAMVT8005_FIELD_NUMBER: _ClassVar[int]
    EAMVT8032_FIELD_NUMBER: _ClassVar[int]
    eamvt8005: str
    eamvt8032: float
    def __init__(self, eamvt8005: _Optional[str] = ..., eamvt8032: _Optional[float] = ...) -> None: ...

class EAMV8004(_message.Message):
    __slots__ = ("eamvt8033", "eamvt8034", "eamvt8035")
    EAMVT8033_FIELD_NUMBER: _ClassVar[int]
    EAMVT8034_FIELD_NUMBER: _ClassVar[int]
    EAMVT8035_FIELD_NUMBER: _ClassVar[int]
    eamvt8033: str
    eamvt8034: bool
    eamvt8035: int
    def __init__(self, eamvt8033: _Optional[str] = ..., eamvt8034: bool = ..., eamvt8035: _Optional[int] = ...) -> None: ...
