from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class AccountGender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[AccountGender]
    FEMALE: _ClassVar[AccountGender]
    MALE: _ClassVar[AccountGender]

class AccountDeviceOS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IOS: _ClassVar[AccountDeviceOS]
    ANDROID: _ClassVar[AccountDeviceOS]
    MACOS: _ClassVar[AccountDeviceOS]
    WINDOWS: _ClassVar[AccountDeviceOS]
    LINUX: _ClassVar[AccountDeviceOS]
    WEB: _ClassVar[AccountDeviceOS]

class MessageEntity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALL_ENTITY_MESSAGE: _ClassVar[MessageEntity]
    ENTITY_ACCOUNT: _ClassVar[MessageEntity]
    ENTITY_ACCOUNT_ASSISTANT: _ClassVar[MessageEntity]

class AccountPayInMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CARD: _ClassVar[AccountPayInMethod]

class LanguageEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENGLISH: _ClassVar[LanguageEnum]
    HINDI: _ClassVar[LanguageEnum]
    ODIA: _ClassVar[LanguageEnum]
UNKNOWN: AccountGender
FEMALE: AccountGender
MALE: AccountGender
IOS: AccountDeviceOS
ANDROID: AccountDeviceOS
MACOS: AccountDeviceOS
WINDOWS: AccountDeviceOS
LINUX: AccountDeviceOS
WEB: AccountDeviceOS
ALL_ENTITY_MESSAGE: MessageEntity
ENTITY_ACCOUNT: MessageEntity
ENTITY_ACCOUNT_ASSISTANT: MessageEntity
CARD: AccountPayInMethod
ENGLISH: LanguageEnum
HINDI: LanguageEnum
ODIA: LanguageEnum

