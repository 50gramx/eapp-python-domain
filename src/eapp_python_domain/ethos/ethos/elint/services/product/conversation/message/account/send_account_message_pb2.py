# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethos/elint/services/product/conversation/message/account/send_account_message.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ethos.elint.entities import account_pb2 as ethos_dot_elint_dot_entities_dot_account__pb2
try:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_account__pb2.google_dot_protobuf_dot_timestamp__pb2
except AttributeError:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_account__pb2.google.protobuf.timestamp_pb2
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
from ethos.elint.entities import generic_pb2 as ethos_dot_elint_dot_entities_dot_generic__pb2
try:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_generic__pb2.google_dot_protobuf_dot_timestamp__pb2
except AttributeError:
  google_dot_protobuf_dot_timestamp__pb2 = ethos_dot_elint_dot_entities_dot_generic__pb2.google.protobuf.timestamp_pb2
from ethos.elint.services.product.identity.account import access_account_pb2 as ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2

from google.protobuf.timestamp_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nTethos/elint/services/product/conversation/message/account/send_account_message.proto\x12\x33\x65lint.services.product.conversation.message.account\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"ethos/elint/entities/account.proto\x1a,ethos/elint/entities/account_assistant.proto\x1a*ethos/elint/entities/space_knowledge.proto\x1a\"ethos/elint/entities/generic.proto\x1a\x42\x65thos/elint/services/product/identity/account/access_account.proto\"\xae\x02\n\x1aMessageForAccountAssistant\x12\x66\n\x13\x61\x63\x63\x65ss_auth_details\x18\x01 \x01(\x0b\x32I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x12S\n\x1b\x63onnected_account_assistant\x18\x02 \x01(\x0b\x32..elint.entity.AccountConnectedAccountAssistant\x12\x42\n\x16space_knowledge_action\x18\x03 \x01(\x0e\x32\".elint.entity.SpaceKnowledgeAction\x12\x0f\n\x07message\x18\x04 \x01(\t\"\xba\x01\n\x1eMessageForAccountAssistantSent\x12)\n!account_assistant_sent_message_id\x18\x01 \x01(\t\x12\x0f\n\x07is_sent\x18\x02 \x01(\x08\x12+\n\x07sent_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0breceived_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xce\x01\n\x11MessageForAccount\x12\x66\n\x13\x61\x63\x63\x65ss_auth_details\x18\x01 \x01(\x0b\x32I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x12@\n\x11\x63onnected_account\x18\x02 \x01(\x0b\x32%.elint.entity.AccountConnectedAccount\x12\x0f\n\x07message\x18\x03 \x01(\t\"\xa7\x01\n\x15MessageForAccountSent\x12\x1f\n\x17\x61\x63\x63ount_sent_message_id\x18\x01 \x01(\t\x12\x0f\n\x07is_sent\x18\x02 \x01(\x08\x12+\n\x07sent_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0breceived_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xdc\x01\n\x19\x46ullMessageForAccountSent\x12l\n\x18message_for_account_sent\x18\x01 \x01(\x0b\x32J.elint.services.product.conversation.message.account.MessageForAccountSent\x12@\n\x11\x63onnected_account\x18\x02 \x01(\x0b\x32%.elint.entity.AccountConnectedAccount\x12\x0f\n\x07message\x18\x03 \x01(\t\"\xbb\x01\n\x1fSyncAccountSentMessagesResponse\x12\x65\n\x14\x61\x63\x63ount_sent_message\x18\x01 \x01(\x0b\x32G.elint.services.product.conversation.message.account.AccountSentMessage\x12\x31\n\rresponse_meta\x18\x02 \x01(\x0b\x32\x1a.elint.entity.ResponseMeta\"\xda\x01\n.SyncAccountConnectedAccountSentMessagesRequest\x12\x66\n\x13\x61\x63\x63\x65ss_auth_details\x18\x01 \x01(\x0b\x32I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x12@\n\x11\x63onnected_account\x18\x02 \x01(\x0b\x32%.elint.entity.AccountConnectedAccount\"\xe2\x01\n/SyncAccountConnectedAccountSentMessagesResponse\x12\x65\n\x14\x61\x63\x63ount_sent_message\x18\x01 \x01(\x0b\x32G.elint.services.product.conversation.message.account.AccountSentMessage\x12\x31\n\rresponse_meta\x18\x02 \x01(\x0b\x32\x1a.elint.entity.ResponseMeta\x12\x15\n\rsync_progress\x18\x03 \x01(\x01\"\xf6\x01\n7SyncAccountConnectedAccountAssistantSentMessagesRequest\x12\x66\n\x13\x61\x63\x63\x65ss_auth_details\x18\x01 \x01(\x0b\x32I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x12S\n\x1b\x63onnected_account_assistant\x18\x02 \x01(\x0b\x32..elint.entity.AccountConnectedAccountAssistant\"\xfe\x01\n8SyncAccountConnectedAccountAssistantSentMessagesResponse\x12x\n\x1e\x61\x63\x63ount_assistant_sent_message\x18\x01 \x01(\x0b\x32P.elint.services.product.conversation.message.account.AccountAssistantSentMessage\x12\x31\n\rresponse_meta\x18\x02 \x01(\x0b\x32\x1a.elint.entity.ResponseMeta\x12\x15\n\rsync_progress\x18\x03 \x01(\x01\"\xf2\x02\n$GetLast24ProductNSentMessagesRequest\x12\x66\n\x13\x61\x63\x63\x65ss_auth_details\x18\x01 \x01(\x0b\x32I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x12\x11\n\tproduct_n\x18\x02 \x01(\x05\x12\x38\n\x13message_entity_enum\x18\x03 \x01(\x0e\x32\x1b.elint.entity.MessageEntity\x12S\n\x1b\x63onnected_account_assistant\x18\x04 \x01(\x0b\x32..elint.entity.AccountConnectedAccountAssistant\x12@\n\x11\x63onnected_account\x18\x05 \x01(\x0b\x32%.elint.entity.AccountConnectedAccount\"\xbd\x02\n%GetLast24ProductNSentMessagesResponse\x12\x31\n\rresponse_meta\x18\x01 \x01(\x0b\x32\x1a.elint.entity.ResponseMeta\x12\x66\n\x15\x61\x63\x63ount_sent_messages\x18\x02 \x03(\x0b\x32G.elint.services.product.conversation.message.account.AccountSentMessage\x12y\n\x1f\x61\x63\x63ount_assistant_sent_messages\x18\x03 \x03(\x0b\x32P.elint.services.product.conversation.message.account.AccountAssistantSentMessage\"\xa8\x01\n GetAccountLastSentMessageRequest\x12\x66\n\x13\x61\x63\x63\x65ss_auth_details\x18\x01 \x01(\x0b\x32I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x12\x1c\n\x14\x63onnected_account_id\x18\x02 \x01(\t\"\xba\x01\n!GetAccountLastSentMessageResponse\x12\x31\n\rresponse_meta\x18\x01 \x01(\x0b\x32\x1a.elint.entity.ResponseMeta\x12\x62\n\x11last_sent_message\x18\x02 \x01(\x0b\x32G.elint.services.product.conversation.message.account.AccountSentMessage\"\xbb\x01\n)GetAccountAssistantLastSentMessageRequest\x12\x66\n\x13\x61\x63\x63\x65ss_auth_details\x18\x01 \x01(\x0b\x32I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x12&\n\x1e\x63onnected_account_assistant_id\x18\x02 \x01(\t\"\xcc\x01\n*GetAccountAssistantLastSentMessageResponse\x12\x31\n\rresponse_meta\x18\x01 \x01(\x0b\x32\x1a.elint.entity.ResponseMeta\x12k\n\x11last_sent_message\x18\x02 \x01(\x0b\x32P.elint.services.product.conversation.message.account.AccountAssistantSentMessage\"\x8b\x01\n\x1fGetSentMessagesAccountsResponse\x12\x31\n\rresponse_meta\x18\x01 \x01(\x0b\x32\x1a.elint.entity.ResponseMeta\x12\x35\n\x16sent_messages_accounts\x18\x02 \x03(\x0b\x32\x15.elint.entity.Account\"\xa7\x01\n(GetSentMessagesAccountAssistantsResponse\x12\x31\n\rresponse_meta\x18\x01 \x01(\x0b\x32\x1a.elint.entity.ResponseMeta\x12H\n sent_messages_account_assistants\x18\x02 \x03(\x0b\x32\x1e.elint.entity.AccountAssistant\"\xe4\x02\n\x1b\x41\x63\x63ountAssistantSentMessage\x12)\n!account_assistant_sent_message_id\x18\x01 \x01(\t\x12\x1c\n\x14\x61\x63\x63ount_assistant_id\x18\x02 \x01(\t\x12\'\n\x1f\x61\x63\x63ount_assistant_connection_id\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x15\n\rmessage_space\x18\x05 \x01(\x05\x12\x1c\n\x14message_space_action\x18\x06 \x01(\x05\x12+\n\x07sent_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0breceived_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0cmessage_info\x18\t \x01(\x0b\x32\x19.elint.entity.MessageInfo\"\x88\x02\n\x12\x41\x63\x63ountSentMessage\x12\x1f\n\x17\x61\x63\x63ount_sent_message_id\x18\x01 \x01(\t\x12\x12\n\naccount_id\x18\x02 \x01(\t\x12\x1d\n\x15\x61\x63\x63ount_connection_id\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12+\n\x07sent_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0breceived_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0cmessage_info\x18\x07 \x01(\x0b\x32\x19.elint.entity.MessageInfo\"z\n AccountSentMessagesCountResponse\x12#\n\x1b\x61\x63\x63ount_sent_messages_count\x18\x01 \x01(\x05\x12\x31\n\rresponse_meta\x18\x02 \x01(\x0b\x32\x1a.elint.entity.ResponseMeta\"\x8d\x01\n)AccountAssistantSentMessagesCountResponse\x12-\n%account_assistant_sent_messages_count\x18\x01 \x01(\x05\x12\x31\n\rresponse_meta\x18\x02 \x01(\x0b\x32\x1a.elint.entity.ResponseMeta2\xa6\x17\n\x19SendAccountMessageService\x12\xc7\x01\n\x1dSendMessageToAccountAssistant\x12O.elint.services.product.conversation.message.account.MessageForAccountAssistant\x1aS.elint.services.product.conversation.message.account.MessageForAccountAssistantSent\"\x00\x12\xac\x01\n\x14SendMessageToAccount\x12\x46.elint.services.product.conversation.message.account.MessageForAccount\x1aJ.elint.services.product.conversation.message.account.MessageForAccountSent\"\x00\x12\xb9\x01\n\x19SendSpeedMessageToAccount\x12\x46.elint.services.product.conversation.message.account.MessageForAccount\x1aN.elint.services.product.conversation.message.account.FullMessageForAccountSent\"\x00(\x01\x30\x01\x12\xc3\x01\n SyncAccountAssistantSentMessages\x12I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x1aP.elint.services.product.conversation.message.account.AccountAssistantSentMessage\"\x00\x30\x01\x12\xbe\x01\n\x17SyncAccountSentMessages\x12I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x1aT.elint.services.product.conversation.message.account.SyncAccountSentMessagesResponse\"\x00\x30\x01\x12\xf8\x01\n\'SyncAccountConnectedAccountSentMessages\x12\x63.elint.services.product.conversation.message.account.SyncAccountConnectedAccountSentMessagesRequest\x1a\x64.elint.services.product.conversation.message.account.SyncAccountConnectedAccountSentMessagesResponse\"\x00\x30\x01\x12\x93\x02\n0SyncAccountConnectedAccountAssistantSentMessages\x12l.elint.services.product.conversation.message.account.SyncAccountConnectedAccountAssistantSentMessagesRequest\x1am.elint.services.product.conversation.message.account.SyncAccountConnectedAccountAssistantSentMessagesResponse\"\x00\x30\x01\x12\xd8\x01\n\x1dGetLast24ProductNSentMessages\x12Y.elint.services.product.conversation.message.account.GetLast24ProductNSentMessagesRequest\x1aZ.elint.services.product.conversation.message.account.GetLast24ProductNSentMessagesResponse\"\x00\x12\xc1\x01\n\x1bGetAccountSentMessagesCount\x12I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x1aU.elint.services.product.conversation.message.account.AccountSentMessagesCountResponse\"\x00\x12\xd3\x01\n$GetAccountAssistantSentMessagesCount\x12I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x1a^.elint.services.product.conversation.message.account.AccountAssistantSentMessagesCountResponse\"\x00\x12\xcc\x01\n\x19GetAccountLastSentMessage\x12U.elint.services.product.conversation.message.account.GetAccountLastSentMessageRequest\x1aV.elint.services.product.conversation.message.account.GetAccountLastSentMessageResponse\"\x00\x12\xe7\x01\n\"GetAccountAssistantLastSentMessage\x12^.elint.services.product.conversation.message.account.GetAccountAssistantLastSentMessageRequest\x1a_.elint.services.product.conversation.message.account.GetAccountAssistantLastSentMessageResponse\"\x00\x12\xbc\x01\n\x17GetSentMessagesAccounts\x12I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x1aT.elint.services.product.conversation.message.account.GetSentMessagesAccountsResponse\"\x00\x12\xce\x01\n GetSentMessagesAccountAssistants\x12I.elint.services.product.identity.account.AccountServicesAccessAuthDetails\x1a].elint.services.product.conversation.message.account.GetSentMessagesAccountAssistantsResponse\"\x00P\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethos.elint.services.product.conversation.message.account.send_account_message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MESSAGEFORACCOUNTASSISTANT']._serialized_start=405
  _globals['_MESSAGEFORACCOUNTASSISTANT']._serialized_end=707
  _globals['_MESSAGEFORACCOUNTASSISTANTSENT']._serialized_start=710
  _globals['_MESSAGEFORACCOUNTASSISTANTSENT']._serialized_end=896
  _globals['_MESSAGEFORACCOUNT']._serialized_start=899
  _globals['_MESSAGEFORACCOUNT']._serialized_end=1105
  _globals['_MESSAGEFORACCOUNTSENT']._serialized_start=1108
  _globals['_MESSAGEFORACCOUNTSENT']._serialized_end=1275
  _globals['_FULLMESSAGEFORACCOUNTSENT']._serialized_start=1278
  _globals['_FULLMESSAGEFORACCOUNTSENT']._serialized_end=1498
  _globals['_SYNCACCOUNTSENTMESSAGESRESPONSE']._serialized_start=1501
  _globals['_SYNCACCOUNTSENTMESSAGESRESPONSE']._serialized_end=1688
  _globals['_SYNCACCOUNTCONNECTEDACCOUNTSENTMESSAGESREQUEST']._serialized_start=1691
  _globals['_SYNCACCOUNTCONNECTEDACCOUNTSENTMESSAGESREQUEST']._serialized_end=1909
  _globals['_SYNCACCOUNTCONNECTEDACCOUNTSENTMESSAGESRESPONSE']._serialized_start=1912
  _globals['_SYNCACCOUNTCONNECTEDACCOUNTSENTMESSAGESRESPONSE']._serialized_end=2138
  _globals['_SYNCACCOUNTCONNECTEDACCOUNTASSISTANTSENTMESSAGESREQUEST']._serialized_start=2141
  _globals['_SYNCACCOUNTCONNECTEDACCOUNTASSISTANTSENTMESSAGESREQUEST']._serialized_end=2387
  _globals['_SYNCACCOUNTCONNECTEDACCOUNTASSISTANTSENTMESSAGESRESPONSE']._serialized_start=2390
  _globals['_SYNCACCOUNTCONNECTEDACCOUNTASSISTANTSENTMESSAGESRESPONSE']._serialized_end=2644
  _globals['_GETLAST24PRODUCTNSENTMESSAGESREQUEST']._serialized_start=2647
  _globals['_GETLAST24PRODUCTNSENTMESSAGESREQUEST']._serialized_end=3017
  _globals['_GETLAST24PRODUCTNSENTMESSAGESRESPONSE']._serialized_start=3020
  _globals['_GETLAST24PRODUCTNSENTMESSAGESRESPONSE']._serialized_end=3337
  _globals['_GETACCOUNTLASTSENTMESSAGEREQUEST']._serialized_start=3340
  _globals['_GETACCOUNTLASTSENTMESSAGEREQUEST']._serialized_end=3508
  _globals['_GETACCOUNTLASTSENTMESSAGERESPONSE']._serialized_start=3511
  _globals['_GETACCOUNTLASTSENTMESSAGERESPONSE']._serialized_end=3697
  _globals['_GETACCOUNTASSISTANTLASTSENTMESSAGEREQUEST']._serialized_start=3700
  _globals['_GETACCOUNTASSISTANTLASTSENTMESSAGEREQUEST']._serialized_end=3887
  _globals['_GETACCOUNTASSISTANTLASTSENTMESSAGERESPONSE']._serialized_start=3890
  _globals['_GETACCOUNTASSISTANTLASTSENTMESSAGERESPONSE']._serialized_end=4094
  _globals['_GETSENTMESSAGESACCOUNTSRESPONSE']._serialized_start=4097
  _globals['_GETSENTMESSAGESACCOUNTSRESPONSE']._serialized_end=4236
  _globals['_GETSENTMESSAGESACCOUNTASSISTANTSRESPONSE']._serialized_start=4239
  _globals['_GETSENTMESSAGESACCOUNTASSISTANTSRESPONSE']._serialized_end=4406
  _globals['_ACCOUNTASSISTANTSENTMESSAGE']._serialized_start=4409
  _globals['_ACCOUNTASSISTANTSENTMESSAGE']._serialized_end=4765
  _globals['_ACCOUNTSENTMESSAGE']._serialized_start=4768
  _globals['_ACCOUNTSENTMESSAGE']._serialized_end=5032
  _globals['_ACCOUNTSENTMESSAGESCOUNTRESPONSE']._serialized_start=5034
  _globals['_ACCOUNTSENTMESSAGESCOUNTRESPONSE']._serialized_end=5156
  _globals['_ACCOUNTASSISTANTSENTMESSAGESCOUNTRESPONSE']._serialized_start=5159
  _globals['_ACCOUNTASSISTANTSENTMESSAGESCOUNTRESPONSE']._serialized_end=5300
  _globals['_SENDACCOUNTMESSAGESERVICE']._serialized_start=5303
  _globals['_SENDACCOUNTMESSAGESERVICE']._serialized_end=8285
# @@protoc_insertion_point(module_scope)
