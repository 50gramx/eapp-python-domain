# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethos/elint/collars/DC499999999.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ethos.elint.entities import space_service_pb2 as ethos_dot_elint_dot_entities_dot_space__service__pb2
try:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_space__service__pb2.google_dot_protobuf_dot_timestamp__pb2
except AttributeError:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_space__service__pb2.google.protobuf.timestamp_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%ethos/elint/collars/DC499999999.proto\x12\relint.collars\x1a\x1fgoogle/protobuf/timestamp.proto\x1a(ethos/elint/entities/space_service.proto\"\xcc\x01\n\x0b\x44\x43\x34\x39\x39\x39\x39\x39\x39\x39\x39\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\ndeployment\x18\x88\' \x01(\x0b\x32\x19.elint.collars.Deployment\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x9e\x05\n\nDeployment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x34\n\x08metadata\x18\x90\' \x01(\x0b\x32!.elint.collars.DeploymentMetadata\x12\x35\n\x0ereplica_config\x18\x91\' \x01(\x0b\x32\x1c.elint.collars.ReplicaConfig\x12\x39\n\x10rollout_settings\x18\x92\' \x01(\x0b\x32\x1e.elint.collars.RolloutSettings\x12;\n\x11networking_config\x18\x93\' \x01(\x0b\x32\x1f.elint.collars.NetworkingConfig\x12/\n\x08selector\x18\x89\' \x01(\x0b\x32\x1c.elint.collars.LabelSelector\x12\x31\n\x0cpod_template\x18\x8a\' \x01(\x0b\x32\x1a.elint.collars.PodTemplate\x12\x34\n\x0e\x61\x66\x66inity_rules\x18\x8b\' \x03(\x0b\x32\x1b.elint.collars.AffinityRule\x12\x33\n\rnode_selector\x18\x8c\' \x01(\x0b\x32\x1b.elint.collars.NodeSelector\x12/\n\x0btolerations\x18\x8d\' \x03(\x0b\x32\x19.elint.collars.Toleration\x12\x36\n\x0flifecycle_hooks\x18\x8e\' \x01(\x0b\x32\x1c.elint.collars.LifecycleHook\x12\x35\n\x0epriority_class\x18\x8f\' \x01(\x0b\x32\x1c.elint.collars.PriorityClass\x12\x30\n\x06status\x18\xa3\' \x01(\x0b\x32\x1f.elint.collars.DeploymentStatus\"\xc5\x02\n\x12\x44\x65ploymentMetadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rdeployment_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tnamespace\x18\x04 \x01(\t\x12>\n\x06labels\x18\x94\' \x03(\x0b\x32-.elint.collars.DeploymentMetadata.LabelsEntry\x12H\n\x0b\x61nnotations\x18\x95\' \x03(\x0b\x32\x32.elint.collars.DeploymentMetadata.AnnotationsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"q\n\rReplicaConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rdeployment_id\x18\x02 \x01(\t\x12\x10\n\x08replicas\x18\x03 \x01(\x05\x12\x10\n\x08strategy\x18\x04 \x01(\t\x12\x19\n\x11min_ready_seconds\x18\x05 \x01(\x05\"}\n\x10NetworkingConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rdeployment_id\x18\x02 \x01(\t\x12\x14\n\x0chost_network\x18\x03 \x01(\x08\x12\x12\n\ndns_policy\x18\x04 \x01(\t\x12\x1c\n\x14service_account_name\x18\x05 \x01(\t\"\xc8\x01\n\rLabelSelector\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rdeployment_id\x18\x02 \x01(\t\x12\x44\n\x0cmatch_labels\x18\x96\' \x03(\x0b\x32-.elint.collars.LabelSelector.MatchLabelsEntry\x12\x1a\n\x11match_expressions\x18\x97\' \x03(\t\x1a\x32\n\x10MatchLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe7\x02\n\x0bPodTemplate\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rdeployment_id\x18\x02 \x01(\t\x12\x37\n\x06labels\x18\x98\' \x03(\x0b\x32&.elint.collars.PodTemplate.LabelsEntry\x12\x41\n\x0b\x61nnotations\x18\x99\' \x03(\x0b\x32+.elint.collars.PodTemplate.AnnotationsEntry\x12-\n\ncontainers\x18\x9a\' \x03(\x0b\x32\x18.elint.collars.Container\x12\'\n\x07volumes\x18\x9b\' \x03(\x0b\x32\x15.elint.collars.Volume\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcf\x04\n\tContainer\x12\n\n\x02id\x18\x0f \x01(\t\x12\x17\n\x0fpod_template_id\x18\x10 \x01(\t\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12\x10\n\x07\x63ommand\x18\x9c\' \x03(\t\x12\r\n\x04\x61rgs\x18\x9d\' \x03(\t\x12,\n\x05ports\x18\x9e\' \x03(\x0b\x32\x1c.elint.collars.ContainerPort\x12(\n\x08\x65nv_vars\x18\x9f\' \x03(\x0b\x32\x15.elint.collars.EnvVar\x12;\n\x11resource_requests\x18\xa0\' \x01(\x0b\x32\x1f.elint.collars.ResourceRequests\x12\x37\n\x0fresource_limits\x18\xa1\' \x01(\x0b\x32\x1d.elint.collars.ResourceLimits\x12\x32\n\rvolume_mounts\x18\xa2\' \x03(\x0b\x32\x1a.elint.collars.VolumeMount\x12\x19\n\x11working_directory\x18\n \x01(\t\x12,\n\x0eliveness_probe\x18\x0b \x01(\x0b\x32\x14.elint.collars.Probe\x12-\n\x0freadiness_probe\x18\x0c \x01(\x0b\x32\x14.elint.collars.Probe\x12+\n\rstartup_probe\x18\r \x01(\x0b\x32\x14.elint.collars.Probe\x12\x38\n\x10security_context\x18\x0e \x01(\x0b\x32\x1e.elint.collars.SecurityContext\"Y\n\x06Volume\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0fpod_template_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0e\n\x06source\x18\x05 \x01(\t\"|\n\rContainerPort\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontainer_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x16\n\x0e\x63ontainer_port\x18\x04 \x01(\x05\x12\x10\n\x08protocol\x18\x05 \x01(\t\x12\x11\n\tnode_port\x18\x06 \x01(\x05\"G\n\x06\x45nvVar\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontainer_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\t\"Q\n\x10ResourceRequests\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontainer_id\x18\x02 \x01(\t\x12\x0b\n\x03\x63pu\x18\x04 \x01(\t\x12\x0e\n\x06memory\x18\x05 \x01(\t\"O\n\x0eResourceLimits\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontainer_id\x18\x02 \x01(\t\x12\x0b\n\x03\x63pu\x18\x04 \x01(\t\x12\x0e\n\x06memory\x18\x05 \x01(\t\"B\n\x0bVolumeMount\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nmount_path\x18\x02 \x01(\t\x12\x11\n\tread_only\x18\x03 \x01(\x08\"\xc4\x01\n\x05Probe\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x0c\x65xec_command\x18\x02 \x01(\t\x12\x11\n\thttp_path\x18\x03 \x01(\t\x12\x1d\n\x15initial_delay_seconds\x18\x04 \x01(\x05\x12\x16\n\x0eperiod_seconds\x18\x05 \x01(\x05\x12\x17\n\x0ftimeout_seconds\x18\x06 \x01(\x05\x12\x19\n\x11success_threshold\x18\x07 \x01(\x05\x12\x19\n\x11\x66\x61ilure_threshold\x18\x08 \x01(\x05\"s\n\x0fSecurityContext\x12\x13\n\x0brun_as_user\x18\x01 \x01(\x03\x12\x14\n\x0crun_as_group\x18\x02 \x01(\x03\x12!\n\x19read_only_root_filesystem\x18\x03 \x01(\x08\x12\x12\n\nprivileged\x18\x04 \x01(\x08\"1\n\x0c\x41\x66\x66inityRule\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x13\n\x0b\x65xpressions\x18\x02 \x03(\t\"\x86\x01\n\x0cNodeSelector\x12\x42\n\x0cmatch_labels\x18\x01 \x03(\x0b\x32,.elint.collars.NodeSelector.MatchLabelsEntry\x1a\x32\n\x10MatchLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"J\n\nToleration\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0e\n\x06\x65\x66\x66\x65\x63t\x18\x04 \x01(\x03\"=\n\x0fRolloutSettings\x12\x11\n\tmax_surge\x18\x01 \x01(\t\x12\x17\n\x0fmax_unavailable\x18\x02 \x01(\t\"E\n\rLifecycleHook\x12\x18\n\x10pre_stop_command\x18\x01 \x01(\t\x12\x1a\n\x12post_start_command\x18\x02 \x01(\t\"\x1d\n\rPriorityClass\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xc9\x01\n\x10\x44\x65ploymentStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rdeployment_id\x18\x02 \x01(\t\x12\x10\n\x08replicas\x18\x03 \x01(\x05\x12\x18\n\x10updated_replicas\x18\x04 \x01(\x05\x12\x1a\n\x12\x61vailable_replicas\x18\x05 \x01(\x05\x12\x1c\n\x14unavailable_replicas\x18\x06 \x01(\x05\x12,\n\nconditions\x18\x07 \x03(\x0b\x32\x18.elint.collars.Condition\"\xba\x01\n\tCondition\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x34\n\x10last_update_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14last_transition_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestampb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethos.elint.collars.DC499999999_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DEPLOYMENTMETADATA_LABELSENTRY']._options = None
  _globals['_DEPLOYMENTMETADATA_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_DEPLOYMENTMETADATA_ANNOTATIONSENTRY']._options = None
  _globals['_DEPLOYMENTMETADATA_ANNOTATIONSENTRY']._serialized_options = b'8\001'
  _globals['_LABELSELECTOR_MATCHLABELSENTRY']._options = None
  _globals['_LABELSELECTOR_MATCHLABELSENTRY']._serialized_options = b'8\001'
  _globals['_PODTEMPLATE_LABELSENTRY']._options = None
  _globals['_PODTEMPLATE_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_PODTEMPLATE_ANNOTATIONSENTRY']._options = None
  _globals['_PODTEMPLATE_ANNOTATIONSENTRY']._serialized_options = b'8\001'
  _globals['_NODESELECTOR_MATCHLABELSENTRY']._options = None
  _globals['_NODESELECTOR_MATCHLABELSENTRY']._serialized_options = b'8\001'
  _globals['_DC499999999']._serialized_start=132
  _globals['_DC499999999']._serialized_end=336
  _globals['_DEPLOYMENT']._serialized_start=339
  _globals['_DEPLOYMENT']._serialized_end=1009
  _globals['_DEPLOYMENTMETADATA']._serialized_start=1012
  _globals['_DEPLOYMENTMETADATA']._serialized_end=1337
  _globals['_DEPLOYMENTMETADATA_LABELSENTRY']._serialized_start=1240
  _globals['_DEPLOYMENTMETADATA_LABELSENTRY']._serialized_end=1285
  _globals['_DEPLOYMENTMETADATA_ANNOTATIONSENTRY']._serialized_start=1287
  _globals['_DEPLOYMENTMETADATA_ANNOTATIONSENTRY']._serialized_end=1337
  _globals['_REPLICACONFIG']._serialized_start=1339
  _globals['_REPLICACONFIG']._serialized_end=1452
  _globals['_NETWORKINGCONFIG']._serialized_start=1454
  _globals['_NETWORKINGCONFIG']._serialized_end=1579
  _globals['_LABELSELECTOR']._serialized_start=1582
  _globals['_LABELSELECTOR']._serialized_end=1782
  _globals['_LABELSELECTOR_MATCHLABELSENTRY']._serialized_start=1732
  _globals['_LABELSELECTOR_MATCHLABELSENTRY']._serialized_end=1782
  _globals['_PODTEMPLATE']._serialized_start=1785
  _globals['_PODTEMPLATE']._serialized_end=2144
  _globals['_PODTEMPLATE_LABELSENTRY']._serialized_start=1240
  _globals['_PODTEMPLATE_LABELSENTRY']._serialized_end=1285
  _globals['_PODTEMPLATE_ANNOTATIONSENTRY']._serialized_start=1287
  _globals['_PODTEMPLATE_ANNOTATIONSENTRY']._serialized_end=1337
  _globals['_CONTAINER']._serialized_start=2147
  _globals['_CONTAINER']._serialized_end=2738
  _globals['_VOLUME']._serialized_start=2740
  _globals['_VOLUME']._serialized_end=2829
  _globals['_CONTAINERPORT']._serialized_start=2831
  _globals['_CONTAINERPORT']._serialized_end=2955
  _globals['_ENVVAR']._serialized_start=2957
  _globals['_ENVVAR']._serialized_end=3028
  _globals['_RESOURCEREQUESTS']._serialized_start=3030
  _globals['_RESOURCEREQUESTS']._serialized_end=3111
  _globals['_RESOURCELIMITS']._serialized_start=3113
  _globals['_RESOURCELIMITS']._serialized_end=3192
  _globals['_VOLUMEMOUNT']._serialized_start=3194
  _globals['_VOLUMEMOUNT']._serialized_end=3260
  _globals['_PROBE']._serialized_start=3263
  _globals['_PROBE']._serialized_end=3459
  _globals['_SECURITYCONTEXT']._serialized_start=3461
  _globals['_SECURITYCONTEXT']._serialized_end=3576
  _globals['_AFFINITYRULE']._serialized_start=3578
  _globals['_AFFINITYRULE']._serialized_end=3627
  _globals['_NODESELECTOR']._serialized_start=3630
  _globals['_NODESELECTOR']._serialized_end=3764
  _globals['_NODESELECTOR_MATCHLABELSENTRY']._serialized_start=1732
  _globals['_NODESELECTOR_MATCHLABELSENTRY']._serialized_end=1782
  _globals['_TOLERATION']._serialized_start=3766
  _globals['_TOLERATION']._serialized_end=3840
  _globals['_ROLLOUTSETTINGS']._serialized_start=3842
  _globals['_ROLLOUTSETTINGS']._serialized_end=3903
  _globals['_LIFECYCLEHOOK']._serialized_start=3905
  _globals['_LIFECYCLEHOOK']._serialized_end=3974
  _globals['_PRIORITYCLASS']._serialized_start=3976
  _globals['_PRIORITYCLASS']._serialized_end=4005
  _globals['_DEPLOYMENTSTATUS']._serialized_start=4008
  _globals['_DEPLOYMENTSTATUS']._serialized_end=4209
  _globals['_CONDITION']._serialized_start=4212
  _globals['_CONDITION']._serialized_end=4398
# @@protoc_insertion_point(module_scope)
