from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAccountAssistantMetaByAccountIdRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetAccountAssistantMetaByAccountIdResponse(_message.Message):
    __slots__ = ("account_assistant_meta", "response_meta")
    ACCOUNT_ASSISTANT_META_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_assistant_meta: _account_assistant_pb2.AccountAssistantMeta
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_assistant_meta: _Optional[_Union[_account_assistant_pb2.AccountAssistantMeta, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetAccountAssistantMetaByAccountAssistantIdRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_assistant_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_assistant_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_assistant_id: _Optional[str] = ...) -> None: ...

class GetAccountAssistantMetaByAccountAssistantIdResponse(_message.Message):
    __slots__ = ("account_assistant_meta", "response_meta")
    ACCOUNT_ASSISTANT_META_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_assistant_meta: _account_assistant_pb2.AccountAssistantMeta
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_assistant_meta: _Optional[_Union[_account_assistant_pb2.AccountAssistantMeta, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetAccountAssistantByIdRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_assistant_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_assistant_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_assistant_id: _Optional[str] = ...) -> None: ...

class GetAccountAssistantByIdResponse(_message.Message):
    __slots__ = ("response_meta", "account_assistant")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    account_assistant: _account_assistant_pb2.AccountAssistant
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., account_assistant: _Optional[_Union[_account_assistant_pb2.AccountAssistant, _Mapping]] = ...) -> None: ...

class GetAccountAssistantNameCodeByIdRequest(_message.Message):
    __slots__ = ("account_assistant_id",)
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    account_assistant_id: str
    def __init__(self, account_assistant_id: _Optional[str] = ...) -> None: ...

class GetAccountAssistantNameCodeByIdResponse(_message.Message):
    __slots__ = ("account_assistant_name_code", "account_assistant_name")
    ACCOUNT_ASSISTANT_NAME_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_NAME_FIELD_NUMBER: _ClassVar[int]
    account_assistant_name_code: int
    account_assistant_name: str
    def __init__(self, account_assistant_name_code: _Optional[int] = ..., account_assistant_name: _Optional[str] = ...) -> None: ...
