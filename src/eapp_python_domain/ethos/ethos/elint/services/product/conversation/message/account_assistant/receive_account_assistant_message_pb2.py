# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethos/elint/services/product/conversation/message/account_assistant/receive_account_assistant_message.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ethos.elint.entities import account_assistant_pb2 as ethos_dot_elint_dot_entities_dot_account__assistant__pb2
try:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_account__assistant__pb2.google_dot_protobuf_dot_timestamp__pb2
except AttributeError:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_account__assistant__pb2.google.protobuf.timestamp_pb2
from ethos.elint.entities import space_knowledge_pb2 as ethos_dot_elint_dot_entities_dot_space__knowledge__pb2
try:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_space__knowledge__pb2.google_dot_protobuf_dot_timestamp__pb2
except AttributeError:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_space__knowledge__pb2.google.protobuf.timestamp_pb2

from google.protobuf.timestamp_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nkethos/elint/services/product/conversation/message/account_assistant/receive_account_assistant_message.proto\x12=elint.services.product.conversation.message.account.assistant\x1a\x1fgoogle/protobuf/timestamp.proto\x1a,ethos/elint/entities/account_assistant.proto\x1a*ethos/elint/entities/space_knowledge.proto\"\xf7\x01\n\x12MessageFromAccount\x12\x1c\n\x14\x61\x63\x63ount_assistant_id\x18\x01 \x01(\t\x12I\n\x11\x63onnected_account\x18\x02 \x01(\x0b\x32..elint.entity.AccountAssistantConnectedAccount\x12\x42\n\x16space_knowledge_action\x18\x03 \x01(\x0e\x32\".elint.entity.SpaceKnowledgeAction\x12\x0f\n\x07message\x18\x04 \x01(\t\x12#\n\x1b\x61\x63\x63ount_received_message_id\x18\x05 \x01(\t\"b\n\x1aMessageFromAccountReceived\x12\x13\n\x0bis_received\x18\x01 \x01(\x08\x12/\n\x0breceived_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xf5\x01\n%ReceiveAccountAssistantMessageService\x12\xcb\x01\n\x19ReceiveMessageFromAccount\x12Q.elint.services.product.conversation.message.account.assistant.MessageFromAccount\x1aY.elint.services.product.conversation.message.account.assistant.MessageFromAccountReceived\"\x00P\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethos.elint.services.product.conversation.message.account_assistant.receive_account_assistant_message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MESSAGEFROMACCOUNT']._serialized_start=298
  _globals['_MESSAGEFROMACCOUNT']._serialized_end=545
  _globals['_MESSAGEFROMACCOUNTRECEIVED']._serialized_start=547
  _globals['_MESSAGEFROMACCOUNTRECEIVED']._serialized_end=645
  _globals['_RECEIVEACCOUNTASSISTANTMESSAGESERVICE']._serialized_start=648
  _globals['_RECEIVEACCOUNTASSISTANTMESSAGESERVICE']._serialized_end=893
# @@protoc_insertion_point(module_scope)
