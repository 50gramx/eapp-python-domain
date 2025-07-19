from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateAccountWithMobileRequest(_message.Message):
    __slots__ = ("account_mobile_country_code", "account_mobile_number", "requested_at")
    ACCOUNT_MOBILE_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    account_mobile_country_code: str
    account_mobile_number: str
    requested_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account_mobile_country_code: _Optional[str] = ..., account_mobile_number: _Optional[str] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class ValidateAccountWithMobileResponse(_message.Message):
    __slots__ = ("account_creation_auth_details", "account_exists_with_mobile", "verification_code_token_details", "code_sent_at", "validate_account_with_mobile_done", "validate_account_with_mobile_message")
    ACCOUNT_CREATION_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_EXISTS_WITH_MOBILE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CODE_SENT_AT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ACCOUNT_WITH_MOBILE_DONE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ACCOUNT_WITH_MOBILE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    account_creation_auth_details: AccountCreationAuthDetails
    account_exists_with_mobile: bool
    verification_code_token_details: _generic_pb2.TemporaryTokenDetails
    code_sent_at: _timestamp_pb2_1.Timestamp
    validate_account_with_mobile_done: bool
    validate_account_with_mobile_message: str
    def __init__(self, account_creation_auth_details: _Optional[_Union[AccountCreationAuthDetails, _Mapping]] = ..., account_exists_with_mobile: bool = ..., verification_code_token_details: _Optional[_Union[_generic_pb2.TemporaryTokenDetails, _Mapping]] = ..., code_sent_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., validate_account_with_mobile_done: bool = ..., validate_account_with_mobile_message: _Optional[str] = ...) -> None: ...

class VerificationAccountRequest(_message.Message):
    __slots__ = ("account_creation_auth_details", "resend_code", "verification_code", "verification_code_token_details", "requested_at")
    ACCOUNT_CREATION_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    RESEND_CODE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    account_creation_auth_details: AccountCreationAuthDetails
    resend_code: bool
    verification_code: str
    verification_code_token_details: _generic_pb2.TemporaryTokenDetails
    requested_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account_creation_auth_details: _Optional[_Union[AccountCreationAuthDetails, _Mapping]] = ..., resend_code: bool = ..., verification_code: _Optional[str] = ..., verification_code_token_details: _Optional[_Union[_generic_pb2.TemporaryTokenDetails, _Mapping]] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class VerificationAccountResponse(_message.Message):
    __slots__ = ("verification_done", "verification_message")
    VERIFICATION_DONE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    verification_done: bool
    verification_message: str
    def __init__(self, verification_done: bool = ..., verification_message: _Optional[str] = ...) -> None: ...

class CaptureAccountMetaDetailsRequest(_message.Message):
    __slots__ = ("account_creation_auth_details", "account_first_name", "account_last_name", "account_birth_at", "account_gender", "account_device_details", "account_assistant_name", "requested_at")
    ACCOUNT_CREATION_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_BIRTH_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_GENDER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    account_creation_auth_details: AccountCreationAuthDetails
    account_first_name: str
    account_last_name: str
    account_birth_at: _timestamp_pb2_1.Timestamp
    account_gender: _account_pb2.AccountGender
    account_device_details: _account_pb2.AccountDeviceDetails
    account_assistant_name: str
    requested_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account_creation_auth_details: _Optional[_Union[AccountCreationAuthDetails, _Mapping]] = ..., account_first_name: _Optional[str] = ..., account_last_name: _Optional[str] = ..., account_birth_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., account_gender: _Optional[_Union[_account_pb2.AccountGender, str]] = ..., account_device_details: _Optional[_Union[_account_pb2.AccountDeviceDetails, _Mapping]] = ..., account_assistant_name: _Optional[str] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...

class CaptureAccountMetaDetailsResponse(_message.Message):
    __slots__ = ("account_service_access_auth_details", "account_creation_done", "account_creation_message")
    ACCOUNT_SERVICE_ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CREATION_DONE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CREATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    account_service_access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_creation_done: bool
    account_creation_message: str
    def __init__(self, account_service_access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_creation_done: bool = ..., account_creation_message: _Optional[str] = ...) -> None: ...

class AccountCreationAuthDetails(_message.Message):
    __slots__ = ("account_mobile_country_code", "account_mobile_number", "account_creation_session_token_details", "requested_at")
    ACCOUNT_MOBILE_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CREATION_SESSION_TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    account_mobile_country_code: str
    account_mobile_number: str
    account_creation_session_token_details: _generic_pb2.PersistentSessionTokenDetails
    requested_at: _timestamp_pb2_1.Timestamp
    def __init__(self, account_mobile_country_code: _Optional[str] = ..., account_mobile_number: _Optional[str] = ..., account_creation_session_token_details: _Optional[_Union[_generic_pb2.PersistentSessionTokenDetails, _Mapping]] = ..., requested_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ...) -> None: ...
