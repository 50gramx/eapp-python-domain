from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MachineClassEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENERAL: _ClassVar[MachineClassEnum]
    ACCELERATED: _ClassVar[MachineClassEnum]

class MachineNameEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    X2: _ClassVar[MachineNameEnum]
    M2N: _ClassVar[MachineNameEnum]
    M2: _ClassVar[MachineNameEnum]

class MachineTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NANO: _ClassVar[MachineTypeEnum]
    MICRO: _ClassVar[MachineTypeEnum]
    SMALL: _ClassVar[MachineTypeEnum]
    MEDIUM: _ClassVar[MachineTypeEnum]
    LARGE: _ClassVar[MachineTypeEnum]
    XLARGE: _ClassVar[MachineTypeEnum]
    XXLARGE: _ClassVar[MachineTypeEnum]
GENERAL: MachineClassEnum
ACCELERATED: MachineClassEnum
X2: MachineNameEnum
M2N: MachineNameEnum
M2: MachineNameEnum
NANO: MachineTypeEnum
MICRO: MachineTypeEnum
SMALL: MachineTypeEnum
MEDIUM: MachineTypeEnum
LARGE: MachineTypeEnum
XLARGE: MachineTypeEnum
XXLARGE: MachineTypeEnum

class Machine(_message.Message):
    __slots__ = ("machine_id", "machine_class_enum", "machine_name_enum", "machine_type_enum", "can_be_shared", "hourly_rate", "baseline_performance_factor", "baseline_memory_factor", "baseline_network_factor", "machine_description")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_CLASS_ENUM_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_ENUM_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_ENUM_FIELD_NUMBER: _ClassVar[int]
    CAN_BE_SHARED_FIELD_NUMBER: _ClassVar[int]
    HOURLY_RATE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_PERFORMANCE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    BASELINE_MEMORY_FACTOR_FIELD_NUMBER: _ClassVar[int]
    BASELINE_NETWORK_FACTOR_FIELD_NUMBER: _ClassVar[int]
    MACHINE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    machine_class_enum: MachineClassEnum
    machine_name_enum: MachineNameEnum
    machine_type_enum: MachineTypeEnum
    can_be_shared: bool
    hourly_rate: float
    baseline_performance_factor: int
    baseline_memory_factor: int
    baseline_network_factor: int
    machine_description: str
    def __init__(self, machine_id: _Optional[str] = ..., machine_class_enum: _Optional[_Union[MachineClassEnum, str]] = ..., machine_name_enum: _Optional[_Union[MachineNameEnum, str]] = ..., machine_type_enum: _Optional[_Union[MachineTypeEnum, str]] = ..., can_be_shared: bool = ..., hourly_rate: _Optional[float] = ..., baseline_performance_factor: _Optional[int] = ..., baseline_memory_factor: _Optional[int] = ..., baseline_network_factor: _Optional[int] = ..., machine_description: _Optional[str] = ...) -> None: ...
