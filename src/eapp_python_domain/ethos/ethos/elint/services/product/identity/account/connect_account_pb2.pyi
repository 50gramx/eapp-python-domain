from google.protobuf import any_pb2 as _any_pb2
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectedAssistantBelongsTo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCOUNT: _ClassVar[ConnectedAssistantBelongsTo]
    ORGANIZATION: _ClassVar[ConnectedAssistantBelongsTo]
ACCOUNT: ConnectedAssistantBelongsTo
ORGANIZATION: ConnectedAssistantBelongsTo

class ConnectedAssistantWithBelongingEntity(_message.Message):
    __slots__ = ("connected_assistant_belongs_to", "connected_assistant", "assistant", "is_connected_to_belonging_entity", "connected_entity", "belonging_entity_meta", "belonging_entity")
    CONNECTED_ASSISTANT_BELONGS_TO_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    IS_CONNECTED_TO_BELONGING_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    BELONGING_ENTITY_META_FIELD_NUMBER: _ClassVar[int]
    BELONGING_ENTITY_FIELD_NUMBER: _ClassVar[int]
    connected_assistant_belongs_to: ConnectedAssistantBelongsTo
    connected_assistant: _any_pb2.Any
    assistant: _any_pb2.Any
    is_connected_to_belonging_entity: bool
    connected_entity: _any_pb2.Any
    belonging_entity_meta: _any_pb2.Any
    belonging_entity: _any_pb2.Any
    def __init__(self, connected_assistant_belongs_to: _Optional[_Union[ConnectedAssistantBelongsTo, str]] = ..., connected_assistant: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., assistant: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., is_connected_to_belonging_entity: bool = ..., connected_entity: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., belonging_entity_meta: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., belonging_entity: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class GetAccountSelfConnectedAccountAssistantResponse(_message.Message):
    __slots__ = ("connected_account_assistant", "response_meta")
    CONNECTED_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    connected_account_assistant: _account_pb2.AccountConnectedAccountAssistant
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, connected_account_assistant: _Optional[_Union[_account_pb2.AccountConnectedAccountAssistant, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ConnectedAssistantsWithBelongingEntity(_message.Message):
    __slots__ = ("connected_assistant_with_belonging_entity", "response_meta")
    CONNECTED_ASSISTANT_WITH_BELONGING_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    connected_assistant_with_belonging_entity: ConnectedAssistantWithBelongingEntity
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, connected_assistant_with_belonging_entity: _Optional[_Union[ConnectedAssistantWithBelongingEntity, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ConnectedAccountAssistants(_message.Message):
    __slots__ = ("connected_account_assistants", "response_meta")
    CONNECTED_ACCOUNT_ASSISTANTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    connected_account_assistants: _containers.RepeatedCompositeFieldContainer[_account_pb2.AccountConnectedAccountAssistant]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, connected_account_assistants: _Optional[_Iterable[_Union[_account_pb2.AccountConnectedAccountAssistant, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ConnectedAccounts(_message.Message):
    __slots__ = ("connected_accounts", "response_meta")
    CONNECTED_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    connected_accounts: _containers.RepeatedCompositeFieldContainer[_account_pb2.AccountConnectedAccount]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, connected_accounts: _Optional[_Iterable[_Union[_account_pb2.AccountConnectedAccount, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetConnectedAccountRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetConnectedAccountResponse(_message.Message):
    __slots__ = ("connected_account", "response_meta")
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    connected_account: _account_pb2.AccountConnectedAccount
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetConnectedAccountAssistantRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_assistant_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_assistant_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_assistant_id: _Optional[str] = ...) -> None: ...

class GetConnectedAccountAssistantResponse(_message.Message):
    __slots__ = ("connected_account_assistant", "response_meta")
    CONNECTED_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    connected_account_assistant: _account_pb2.AccountConnectedAccountAssistant
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, connected_account_assistant: _Optional[_Union[_account_pb2.AccountConnectedAccountAssistant, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class IsAccountConnectionExistsRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_id: _Optional[str] = ...) -> None: ...

class IsAccountAssistantConnectionExistsRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_assistant_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_assistant_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_assistant_id: _Optional[str] = ...) -> None: ...

class IsAccountAssistantConnectedRequest(_message.Message):
    __slots__ = ("account_id", "connected_account_assistant")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    connected_account_assistant: _account_pb2.AccountConnectedAccountAssistant
    def __init__(self, account_id: _Optional[str] = ..., connected_account_assistant: _Optional[_Union[_account_pb2.AccountConnectedAccountAssistant, _Mapping]] = ...) -> None: ...

class IsAccountConnectedRequest(_message.Message):
    __slots__ = ("account_id", "connected_account")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    connected_account: _account_pb2.AccountConnectedAccount
    def __init__(self, account_id: _Optional[str] = ..., connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ...) -> None: ...

class ParseAccountMobilesRequest(_message.Message):
    __slots__ = ("access_auth_details", "connecting_account_mobile_numbers")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTING_ACCOUNT_MOBILE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connecting_account_mobile_numbers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connecting_account_mobile_numbers: _Optional[_Iterable[str]] = ...) -> None: ...

class ParseAccountMobilesResponse(_message.Message):
    __slots__ = ("account_mobiles", "response_meta")
    ACCOUNT_MOBILES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_mobiles: _containers.RepeatedCompositeFieldContainer[_account_pb2.AccountMobile]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_mobiles: _Optional[_Iterable[_Union[_account_pb2.AccountMobile, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ParseStreamingAccountMobilesRequest(_message.Message):
    __slots__ = ("connecting_account_mobile_numbers",)
    CONNECTING_ACCOUNT_MOBILE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    connecting_account_mobile_numbers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, connecting_account_mobile_numbers: _Optional[_Iterable[str]] = ...) -> None: ...

class ParseStreamingAccountMobilesResponse(_message.Message):
    __slots__ = ("account_mobiles",)
    ACCOUNT_MOBILES_FIELD_NUMBER: _ClassVar[int]
    account_mobiles: _containers.RepeatedCompositeFieldContainer[_account_pb2.AccountMobile]
    def __init__(self, account_mobiles: _Optional[_Iterable[_Union[_account_pb2.AccountMobile, _Mapping]]] = ...) -> None: ...

class SyncAccountConnectionsRequest(_message.Message):
    __slots__ = ("access_auth_details", "connecting_account_mobile")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTING_ACCOUNT_MOBILE_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connecting_account_mobile: _account_pb2.AccountMobile
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connecting_account_mobile: _Optional[_Union[_account_pb2.AccountMobile, _Mapping]] = ...) -> None: ...

class SyncAccountConnectionsResponse(_message.Message):
    __slots__ = ("connected_account", "response_meta")
    class ConnectedAccount(_message.Message):
        __slots__ = ("connected_account", "connected_account_mobile")
        CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_ACCOUNT_MOBILE_FIELD_NUMBER: _ClassVar[int]
        connected_account: _account_pb2.AccountConnectedAccount
        connected_account_mobile: _account_pb2.AccountMobile
        def __init__(self, connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ..., connected_account_mobile: _Optional[_Union[_account_pb2.AccountMobile, _Mapping]] = ...) -> None: ...
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    connected_account: SyncAccountConnectionsResponse.ConnectedAccount
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, connected_account: _Optional[_Union[SyncAccountConnectionsResponse.ConnectedAccount, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ConnectAccountRequest(_message.Message):
    __slots__ = ("access_auth_details", "connecting_account_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTING_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connecting_account_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connecting_account_id: _Optional[str] = ...) -> None: ...

class ConnectAccountResponse(_message.Message):
    __slots__ = ("connected_account", "response_meta")
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    connected_account: _account_pb2.AccountConnectedAccount
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ToggleAccountConnectAccountInterestRequest(_message.Message):
    __slots__ = ("access_auth_details", "connected_account")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    connected_account: _account_pb2.AccountConnectedAccount
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., connected_account: _Optional[_Union[_account_pb2.AccountConnectedAccount, _Mapping]] = ...) -> None: ...
