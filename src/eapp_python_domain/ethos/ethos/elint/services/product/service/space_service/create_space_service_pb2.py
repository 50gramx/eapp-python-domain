# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethos/elint/services/product/service/space_service/create_space_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ethos.elint.services.product.identity.space import access_space_pb2 as ethos_dot_elint_dot_services_dot_product_dot_identity_dot_space_dot_access__space__pb2
from ethos.elint.services.product.service.space_service import access_space_service_pb2 as ethos_dot_elint_dot_services_dot_product_dot_service_dot_space__service_dot_access__space__service__pb2

from google.protobuf.timestamp_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMethos/elint/services/product/service/space_service/create_space_service.proto\x12$elint.services.product.service.space\x1a\x1fgoogle/protobuf/timestamp.proto\x1a>ethos/elint/services/product/identity/space/access_space.proto\x1aMethos/elint/services/product/service/space_service/access_space_service.proto\"\xe2\x01\n CreateAccountSpaceServiceRequest\x12p\n!space_service_access_auth_details\x18\x01 \x01(\x0b\x32\x45.elint.services.product.identity.space.SpaceServicesAccessAuthDetails\x12\x1a\n\x12space_service_name\x18\x02 \x01(\t\x12\x30\n\x0crequested_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xfd\x01\n!CreateAccountSpaceServiceResponse\x12\x7f\n*space_service_services_access_auth_details\x18\x01 \x01(\x0b\x32K.elint.services.product.service.space.SpaceServiceServicesAccessAuthDetails\x12)\n!create_account_space_service_done\x18\x02 \x01(\x08\x12,\n$create_account_space_service_message\x18\x03 \x01(\t2\xcc\x01\n\x19\x43reateSpaceServiceService\x12\xae\x01\n\x19\x43reateAccountSpaceService\x12\x46.elint.services.product.service.space.CreateAccountSpaceServiceRequest\x1aG.elint.services.product.service.space.CreateAccountSpaceServiceResponse\"\x00P\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethos.elint.services.product.service.space_service.create_space_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATEACCOUNTSPACESERVICEREQUEST']._serialized_start=296
  _globals['_CREATEACCOUNTSPACESERVICEREQUEST']._serialized_end=522
  _globals['_CREATEACCOUNTSPACESERVICERESPONSE']._serialized_start=525
  _globals['_CREATEACCOUNTSPACESERVICERESPONSE']._serialized_end=778
  _globals['_CREATESPACESERVICESERVICE']._serialized_start=781
  _globals['_CREATESPACESERVICESERVICE']._serialized_end=985
# @@protoc_insertion_point(module_scope)
