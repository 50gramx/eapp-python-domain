# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethos/elint/entities/space_knowledge.proto
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

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*ethos/elint/entities/space_knowledge.proto\x12\x0c\x65lint.entity\x1a ethos/elint/entities/space.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc8\x01\n\x0eSpaceKnowledge\x12\x1c\n\x14space_knowledge_name\x18\x01 \x01(\t\x12\x1a\n\x12space_knowledge_id\x18\x02 \x01(\t\x12(\n space_knowledge_admin_account_id\x18\x03 \x01(\t\x12\"\n\x05space\x18\x04 \x01(\x0b\x32\x13.elint.entity.Space\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xaa\x01\n\x1cSpaceKnowledgeInferredDomain\x12\x1a\n\x12inferred_domain_id\x18\x01 \x01(\t\x12\x1a\n\x12space_knowledge_id\x18\x02 \x01(\t\x12!\n\x19space_knowledge_domain_id\x18\x03 \x01(\t\x12/\n\x0binferred_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*;\n\x14SpaceKnowledgeAction\x12\x10\n\x0c\x41SK_QUESTION\x10\x00\x12\x11\n\rSHOW_URL_PAGE\x10\x01\x42%\n\x0c\x65lint.entityB\x13SpaceKnowledgeProtoP\x01P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethos.elint.entities.space_knowledge_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\014elint.entityB\023SpaceKnowledgeProtoP\001'
  _globals['_SPACEKNOWLEDGEACTION']._serialized_start=503
  _globals['_SPACEKNOWLEDGEACTION']._serialized_end=562
  _globals['_SPACEKNOWLEDGE']._serialized_start=128
  _globals['_SPACEKNOWLEDGE']._serialized_end=328
  _globals['_SPACEKNOWLEDGEINFERREDDOMAIN']._serialized_start=331
  _globals['_SPACEKNOWLEDGEINFERREDDOMAIN']._serialized_end=501
# @@protoc_insertion_point(module_scope)
