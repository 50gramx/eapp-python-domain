from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from ethos.elint.services.product.identity.account_assistant import access_account_assistant_pb2 as _access_account_assistant_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAccountAssistantRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_assistant_name")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_NAME_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_assistant_name: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_assistant_name: _Optional[str] = ...) -> None: ...

class CreateAccountAssistantResponse(_message.Message):
    __slots__ = ("account_assistant_services_access_auth_details", "response_meta")
    ACCOUNT_ASSISTANT_SERVICES_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_assistant_services_access_auth_details: _access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_assistant_services_access_auth_details: _Optional[_Union[_access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetAccountAssistantNameCodeRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_assistant_name")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_NAME_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_assistant_name: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_assistant_name: _Optional[str] = ...) -> None: ...

class GetAccountAssistantNameCodeResponse(_message.Message):
    __slots__ = ("account_assistant_name_code", "response_meta")
    ACCOUNT_ASSISTANT_NAME_CODE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_assistant_name_code: int
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_assistant_name_code: _Optional[int] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...
