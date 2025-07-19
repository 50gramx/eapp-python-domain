from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_service_pb2 as _space_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DC499999999(_message.Message):
    __slots__ = ("id", "name", "description", "deployment", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    deployment: Deployment
    created_at: _timestamp_pb2_1.Timestamp
    updated_at: _timestamp_pb2_1.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., deployment: _Optional[_Union[Deployment, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class Deployment(_message.Message):
    __slots__ = ("id", "metadata", "replica_config", "rollout_settings", "networking_config", "selector", "pod_template", "affinity_rules", "node_selector", "tolerations", "lifecycle_hooks", "priority_class", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REPLICA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NETWORKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    POD_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    AFFINITY_RULES_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    TOLERATIONS_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_HOOKS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_CLASS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    metadata: DeploymentMetadata
    replica_config: ReplicaConfig
    rollout_settings: RolloutSettings
    networking_config: NetworkingConfig
    selector: LabelSelector
    pod_template: PodTemplate
    affinity_rules: _containers.RepeatedCompositeFieldContainer[AffinityRule]
    node_selector: NodeSelector
    tolerations: _containers.RepeatedCompositeFieldContainer[Toleration]
    lifecycle_hooks: LifecycleHook
    priority_class: PriorityClass
    status: DeploymentStatus
    def __init__(self, id: _Optional[str] = ..., metadata: _Optional[_Union[DeploymentMetadata, _Mapping]] = ..., replica_config: _Optional[_Union[ReplicaConfig, _Mapping]] = ..., rollout_settings: _Optional[_Union[RolloutSettings, _Mapping]] = ..., networking_config: _Optional[_Union[NetworkingConfig, _Mapping]] = ..., selector: _Optional[_Union[LabelSelector, _Mapping]] = ..., pod_template: _Optional[_Union[PodTemplate, _Mapping]] = ..., affinity_rules: _Optional[_Iterable[_Union[AffinityRule, _Mapping]]] = ..., node_selector: _Optional[_Union[NodeSelector, _Mapping]] = ..., tolerations: _Optional[_Iterable[_Union[Toleration, _Mapping]]] = ..., lifecycle_hooks: _Optional[_Union[LifecycleHook, _Mapping]] = ..., priority_class: _Optional[_Union[PriorityClass, _Mapping]] = ..., status: _Optional[_Union[DeploymentStatus, _Mapping]] = ...) -> None: ...

class DeploymentMetadata(_message.Message):
    __slots__ = ("id", "deployment_id", "name", "namespace", "labels", "annotations")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    deployment_id: str
    name: str
    namespace: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ReplicaConfig(_message.Message):
    __slots__ = ("id", "deployment_id", "replicas", "strategy", "min_ready_seconds")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    MIN_READY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    deployment_id: str
    replicas: int
    strategy: str
    min_ready_seconds: int
    def __init__(self, id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., replicas: _Optional[int] = ..., strategy: _Optional[str] = ..., min_ready_seconds: _Optional[int] = ...) -> None: ...

class NetworkingConfig(_message.Message):
    __slots__ = ("id", "deployment_id", "host_network", "dns_policy", "service_account_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_NETWORK_FIELD_NUMBER: _ClassVar[int]
    DNS_POLICY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    deployment_id: str
    host_network: bool
    dns_policy: str
    service_account_name: str
    def __init__(self, id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., host_network: bool = ..., dns_policy: _Optional[str] = ..., service_account_name: _Optional[str] = ...) -> None: ...

class LabelSelector(_message.Message):
    __slots__ = ("id", "deployment_id", "match_labels", "match_expressions")
    class MatchLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_LABELS_FIELD_NUMBER: _ClassVar[int]
    MATCH_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    deployment_id: str
    match_labels: _containers.ScalarMap[str, str]
    match_expressions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., match_labels: _Optional[_Mapping[str, str]] = ..., match_expressions: _Optional[_Iterable[str]] = ...) -> None: ...

class PodTemplate(_message.Message):
    __slots__ = ("id", "deployment_id", "labels", "annotations", "containers", "volumes")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    id: str
    deployment_id: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    containers: _containers.RepeatedCompositeFieldContainer[Container]
    volumes: _containers.RepeatedCompositeFieldContainer[Volume]
    def __init__(self, id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., containers: _Optional[_Iterable[_Union[Container, _Mapping]]] = ..., volumes: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ...) -> None: ...

class Container(_message.Message):
    __slots__ = ("id", "pod_template_id", "name", "image", "command", "args", "ports", "env_vars", "resource_requests", "resource_limits", "volume_mounts", "working_directory", "liveness_probe", "readiness_probe", "startup_probe", "security_context")
    ID_FIELD_NUMBER: _ClassVar[int]
    POD_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    ENV_VARS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNTS_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_PROBE_FIELD_NUMBER: _ClassVar[int]
    READINESS_PROBE_FIELD_NUMBER: _ClassVar[int]
    STARTUP_PROBE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    pod_template_id: str
    name: str
    image: str
    command: _containers.RepeatedScalarFieldContainer[str]
    args: _containers.RepeatedScalarFieldContainer[str]
    ports: _containers.RepeatedCompositeFieldContainer[ContainerPort]
    env_vars: _containers.RepeatedCompositeFieldContainer[EnvVar]
    resource_requests: ResourceRequests
    resource_limits: ResourceLimits
    volume_mounts: _containers.RepeatedCompositeFieldContainer[VolumeMount]
    working_directory: str
    liveness_probe: Probe
    readiness_probe: Probe
    startup_probe: Probe
    security_context: SecurityContext
    def __init__(self, id: _Optional[str] = ..., pod_template_id: _Optional[str] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., args: _Optional[_Iterable[str]] = ..., ports: _Optional[_Iterable[_Union[ContainerPort, _Mapping]]] = ..., env_vars: _Optional[_Iterable[_Union[EnvVar, _Mapping]]] = ..., resource_requests: _Optional[_Union[ResourceRequests, _Mapping]] = ..., resource_limits: _Optional[_Union[ResourceLimits, _Mapping]] = ..., volume_mounts: _Optional[_Iterable[_Union[VolumeMount, _Mapping]]] = ..., working_directory: _Optional[str] = ..., liveness_probe: _Optional[_Union[Probe, _Mapping]] = ..., readiness_probe: _Optional[_Union[Probe, _Mapping]] = ..., startup_probe: _Optional[_Union[Probe, _Mapping]] = ..., security_context: _Optional[_Union[SecurityContext, _Mapping]] = ...) -> None: ...

class Volume(_message.Message):
    __slots__ = ("id", "pod_template_id", "name", "type", "source")
    ID_FIELD_NUMBER: _ClassVar[int]
    POD_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    pod_template_id: str
    name: str
    type: str
    source: str
    def __init__(self, id: _Optional[str] = ..., pod_template_id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class ContainerPort(_message.Message):
    __slots__ = ("id", "container_id", "name", "container_port", "protocol", "node_port")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_PORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    NODE_PORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    container_id: str
    name: str
    container_port: int
    protocol: str
    node_port: int
    def __init__(self, id: _Optional[str] = ..., container_id: _Optional[str] = ..., name: _Optional[str] = ..., container_port: _Optional[int] = ..., protocol: _Optional[str] = ..., node_port: _Optional[int] = ...) -> None: ...

class EnvVar(_message.Message):
    __slots__ = ("id", "container_id", "name", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    container_id: str
    name: str
    value: str
    def __init__(self, id: _Optional[str] = ..., container_id: _Optional[str] = ..., name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ResourceRequests(_message.Message):
    __slots__ = ("id", "container_id", "cpu", "memory")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    container_id: str
    cpu: str
    memory: str
    def __init__(self, id: _Optional[str] = ..., container_id: _Optional[str] = ..., cpu: _Optional[str] = ..., memory: _Optional[str] = ...) -> None: ...

class ResourceLimits(_message.Message):
    __slots__ = ("id", "container_id", "cpu", "memory")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    container_id: str
    cpu: str
    memory: str
    def __init__(self, id: _Optional[str] = ..., container_id: _Optional[str] = ..., cpu: _Optional[str] = ..., memory: _Optional[str] = ...) -> None: ...

class VolumeMount(_message.Message):
    __slots__ = ("name", "mount_path", "read_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    mount_path: str
    read_only: bool
    def __init__(self, name: _Optional[str] = ..., mount_path: _Optional[str] = ..., read_only: bool = ...) -> None: ...

class Probe(_message.Message):
    __slots__ = ("type", "exec_command", "http_path", "initial_delay_seconds", "period_seconds", "timeout_seconds", "success_threshold", "failure_threshold")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXEC_COMMAND_FIELD_NUMBER: _ClassVar[int]
    HTTP_PATH_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    type: str
    exec_command: str
    http_path: str
    initial_delay_seconds: int
    period_seconds: int
    timeout_seconds: int
    success_threshold: int
    failure_threshold: int
    def __init__(self, type: _Optional[str] = ..., exec_command: _Optional[str] = ..., http_path: _Optional[str] = ..., initial_delay_seconds: _Optional[int] = ..., period_seconds: _Optional[int] = ..., timeout_seconds: _Optional[int] = ..., success_threshold: _Optional[int] = ..., failure_threshold: _Optional[int] = ...) -> None: ...

class SecurityContext(_message.Message):
    __slots__ = ("run_as_user", "run_as_group", "read_only_root_filesystem", "privileged")
    RUN_AS_USER_FIELD_NUMBER: _ClassVar[int]
    RUN_AS_GROUP_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_ROOT_FILESYSTEM_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
    run_as_user: int
    run_as_group: int
    read_only_root_filesystem: bool
    privileged: bool
    def __init__(self, run_as_user: _Optional[int] = ..., run_as_group: _Optional[int] = ..., read_only_root_filesystem: bool = ..., privileged: bool = ...) -> None: ...

class AffinityRule(_message.Message):
    __slots__ = ("type", "expressions")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    type: str
    expressions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[str] = ..., expressions: _Optional[_Iterable[str]] = ...) -> None: ...

class NodeSelector(_message.Message):
    __slots__ = ("match_labels",)
    class MatchLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MATCH_LABELS_FIELD_NUMBER: _ClassVar[int]
    match_labels: _containers.ScalarMap[str, str]
    def __init__(self, match_labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Toleration(_message.Message):
    __slots__ = ("key", "operator", "value", "effect")
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    key: str
    operator: str
    value: str
    effect: int
    def __init__(self, key: _Optional[str] = ..., operator: _Optional[str] = ..., value: _Optional[str] = ..., effect: _Optional[int] = ...) -> None: ...

class RolloutSettings(_message.Message):
    __slots__ = ("max_surge", "max_unavailable")
    MAX_SURGE_FIELD_NUMBER: _ClassVar[int]
    MAX_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    max_surge: str
    max_unavailable: str
    def __init__(self, max_surge: _Optional[str] = ..., max_unavailable: _Optional[str] = ...) -> None: ...

class LifecycleHook(_message.Message):
    __slots__ = ("pre_stop_command", "post_start_command")
    PRE_STOP_COMMAND_FIELD_NUMBER: _ClassVar[int]
    POST_START_COMMAND_FIELD_NUMBER: _ClassVar[int]
    pre_stop_command: str
    post_start_command: str
    def __init__(self, pre_stop_command: _Optional[str] = ..., post_start_command: _Optional[str] = ...) -> None: ...

class PriorityClass(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeploymentStatus(_message.Message):
    __slots__ = ("id", "deployment_id", "replicas", "updated_replicas", "available_replicas", "unavailable_replicas", "conditions")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    deployment_id: str
    replicas: int
    updated_replicas: int
    available_replicas: int
    unavailable_replicas: int
    conditions: _containers.RepeatedCompositeFieldContainer[Condition]
    def __init__(self, id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., replicas: _Optional[int] = ..., updated_replicas: _Optional[int] = ..., available_replicas: _Optional[int] = ..., unavailable_replicas: _Optional[int] = ..., conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ...) -> None: ...

class Condition(_message.Message):
    __slots__ = ("type", "status", "reason", "message", "last_update_time", "last_transition_time")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_TRANSITION_TIME_FIELD_NUMBER: _ClassVar[int]
    type: str
    status: str
    reason: str
    message: str
    last_update_time: _timestamp_pb2_1.Timestamp
    last_transition_time: _timestamp_pb2_1.Timestamp
    def __init__(self, type: _Optional[str] = ..., status: _Optional[str] = ..., reason: _Optional[str] = ..., message: _Optional[str] = ..., last_update_time: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., last_transition_time: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...
