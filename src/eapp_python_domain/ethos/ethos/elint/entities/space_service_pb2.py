# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethos/elint/entities/space_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ethos.elint.entities import space_pb2 as ethos_dot_elint_dot_entities_dot_space__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from google.protobuf.timestamp_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(ethos/elint/entities/space_service.proto\x12\x0c\x65lint.entity\x1a ethos/elint/entities/space.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc0\x01\n\x0cSpaceService\x12\x1a\n\x12space_service_name\x18\x01 \x01(\t\x12\x18\n\x10space_service_id\x18\x02 \x01(\t\x12&\n\x1espace_service_admin_account_id\x18\x03 \x01(\t\x12\"\n\x05space\x18\x04 \x01(\x0b\x32\x13.elint.entity.Space\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB#\n\x0c\x65lint.entityB\x11SpaceServiceProtoP\x01P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethos.elint.entities.space_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\014elint.entityB\021SpaceServiceProtoP\001'
  _globals['_SPACESERVICE']._serialized_start=126
  _globals['_SPACESERVICE']._serialized_end=318
# @@protoc_insertion_point(module_scope)
