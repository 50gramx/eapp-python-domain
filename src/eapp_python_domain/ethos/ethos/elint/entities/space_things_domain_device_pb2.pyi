from ethos.elint.entities import space_things_domain_pb2 as _space_things_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_TYPE_UNKNOWN: _ClassVar[DeviceType]
    SENSOR: _ClassVar[DeviceType]
    ACTUATOR: _ClassVar[DeviceType]
    CAMERA: _ClassVar[DeviceType]
    ROBOT: _ClassVar[DeviceType]
    COMPUTER: _ClassVar[DeviceType]

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFO: _ClassVar[LogLevel]
    WARNING: _ClassVar[LogLevel]
    ERROR: _ClassVar[LogLevel]
    CRITICAL: _ClassVar[LogLevel]

class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTART: _ClassVar[ActionType]
    SHUTDOWN: _ClassVar[ActionType]
    UPDATE_FIRMWARE: _ClassVar[ActionType]
DEVICE_TYPE_UNKNOWN: DeviceType
SENSOR: DeviceType
ACTUATOR: DeviceType
CAMERA: DeviceType
ROBOT: DeviceType
COMPUTER: DeviceType
INFO: LogLevel
WARNING: LogLevel
ERROR: LogLevel
CRITICAL: LogLevel
RESTART: ActionType
SHUTDOWN: ActionType
UPDATE_FIRMWARE: ActionType

class SpaceThingsDomainDevice(_message.Message):
    __slots__ = ("id", "name", "domain", "created_at", "last_updated_at", "last_accessed_at", "type", "specs", "status", "logs", "tags", "config", "metrics", "actions", "action_logs")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_AT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SPECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ACTION_LOGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    domain: _space_things_domain_pb2.SpaceThingsDomain
    created_at: _timestamp_pb2.Timestamp
    last_updated_at: _timestamp_pb2.Timestamp
    last_accessed_at: _timestamp_pb2.Timestamp
    type: DeviceType
    specs: DeviceSpecs
    status: DeviceStatus
    logs: _containers.RepeatedCompositeFieldContainer[DeviceLog]
    tags: _containers.RepeatedScalarFieldContainer[str]
    config: DeviceConfiguration
    metrics: _containers.RepeatedCompositeFieldContainer[DeviceMetric]
    actions: _containers.RepeatedCompositeFieldContainer[DeviceAction]
    action_logs: _containers.RepeatedCompositeFieldContainer[DeviceActionLog]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., domain: _Optional[_Union[_space_things_domain_pb2.SpaceThingsDomain, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_accessed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[_Union[DeviceType, str]] = ..., specs: _Optional[_Union[DeviceSpecs, _Mapping]] = ..., status: _Optional[_Union[DeviceStatus, _Mapping]] = ..., logs: _Optional[_Iterable[_Union[DeviceLog, _Mapping]]] = ..., tags: _Optional[_Iterable[str]] = ..., config: _Optional[_Union[DeviceConfiguration, _Mapping]] = ..., metrics: _Optional[_Iterable[_Union[DeviceMetric, _Mapping]]] = ..., actions: _Optional[_Iterable[_Union[DeviceAction, _Mapping]]] = ..., action_logs: _Optional[_Iterable[_Union[DeviceActionLog, _Mapping]]] = ...) -> None: ...

class DeviceSpecs(_message.Message):
    __slots__ = ("manufacturer", "model", "firmware_version", "memory_gb", "storage_gb", "cpu_ghz", "network_interfaces")
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    MEMORY_GB_FIELD_NUMBER: _ClassVar[int]
    STORAGE_GB_FIELD_NUMBER: _ClassVar[int]
    CPU_GHZ_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    manufacturer: str
    model: str
    firmware_version: str
    memory_gb: int
    storage_gb: int
    cpu_ghz: float
    network_interfaces: _containers.RepeatedCompositeFieldContainer[NetworkInterface]
    def __init__(self, manufacturer: _Optional[str] = ..., model: _Optional[str] = ..., firmware_version: _Optional[str] = ..., memory_gb: _Optional[int] = ..., storage_gb: _Optional[int] = ..., cpu_ghz: _Optional[float] = ..., network_interfaces: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]] = ...) -> None: ...

class NetworkInterface(_message.Message):
    __slots__ = ("mac_address", "ip_address", "interface_type")
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    mac_address: str
    ip_address: str
    interface_type: str
    def __init__(self, mac_address: _Optional[str] = ..., ip_address: _Optional[str] = ..., interface_type: _Optional[str] = ...) -> None: ...

class DeviceStatus(_message.Message):
    __slots__ = ("is_online", "last_checked", "alerts")
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECKED_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    is_online: bool
    last_checked: str
    alerts: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, is_online: bool = ..., last_checked: _Optional[str] = ..., alerts: _Optional[_Iterable[str]] = ...) -> None: ...

class DeviceLog(_message.Message):
    __slots__ = ("timestamp", "message", "level")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    timestamp: str
    message: str
    level: LogLevel
    def __init__(self, timestamp: _Optional[str] = ..., message: _Optional[str] = ..., level: _Optional[_Union[LogLevel, str]] = ...) -> None: ...

class DeviceConfiguration(_message.Message):
    __slots__ = ("config_name", "config_value")
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VALUE_FIELD_NUMBER: _ClassVar[int]
    config_name: str
    config_value: str
    def __init__(self, config_name: _Optional[str] = ..., config_value: _Optional[str] = ...) -> None: ...

class DeviceMetric(_message.Message):
    __slots__ = ("metric_name", "value", "timestamp")
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    metric_name: str
    value: float
    timestamp: str
    def __init__(self, metric_name: _Optional[str] = ..., value: _Optional[float] = ..., timestamp: _Optional[str] = ...) -> None: ...

class DeviceAction(_message.Message):
    __slots__ = ("action_id", "action_name", "action_type", "parameters")
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    action_name: str
    action_type: ActionType
    parameters: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, action_id: _Optional[str] = ..., action_name: _Optional[str] = ..., action_type: _Optional[_Union[ActionType, str]] = ..., parameters: _Optional[_Iterable[str]] = ...) -> None: ...

class DeviceActionLog(_message.Message):
    __slots__ = ("action_id", "timestamp", "result")
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    timestamp: str
    result: str
    def __init__(self, action_id: _Optional[str] = ..., timestamp: _Optional[str] = ..., result: _Optional[str] = ...) -> None: ...
