# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethos/elint/services/product/identity/galaxy/create_galaxy.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ethos.elint.entities import account_pb2 as ethos_dot_elint_dot_entities_dot_account__pb2
try:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_account__pb2.google_dot_protobuf_dot_timestamp__pb2
except AttributeError:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_account__pb2.google.protobuf.timestamp_pb2
from ethos.elint.entities import universe_pb2 as ethos_dot_elint_dot_entities_dot_universe__pb2
try:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_universe__pb2.google_dot_protobuf_dot_timestamp__pb2
except AttributeError:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_universe__pb2.google.protobuf.timestamp_pb2
from ethos.elint.entities import galaxy_pb2 as ethos_dot_elint_dot_entities_dot_galaxy__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@ethos/elint/services/product/identity/galaxy/create_galaxy.proto\x12&elint.services.product.identity.galaxy\x1a\"ethos/elint/entities/account.proto\x1a#ethos/elint/entities/universe.proto\x1a!ethos/elint/entities/galaxy.proto\"\x80\x01\n\x13\x43reateGalaxyRequest\x12\x13\n\x0bgalaxy_name\x18\x01 \x01(\t\x12(\n\x08universe\x18\x02 \x01(\x0b\x32\x16.elint.entity.Universe\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\x1a\n\x12galaxy_description\x18\x04 \x01(\t\"<\n\x14\x43reateGalaxyResponse\x12$\n\x06galaxy\x18\x01 \x01(\x0b\x32\x14.elint.entity.Galaxy2\xa1\x01\n\x13\x43reateGalaxyService\x12\x89\x01\n\x0c\x43reateGalaxy\x12;.elint.services.product.identity.galaxy.CreateGalaxyRequest\x1a<.elint.services.product.identity.galaxy.CreateGalaxyResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethos.elint.services.product.identity.galaxy.create_galaxy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATEGALAXYREQUEST']._serialized_start=217
  _globals['_CREATEGALAXYREQUEST']._serialized_end=345
  _globals['_CREATEGALAXYRESPONSE']._serialized_start=347
  _globals['_CREATEGALAXYRESPONSE']._serialized_end=407
  _globals['_CREATEGALAXYSERVICE']._serialized_start=410
  _globals['_CREATEGALAXYSERVICE']._serialized_end=571
# @@protoc_insertion_point(module_scope)
