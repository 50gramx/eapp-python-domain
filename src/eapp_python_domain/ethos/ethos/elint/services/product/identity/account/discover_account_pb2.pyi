from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_assistant_pb2 as _account_assistant_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from ethos.elint.services.product.identity.account import access_account_pb2 as _access_account_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAccountByIdRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class GetAccountByIdResponse(_message.Message):
    __slots__ = ("account", "response_meta")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account: _account_pb2.Account
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetAccountMetaByAccountIdRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_id")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_id: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetAccountMetaByAccountIdResponse(_message.Message):
    __slots__ = ("account_meta", "response_meta")
    ACCOUNT_META_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_meta: _account_pb2.AccountMeta
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_meta: _Optional[_Union[_account_pb2.AccountMeta, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class GetAccountProfilePictureRequest(_message.Message):
    __slots__ = ("access_auth_details", "picture_size", "picture_scale")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PICTURE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PICTURE_SCALE_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    picture_size: _generic_pb2.PictureSize
    picture_scale: _generic_pb2.PictureScale
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., picture_size: _Optional[_Union[_generic_pb2.PictureSize, str]] = ..., picture_scale: _Optional[_Union[_generic_pb2.PictureScale, str]] = ...) -> None: ...

class GetAccountProfilePictureResponse(_message.Message):
    __slots__ = ("image_data", "response_meta")
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    image_data: _containers.RepeatedScalarFieldContainer[bytes]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, image_data: _Optional[_Iterable[bytes]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class IsAccountExistsWithMobileRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_country_code", "account_mobile_number")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_country_code: str
    account_mobile_number: str
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_country_code: _Optional[str] = ..., account_mobile_number: _Optional[str] = ...) -> None: ...

class AreAccountsExistingWithMobileRequest(_message.Message):
    __slots__ = ("access_auth_details", "account_mobiles")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_MOBILES_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_pb2.AccountServicesAccessAuthDetails
    account_mobiles: _containers.RepeatedCompositeFieldContainer[_account_pb2.AccountMobile]
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_pb2.AccountServicesAccessAuthDetails, _Mapping]] = ..., account_mobiles: _Optional[_Iterable[_Union[_account_pb2.AccountMobile, _Mapping]]] = ...) -> None: ...

class AreAccountsExistingWithMobileResponse(_message.Message):
    __slots__ = ("account_mobiles_exists", "response_meta")
    class AccountMobileExists(_message.Message):
        __slots__ = ("account_country_code", "account_mobile_number", "account_exists")
        ACCOUNT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_EXISTS_FIELD_NUMBER: _ClassVar[int]
        account_country_code: str
        account_mobile_number: str
        account_exists: bool
        def __init__(self, account_country_code: _Optional[str] = ..., account_mobile_number: _Optional[str] = ..., account_exists: bool = ...) -> None: ...
    ACCOUNT_MOBILES_EXISTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    account_mobiles_exists: AreAccountsExistingWithMobileResponse.AccountMobileExists
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, account_mobiles_exists: _Optional[_Union[AreAccountsExistingWithMobileResponse.AccountMobileExists, _Mapping]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...
