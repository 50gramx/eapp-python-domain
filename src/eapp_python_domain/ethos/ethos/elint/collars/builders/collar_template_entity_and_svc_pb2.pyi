from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DC49999XXXX(_message.Message):
    __slots__ = ("id", "name", "description", "collar_first_entity", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COLLAR_FIRST_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    collar_first_entity: CollarFirstEntity
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., collar_first_entity: _Optional[_Union[CollarFirstEntity, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CollarFirstEntity(_message.Message):
    __slots__ = ("id", "dummy", "yet_another_collar_entity")
    ID_FIELD_NUMBER: _ClassVar[int]
    DUMMY_FIELD_NUMBER: _ClassVar[int]
    YET_ANOTHER_COLLAR_ENTITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    dummy: str
    yet_another_collar_entity: _containers.RepeatedCompositeFieldContainer[YetAnotherCollarEntity]
    def __init__(self, id: _Optional[str] = ..., dummy: _Optional[str] = ..., yet_another_collar_entity: _Optional[_Iterable[_Union[YetAnotherCollarEntity, _Mapping]]] = ...) -> None: ...

class YetAnotherCollarEntity(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
