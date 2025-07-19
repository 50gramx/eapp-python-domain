from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DC499999998(_message.Message):
    __slots__ = ("id", "name", "description", "vm_instance", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VM_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    vm_instance: VMInstance
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., vm_instance: _Optional[_Union[VMInstance, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class VMInstance(_message.Message):
    __slots__ = ("id", "collar_id", "pod_id", "cpu_cores", "ram_gb", "storage_gb", "status", "created_at", "updated_at", "usage_metrics", "alerts")
    ID_FIELD_NUMBER: _ClassVar[int]
    COLLAR_ID_FIELD_NUMBER: _ClassVar[int]
    POD_ID_FIELD_NUMBER: _ClassVar[int]
    CPU_CORES_FIELD_NUMBER: _ClassVar[int]
    RAM_GB_FIELD_NUMBER: _ClassVar[int]
    STORAGE_GB_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USAGE_METRICS_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    collar_id: str
    pod_id: str
    cpu_cores: int
    ram_gb: float
    storage_gb: float
    status: str
    created_at: str
    updated_at: str
    usage_metrics: _containers.RepeatedCompositeFieldContainer[UsageMetric]
    alerts: _containers.RepeatedCompositeFieldContainer[Alert]
    def __init__(self, id: _Optional[str] = ..., collar_id: _Optional[str] = ..., pod_id: _Optional[str] = ..., cpu_cores: _Optional[int] = ..., ram_gb: _Optional[float] = ..., storage_gb: _Optional[float] = ..., status: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ..., usage_metrics: _Optional[_Iterable[_Union[UsageMetric, _Mapping]]] = ..., alerts: _Optional[_Iterable[_Union[Alert, _Mapping]]] = ...) -> None: ...

class UsageMetric(_message.Message):
    __slots__ = ("vm_instance_id", "cpu_usage", "memory_usage", "disk_io", "timestamp")
    VM_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    DISK_IO_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    vm_instance_id: str
    cpu_usage: float
    memory_usage: float
    disk_io: float
    timestamp: str
    def __init__(self, vm_instance_id: _Optional[str] = ..., cpu_usage: _Optional[float] = ..., memory_usage: _Optional[float] = ..., disk_io: _Optional[float] = ..., timestamp: _Optional[str] = ...) -> None: ...

class Alert(_message.Message):
    __slots__ = ("vm_instance_id", "alert_type", "alert_message", "created_at", "resolved_at")
    VM_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALERT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AT_FIELD_NUMBER: _ClassVar[int]
    vm_instance_id: str
    alert_type: str
    alert_message: str
    created_at: str
    resolved_at: str
    def __init__(self, vm_instance_id: _Optional[str] = ..., alert_type: _Optional[str] = ..., alert_message: _Optional[str] = ..., created_at: _Optional[str] = ..., resolved_at: _Optional[str] = ...) -> None: ...

class LaunchVMRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LaunchVMResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetVMInstanceRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetVMInstanceResponse(_message.Message):
    __slots__ = ("vm_instance",)
    VM_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    vm_instance: VMInstance
    def __init__(self, vm_instance: _Optional[_Union[VMInstance, _Mapping]] = ...) -> None: ...

class ListVMInstancesRequest(_message.Message):
    __slots__ = ("customer_id",)
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    def __init__(self, customer_id: _Optional[str] = ...) -> None: ...

class ListVMInstancesResponse(_message.Message):
    __slots__ = ("vm_instances",)
    VM_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    vm_instances: _containers.RepeatedCompositeFieldContainer[VMInstance]
    def __init__(self, vm_instances: _Optional[_Iterable[_Union[VMInstance, _Mapping]]] = ...) -> None: ...

class GetUsageMetricsRequest(_message.Message):
    __slots__ = ("vm_instance_id",)
    VM_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    vm_instance_id: str
    def __init__(self, vm_instance_id: _Optional[str] = ...) -> None: ...

class GetUsageMetricsResponse(_message.Message):
    __slots__ = ("usage_metrics",)
    USAGE_METRICS_FIELD_NUMBER: _ClassVar[int]
    usage_metrics: _containers.RepeatedCompositeFieldContainer[UsageMetric]
    def __init__(self, usage_metrics: _Optional[_Iterable[_Union[UsageMetric, _Mapping]]] = ...) -> None: ...

class GetAlertsRequest(_message.Message):
    __slots__ = ("vm_instance_id", "unresolved_only")
    VM_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    UNRESOLVED_ONLY_FIELD_NUMBER: _ClassVar[int]
    vm_instance_id: str
    unresolved_only: bool
    def __init__(self, vm_instance_id: _Optional[str] = ..., unresolved_only: bool = ...) -> None: ...

class GetAlertsResponse(_message.Message):
    __slots__ = ("alerts",)
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    alerts: _containers.RepeatedCompositeFieldContainer[Alert]
    def __init__(self, alerts: _Optional[_Iterable[_Union[Alert, _Mapping]]] = ...) -> None: ...
