from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateAccountRequest(_message.Message):
    __slots__ = ("account_mobile_number", "requested_at", "account_mobile_country_code")
    ACCOUNT_MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_MOBILE_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    account_mobile_number: str
    requested_at: _timestamp_pb2_1.Timestamp
    account_mobile_country_code: str
    def __init__(self, account_mobile_number: _Optional[str] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., account_mobile_country_code: _Optional[str] = ...) -> None: ...

class ValidateAccountResponse(_message.Message):
    __slots__ = ("account_access_auth_details", "account_exists", "verification_code_token_details", "code_sent_at", "validate_account_done", "validate_account_message")
    ACCOUNT_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CODE_SENT_AT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ACCOUNT_DONE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ACCOUNT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    account_access_auth_details: AccountAccessAuthDetails
    account_exists: bool
    verification_code_token_details: _generic_pb2.TemporaryTokenDetails
    code_sent_at: _timestamp_pb2_1.Timestamp
    validate_account_done: bool
    validate_account_message: str
    def __init__(self, account_access_auth_details: _Optional[_Union[AccountAccessAuthDetails, _Mapping]] = ..., account_exists: bool = ..., verification_code_token_details: _Optional[_Union[_generic_pb2.TemporaryTokenDetails, _Mapping]] = ..., code_sent_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., validate_account_done: bool = ..., validate_account_message: _Optional[str] = ...) -> None: ...

class VerifyAccountRequest(_message.Message):
    __slots__ = ("account_access_auth_details", "resend_code", "verification_code_token_details", "verification_code", "account_device_details", "requested_at")
    ACCOUNT_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    RESEND_CODE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    account_access_auth_details: AccountAccessAuthDetails
    resend_code: bool
    verification_code_token_details: _generic_pb2.TemporaryTokenDetails
    verification_code: str
    account_device_details: _account_pb2.AccountDeviceDetails
    requested_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account_access_auth_details: _Optional[_Union[AccountAccessAuthDetails, _Mapping]] = ..., resend_code: bool = ..., verification_code_token_details: _Optional[_Union[_generic_pb2.TemporaryTokenDetails, _Mapping]] = ..., verification_code: _Optional[str] = ..., account_device_details: _Optional[_Union[_account_pb2.AccountDeviceDetails, _Mapping]] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class VerifyAccountResponse(_message.Message):
    __slots__ = ("account_service_access_auth_details", "verification_done", "verification_message")
    ACCOUNT_SERVICE_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_DONE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    account_service_access_auth_details: AccountServicesAccessAuthDetails
    verification_done: bool
    verification_message: str
    def __init__(self, account_service_access_auth_details: _Optional[_Union[AccountServicesAccessAuthDetails, _Mapping]] = ..., verification_done: bool = ..., verification_message: _Optional[str] = ...) -> None: ...

class ValidateAccountServicesResponse(_message.Message):
    __slots__ = ("account_service_access_validation_done", "account_service_access_validation_message")
    ACCOUNT_SERVICE_ACCESS_VALIDATION_DONE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_SERVICE_ACCESS_VALIDATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    account_service_access_validation_done: bool
    account_service_access_validation_message: str
    def __init__(self, account_service_access_validation_done: bool = ..., account_service_access_validation_message: _Optional[str] = ...) -> None: ...

class ReAccountAccessTokenRequest(_message.Message):
    __slots__ = ("account_service_access_auth_details",)
    ACCOUNT_SERVICE_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    account_service_access_auth_details: AccountServicesAccessAuthDetails
    def __init__(self, account_service_access_auth_details: _Optional[_Union[AccountServicesAccessAuthDetails, _Mapping]] = ...) -> None: ...

class ReAccountAccessTokenResponse(_message.Message):
    __slots__ = ("account_service_access_auth_details", "response_meta")
    ACCOUNT_SERVICE_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_service_access_auth_details: AccountServicesAccessAuthDetails
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_service_access_auth_details: _Optional[_Union[AccountServicesAccessAuthDetails, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class AccountAccessAuthDetails(_message.Message):
    __slots__ = ("account_mobile_number", "account_access_auth_session_token_details")
    ACCOUNT_MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ACCESS_AUTH_SESSION_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    account_mobile_number: str
    account_access_auth_session_token_details: _generic_pb2.PersistentSessionTokenDetails
    def __init__(self, account_mobile_number: _Optional[str] = ..., account_access_auth_session_token_details: _Optional[_Union[_generic_pb2.PersistentSessionTokenDetails, _Mapping]] = ...) -> None: ...

class AccountServicesAccessAuthDetails(_message.Message):
    __slots__ = ("account", "account_services_access_session_token_details", "requested_at")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_SERVICES_ACCESS_SESSION_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    account: _account_pb2.Account
    account_services_access_session_token_details: _generic_pb2.PersistentSessionTokenDetails
    requested_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., account_services_access_session_token_details: _Optional[_Union[_generic_pb2.PersistentSessionTokenDetails, _Mapping]] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...
