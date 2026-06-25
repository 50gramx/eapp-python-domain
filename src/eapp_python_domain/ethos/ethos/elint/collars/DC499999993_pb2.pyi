from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DC499999993(_message.Message):
    __slots__ = ("id", "name", "description", "mail_message", "mailbox", "contact_key", "thread", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MAIL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_FIELD_NUMBER: _ClassVar[int]
    CONTACT_KEY_FIELD_NUMBER: _ClassVar[int]
    THREAD_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    mail_message: MailMessage
    mailbox: MailBox
    contact_key: ContactKey
    thread: MailThread
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., mail_message: _Optional[_Union[MailMessage, _Mapping]] = ..., mailbox: _Optional[_Union[MailBox, _Mapping]] = ..., contact_key: _Optional[_Union[ContactKey, _Mapping]] = ..., thread: _Optional[_Union[MailThread, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MailMessage(_message.Message):
    __slots__ = ("id", "from_address", "to_address", "encrypted_envelope", "envelope_nonce", "envelope_mac", "sender_signature", "sender_kx_pubkey", "sender_sig_pubkey", "sent_at", "received_at", "thread_id", "envelope_version")
    ID_FIELD_NUMBER: _ClassVar[int]
    FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_NONCE_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_MAC_FIELD_NUMBER: _ClassVar[int]
    SENDER_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SENDER_KX_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    SENDER_SIG_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    from_address: str
    to_address: str
    encrypted_envelope: bytes
    envelope_nonce: bytes
    envelope_mac: bytes
    sender_signature: bytes
    sender_kx_pubkey: bytes
    sender_sig_pubkey: bytes
    sent_at: _timestamp_pb2.Timestamp
    received_at: _timestamp_pb2.Timestamp
    thread_id: str
    envelope_version: int
    def __init__(self, id: _Optional[str] = ..., from_address: _Optional[str] = ..., to_address: _Optional[str] = ..., encrypted_envelope: _Optional[bytes] = ..., envelope_nonce: _Optional[bytes] = ..., envelope_mac: _Optional[bytes] = ..., sender_signature: _Optional[bytes] = ..., sender_kx_pubkey: _Optional[bytes] = ..., sender_sig_pubkey: _Optional[bytes] = ..., sent_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., thread_id: _Optional[str] = ..., envelope_version: _Optional[int] = ...) -> None: ...

class MailBox(_message.Message):
    __slots__ = ("id", "owner_address", "unread_count", "total_count", "last_received_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    owner_address: str
    unread_count: int
    total_count: int
    last_received_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., owner_address: _Optional[str] = ..., unread_count: _Optional[int] = ..., total_count: _Optional[int] = ..., last_received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ContactKey(_message.Message):
    __slots__ = ("address", "kx_pubkey", "sig_pubkey", "transport_hint", "last_verified", "verified_via")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    KX_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    SIG_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_HINT_FIELD_NUMBER: _ClassVar[int]
    LAST_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_VIA_FIELD_NUMBER: _ClassVar[int]
    address: str
    kx_pubkey: bytes
    sig_pubkey: bytes
    transport_hint: str
    last_verified: _timestamp_pb2.Timestamp
    verified_via: str
    def __init__(self, address: _Optional[str] = ..., kx_pubkey: _Optional[bytes] = ..., sig_pubkey: _Optional[bytes] = ..., transport_hint: _Optional[str] = ..., last_verified: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., verified_via: _Optional[str] = ...) -> None: ...

class MailThread(_message.Message):
    __slots__ = ("id", "participant_addresses", "message_ids", "started_at", "last_message_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    participant_addresses: _containers.RepeatedScalarFieldContainer[str]
    message_ids: _containers.RepeatedScalarFieldContainer[str]
    started_at: _timestamp_pb2.Timestamp
    last_message_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., participant_addresses: _Optional[_Iterable[str]] = ..., message_ids: _Optional[_Iterable[str]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_message_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