class Account(_message.Message):
    __slots__ = ("account_analytics_id", "account_id", "account_personal_email_id", "account_work_email_id", "account_country_code", "account_mobile_number", "account_first_name", "account_last_name", "account_galaxy_id", "account_birth_at", "account_gender", "created_at", "account_billing_active")
    ACCOUNT_ANALYTICS_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_PERSONAL_EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_WORK_EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_GALAXY_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_BIRTH_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_GENDER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_BILLING_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    account_analytics_id: str
    account_id: str
    account_personal_email_id: str
    account_work_email_id: str
    account_country_code: str
    account_mobile_number: str
    account_first_name: str
    account_last_name: str
    account_galaxy_id: str
    account_birth_at: _timestamp_pb2.Timestamp
    account_gender: AccountGender
    created_at: _timestamp_pb2.Timestamp
    account_billing_active: bool
    def __init__(self, account_analytics_id: _Optional[str] = ..., account_id: _Optional[str] = ..., account_personal_email_id: _Optional[str] = ..., account_work_email_id: _Optional[str] = ..., account_country_code: _Optional[str] = ..., account_mobile_number: _Optional[str] = ..., account_first_name: _Optional[str] = ..., account_last_name: _Optional[str] = ..., account_galaxy_id: _Optional[str] = ..., account_birth_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_gender: _Optional[_Union[AccountGender, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_billing_active: bool = ...) -> None: ...

class AccountSpaceKnowledgeAccessMeta(_message.Message):
    __slots__ = ("account_id", "knowledge_space_access_session_token", "space_knowledge_id", "access_at")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_SPACE_ACCESS_SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_AT_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    knowledge_space_access_session_token: str
    space_knowledge_id: str
    access_at: _timestamp_pb2.Timestamp
    def __init__(self, account_id: _Optional[str] = ..., knowledge_space_access_session_token: _Optional[str] = ..., space_knowledge_id: _Optional[str] = ..., access_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AccountSpaceKnowledgeDomainAccessMeta(_message.Message):
    __slots__ = ("account_id", "knowledge_space_access_session_token", "space_knowledge_id", "space_knowledge_domain_id", "access_at")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_SPACE_ACCESS_SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_AT_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    knowledge_space_access_session_token: str
    space_knowledge_id: str
    space_knowledge_domain_id: str
    access_at: _timestamp_pb2.Timestamp
    def __init__(self, account_id: _Optional[str] = ..., knowledge_space_access_session_token: _Optional[str] = ..., space_knowledge_id: _Optional[str] = ..., space_knowledge_domain_id: _Optional[str] = ..., access_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AccountSpaceKnowledgeDomainFileAccessMeta(_message.Message):
    __slots__ = ("account_id", "knowledge_space_access_session_token", "space_knowledge_id", "space_knowledge_domain_id", "space_knowledge_domain_file_id", "access_at")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_SPACE_ACCESS_SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_AT_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    knowledge_space_access_session_token: str
    space_knowledge_id: str
    space_knowledge_domain_id: str
    space_knowledge_domain_file_id: str
    access_at: _timestamp_pb2.Timestamp
    def __init__(self, account_id: _Optional[str] = ..., knowledge_space_access_session_token: _Optional[str] = ..., space_knowledge_id: _Optional[str] = ..., space_knowledge_domain_id: _Optional[str] = ..., space_knowledge_domain_file_id: _Optional[str] = ..., access_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AccountConnectedAccount(_message.Message):
    __slots__ = ("account_connection_id", "account_id", "account_interested_in_connection", "connected_account_interested_in_connection", "connected_at")
    ACCOUNT_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_INTERESTED_IN_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_INTERESTED_IN_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_AT_FIELD_NUMBER: _ClassVar[int]
    account_connection_id: str
    account_id: str
    account_interested_in_connection: bool
    connected_account_interested_in_connection: bool
    connected_at: _timestamp_pb2.Timestamp
    def __init__(self, account_connection_id: _Optional[str] = ..., account_id: _Optional[str] = ..., account_interested_in_connection: bool = ..., connected_account_interested_in_connection: bool = ..., connected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AccountConnectedAccountAssistant(_message.Message):
    __slots__ = ("account_assistant_connection_id", "account_assistant_id", "connected_at")
    ACCOUNT_ASSISTANT_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_AT_FIELD_NUMBER: _ClassVar[int]
    account_assistant_connection_id: str
    account_assistant_id: str
    connected_at: _timestamp_pb2.Timestamp
    def __init__(self, account_assistant_connection_id: _Optional[str] = ..., account_assistant_id: _Optional[str] = ..., connected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AccountDeviceDetails(_message.Message):
    __slots__ = ("account_device_os", "device_token")
    ACCOUNT_DEVICE_OS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_device_os: AccountDeviceOS
    device_token: str
    def __init__(self, account_device_os: _Optional[_Union[AccountDeviceOS, str]] = ..., device_token: _Optional[str] = ...) -> None: ...

class AccountMobile(_message.Message):
    __slots__ = ("account_country_code", "account_mobile_number")
    ACCOUNT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    account_country_code: str
    account_mobile_number: str
    def __init__(self, account_country_code: _Optional[str] = ..., account_mobile_number: _Optional[str] = ...) -> None: ...

class AccountMeta(_message.Message):
    __slots__ = ("account_id", "account_first_name", "account_last_name", "account_galaxy_id", "account_gender")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_GALAXY_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_GENDER_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    account_first_name: str
    account_last_name: str
    account_galaxy_id: str
    account_gender: AccountGender
    def __init__(self, account_id: _Optional[str] = ..., account_first_name: _Optional[str] = ..., account_last_name: _Optional[str] = ..., account_galaxy_id: _Optional[str] = ..., account_gender: _Optional[_Union[AccountGender, str]] = ...) -> None: ...

class MessageInfo(_message.Message):
    __slots__ = ("is_urgent", "is_important", "is_sensitive")
    IS_URGENT_FIELD_NUMBER: _ClassVar[int]
    IS_IMPORTANT_FIELD_NUMBER: _ClassVar[int]
    IS_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    is_urgent: bool
    is_important: bool
    is_sensitive: bool
    def __init__(self, is_urgent: bool = ..., is_important: bool = ..., is_sensitive: bool = ...) -> None: ...

class AccountPayInCardDetails(_message.Message):
    __slots__ = ("card_id", "brand", "country", "expiry_month", "expiry_year", "fingerprint", "funding", "last_4_digits")
    CARD_ID_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_MONTH_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_YEAR_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    FUNDING_FIELD_NUMBER: _ClassVar[int]
    LAST_4_DIGITS_FIELD_NUMBER: _ClassVar[int]
    card_id: str
    brand: str
    country: str
    expiry_month: int
    expiry_year: int
    fingerprint: str
    funding: str
    last_4_digits: str
    def __init__(self, card_id: _Optional[str] = ..., brand: _Optional[str] = ..., country: _Optional[str] = ..., expiry_month: _Optional[int] = ..., expiry_year: _Optional[int] = ..., fingerprint: _Optional[str] = ..., funding: _Optional[str] = ..., last_4_digits: _Optional[str] = ...) -> None: ...

class AccountTransaction(_message.Message):
    __slots__ = ("is_debited", "amount", "balance")
    IS_DEBITED_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    is_debited: bool
    amount: float
    balance: float
    def __init__(self, is_debited: bool = ..., amount: _Optional[float] = ..., balance: _Optional[float] = ...) -> None: ...

class AccountPreferredFirstLanguage(_message.Message):
    __slots__ = ("preferred_language",)
    PREFERRED_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    preferred_language: LanguageEnum
    def __init__(self, preferred_language: _Optional[_Union[LanguageEnum, str]] = ...) -> None: ...

class AccountPreferredSecondLanguage(_message.Message):
    __slots__ = ("preferred_language",)
    PREFERRED_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    preferred_language: LanguageEnum
    def __init__(self, preferred_language: _Optional[_Union[LanguageEnum, str]] = ...) -> None: ...

class AccountCurrentLocation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
