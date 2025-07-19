from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import galaxy_pb2 as _galaxy_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from ethos.elint.services.product.knowledge.space_knowledge_domain import create_space_knowledge_domain_pb2 as _create_space_knowledge_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddEthosCoinEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADD_100_ETHOSCOIN: _ClassVar[AddEthosCoinEnum]
    ADD_200_ETHOSCOIN: _ClassVar[AddEthosCoinEnum]
    ADD_400_ETHOSCOIN: _ClassVar[AddEthosCoinEnum]
    ADD_800_ETHOSCOIN: _ClassVar[AddEthosCoinEnum]
    ADD_1600_ETHOSCOIN: _ClassVar[AddEthosCoinEnum]
    ADD_3200_ETHOSCOIN: _ClassVar[AddEthosCoinEnum]
    ADD_6400_ETHOSCOIN: _ClassVar[AddEthosCoinEnum]
ADD_100_ETHOSCOIN: AddEthosCoinEnum
ADD_200_ETHOSCOIN: AddEthosCoinEnum
ADD_400_ETHOSCOIN: AddEthosCoinEnum
ADD_800_ETHOSCOIN: AddEthosCoinEnum
ADD_1600_ETHOSCOIN: AddEthosCoinEnum
ADD_3200_ETHOSCOIN: AddEthosCoinEnum
ADD_6400_ETHOSCOIN: AddEthosCoinEnum

class AccountPayInPublishableKey(_message.Message):
    __slots__ = ("key", "response_meta")
    KEY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    key: str
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, key: _Optional[str] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class AccountPayInAccessKey(_message.Message):
    __slots__ = ("json_key", "response_meta")
    JSON_KEY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    json_key: str
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, json_key: _Optional[str] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class AccountPayInSecretKey(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class GetAccountPayInIntentRequest(_message.Message):
    __slots__ = ("access_auth_details", "prefer_billing_annually")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PREFER_BILLING_ANNUALLY_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    prefer_billing_annually: bool
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., prefer_billing_annually: bool = ...) -> None: ...

class GetAccountPayInIntentResponse(_message.Message):
    __slots__ = ("response_meta",)
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class ListAllCardsResponse(_message.Message):
    __slots__ = ("account_pay_in_cards", "response_meta")
    ACCOUNT_PAY_IN_CARDS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_pay_in_cards: _containers.RepeatedCompositeFieldContainer[_account_pb2.AccountPayInCardDetails]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_pay_in_cards: _Optional[_Iterable[_Union[_account_pb2.AccountPayInCardDetails, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class SaveCardResponse(_message.Message):
    __slots__ = ("save_card_secret", "response_meta")
    SAVE_CARD_SECRET_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    save_card_secret: str
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, save_card_secret: _Optional[str] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class AccountEthosCoinBalanceResponse(_message.Message):
    __slots__ = ("response_meta", "balance")
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    response_meta: _generic_pb2.ResponseMeta
    balance: float
    def __init__(self, response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ..., balance: _Optional[float] = ...) -> None: ...

class CreditAccountEthosCoinBalanceRequest(_message.Message):
    __slots__ = ("access_auth_details", "add_ethoscoin", "account_currency", "play_store_subscription_id", "google_play_purchase_token", "description", "play_store_product_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ADD_ETHOSCOIN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PLAY_STORE_SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_PLAY_PURCHASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PLAY_STORE_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    add_ethoscoin: float
    account_currency: str
    play_store_subscription_id: str
    google_play_purchase_token: str
    description: str
    play_store_product_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., add_ethoscoin: _Optional[float] = ..., account_currency: _Optional[str] = ..., play_store_subscription_id: _Optional[str] = ..., google_play_purchase_token: _Optional[str] = ..., description: _Optional[str] = ..., play_store_product_id: _Optional[str] = ...) -> None: ...

class CreateAccountOpenGalaxyTierSubscriptionRequest(_message.Message):
    __slots__ = ("access_auth_details", "open_galaxy_tier_enum")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    OPEN_GALAXY_TIER_ENUM_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    open_galaxy_tier_enum: _galaxy_pb2.OpenGalaxyTierEnum
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., open_galaxy_tier_enum: _Optional[_Union[_galaxy_pb2.OpenGalaxyTierEnum, str]] = ...) -> None: ...

class VerifyAccountOpenGalaxyPlayStoreSubscriptionChargeRequest(_message.Message):
    __slots__ = ("access_auth_details", "open_galaxy_tier_enum", "google_play_purchase_token")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    OPEN_GALAXY_TIER_ENUM_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_PLAY_PURCHASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    open_galaxy_tier_enum: _galaxy_pb2.OpenGalaxyTierEnum
    google_play_purchase_token: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., open_galaxy_tier_enum: _Optional[_Union[_galaxy_pb2.OpenGalaxyTierEnum, str]] = ..., google_play_purchase_token: _Optional[str] = ...) -> None: ...

class ConfirmAccountOpenGalaxyPlayStoreSubscriptionRequest(_message.Message):
    __slots__ = ("access_auth_details", "open_galaxy_tier_enum", "google_play_purchase_token")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    OPEN_GALAXY_TIER_ENUM_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_PLAY_PURCHASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    open_galaxy_tier_enum: _galaxy_pb2.OpenGalaxyTierEnum
    google_play_purchase_token: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., open_galaxy_tier_enum: _Optional[_Union[_galaxy_pb2.OpenGalaxyTierEnum, str]] = ..., google_play_purchase_token: _Optional[str] = ...) -> None: ...

class ConfirmAccountEthosCoinBalanceAdditionRequest(_message.Message):
    __slots__ = ("access_auth_details", "add_ethos_coin_enum", "google_play_purchase_token")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ADD_ETHOS_COIN_ENUM_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_PLAY_PURCHASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    add_ethos_coin_enum: AddEthosCoinEnum
    google_play_purchase_token: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., add_ethos_coin_enum: _Optional[_Union[AddEthosCoinEnum, str]] = ..., google_play_purchase_token: _Optional[str] = ...) -> None: ...

class VerifyAccountEthosCoinBalanceAdditionRequest(_message.Message):
    __slots__ = ("access_auth_details", "add_ethos_coin_enum", "google_play_purchase_token")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ADD_ETHOS_COIN_ENUM_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_PLAY_PURCHASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    add_ethos_coin_enum: AddEthosCoinEnum
    google_play_purchase_token: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., add_ethos_coin_enum: _Optional[_Union[AddEthosCoinEnum, str]] = ..., google_play_purchase_token: _Optional[str] = ...) -> None: ...
