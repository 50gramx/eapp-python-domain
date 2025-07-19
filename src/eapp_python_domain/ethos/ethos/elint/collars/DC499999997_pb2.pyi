from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class DC499999997(_message.Message):
    __slots__ = ("node_id", "name", "machine_class", "storage_class", "bandwidth_class", "operator_class", "hashing_class", "base_os", "orchestrator_os", "node_liability", "created_at")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MACHINE_CLASS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_CLASS_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_CLASS_FIELD_NUMBER: _ClassVar[int]
    HASHING_CLASS_FIELD_NUMBER: _ClassVar[int]
    BASE_OS_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_OS_FIELD_NUMBER: _ClassVar[int]
    NODE_LIABILITY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    name: str
    machine_class: MachineClass
    storage_class: StorageClass
    bandwidth_class: BandwidthClass
    operator_class: OperatorClass
    hashing_class: HashingClass
    base_os: BaseOS
    orchestrator_os: OrchestratorOS
    node_liability: NodeLiability
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, node_id: _Optional[str] = ..., name: _Optional[str] = ..., machine_class: _Optional[_Union[MachineClass, _Mapping]] = ..., storage_class: _Optional[_Union[StorageClass, _Mapping]] = ..., bandwidth_class: _Optional[_Union[BandwidthClass, _Mapping]] = ..., operator_class: _Optional[_Union[OperatorClass, _Mapping]] = ..., hashing_class: _Optional[_Union[HashingClass, _Mapping]] = ..., base_os: _Optional[_Union[BaseOS, _Mapping]] = ..., orchestrator_os: _Optional[_Union[OrchestratorOS, _Mapping]] = ..., node_liability: _Optional[_Union[NodeLiability, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MachineClass(_message.Message):
    __slots__ = ("id", "main_class", "sub_classes", "vcpu", "ram_gib", "machine_type", "machine_category")
    ID_FIELD_NUMBER: _ClassVar[int]
    MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
    SUB_CLASSES_FIELD_NUMBER: _ClassVar[int]
    VCPU_FIELD_NUMBER: _ClassVar[int]
    RAM_GIB_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    main_class: str
    sub_classes: str
    vcpu: int
    ram_gib: float
    machine_type: str
    machine_category: str
    def __init__(self, id: _Optional[str] = ..., main_class: _Optional[str] = ..., sub_classes: _Optional[str] = ..., vcpu: _Optional[int] = ..., ram_gib: _Optional[float] = ..., machine_type: _Optional[str] = ..., machine_category: _Optional[str] = ...) -> None: ...

class StorageClass(_message.Message):
    __slots__ = ("id", "main_class", "sub_classes", "fast_storage", "standard_storage", "slow_storage")
    ID_FIELD_NUMBER: _ClassVar[int]
    MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
    SUB_CLASSES_FIELD_NUMBER: _ClassVar[int]
    FAST_STORAGE_FIELD_NUMBER: _ClassVar[int]
    STANDARD_STORAGE_FIELD_NUMBER: _ClassVar[int]
    SLOW_STORAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    main_class: str
    sub_classes: str
    fast_storage: float
    standard_storage: float
    slow_storage: float
    def __init__(self, id: _Optional[str] = ..., main_class: _Optional[str] = ..., sub_classes: _Optional[str] = ..., fast_storage: _Optional[float] = ..., standard_storage: _Optional[float] = ..., slow_storage: _Optional[float] = ...) -> None: ...

class BandwidthClass(_message.Message):
    __slots__ = ("id", "main_class", "sub_classes", "locale_network_bandwidth_class", "main_network_bandwidth_class", "main_network_bandwidth_static_address")
    ID_FIELD_NUMBER: _ClassVar[int]
    MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
    SUB_CLASSES_FIELD_NUMBER: _ClassVar[int]
    LOCALE_NETWORK_BANDWIDTH_CLASS_FIELD_NUMBER: _ClassVar[int]
    MAIN_NETWORK_BANDWIDTH_CLASS_FIELD_NUMBER: _ClassVar[int]
    MAIN_NETWORK_BANDWIDTH_STATIC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: str
    main_class: str
    sub_classes: str
    locale_network_bandwidth_class: float
    main_network_bandwidth_class: float
    main_network_bandwidth_static_address: bool
    def __init__(self, id: _Optional[str] = ..., main_class: _Optional[str] = ..., sub_classes: _Optional[str] = ..., locale_network_bandwidth_class: _Optional[float] = ..., main_network_bandwidth_class: _Optional[float] = ..., main_network_bandwidth_static_address: bool = ...) -> None: ...

class OperatorClass(_message.Message):
    __slots__ = ("id", "main_class", "sub_classes", "human_operator_class", "collaborator_operator_class", "certified_operator_class")
    ID_FIELD_NUMBER: _ClassVar[int]
    MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
    SUB_CLASSES_FIELD_NUMBER: _ClassVar[int]
    HUMAN_OPERATOR_CLASS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_OPERATOR_CLASS_FIELD_NUMBER: _ClassVar[int]
    CERTIFIED_OPERATOR_CLASS_FIELD_NUMBER: _ClassVar[int]
    id: str
    main_class: str
    sub_classes: str
    human_operator_class: bool
    collaborator_operator_class: bool
    certified_operator_class: bool
    def __init__(self, id: _Optional[str] = ..., main_class: _Optional[str] = ..., sub_classes: _Optional[str] = ..., human_operator_class: bool = ..., collaborator_operator_class: bool = ..., certified_operator_class: bool = ...) -> None: ...

class HashingClass(_message.Message):
    __slots__ = ("id", "main_class", "sub_classes", "chain_hash_generation_class")
    ID_FIELD_NUMBER: _ClassVar[int]
    MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
    SUB_CLASSES_FIELD_NUMBER: _ClassVar[int]
    CHAIN_HASH_GENERATION_CLASS_FIELD_NUMBER: _ClassVar[int]
    id: str
    main_class: str
    sub_classes: str
    chain_hash_generation_class: bool
    def __init__(self, id: _Optional[str] = ..., main_class: _Optional[str] = ..., sub_classes: _Optional[str] = ..., chain_hash_generation_class: bool = ...) -> None: ...

class BaseOS(_message.Message):
    __slots__ = ("id", "name", "arch")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARCH_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    arch: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., arch: _Optional[str] = ...) -> None: ...

class OrchestratorOS(_message.Message):
    __slots__ = ("id", "name", "version")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    version: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class NodeLiability(_message.Message):
    __slots__ = ("id", "liability", "license_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    LIABILITY_FIELD_NUMBER: _ClassVar[int]
    LICENSE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    liability: str
    license_id: str
    def __init__(self, id: _Optional[str] = ..., liability: _Optional[str] = ..., license_id: _Optional[str] = ...) -> None: ...

class OVPNConfig(_message.Message):
    __slots__ = ("config_id", "server_address", "port", "protocol", "ca_cert", "cert", "key", "dh_param", "tls_auth_key", "allowed_ips", "created_at", "updated_at", "description")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    CA_CERT_FIELD_NUMBER: _ClassVar[int]
    CERT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    DH_PARAM_FIELD_NUMBER: _ClassVar[int]
    TLS_AUTH_KEY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_IPS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    config_id: str
    server_address: str
    port: str
    protocol: str
    ca_cert: str
    cert: str
    key: str
    dh_param: str
    tls_auth_key: str
    allowed_ips: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    description: str
    def __init__(self, config_id: _Optional[str] = ..., server_address: _Optional[str] = ..., port: _Optional[str] = ..., protocol: _Optional[str] = ..., ca_cert: _Optional[str] = ..., cert: _Optional[str] = ..., key: _Optional[str] = ..., dh_param: _Optional[str] = ..., tls_auth_key: _Optional[str] = ..., allowed_ips: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...
