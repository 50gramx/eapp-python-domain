from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import account_pb2 as _account_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import organisation_pb2 as _organisation_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1_1
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class AssociateLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LEVEL_0: _ClassVar[AssociateLevel]
    LEVEL_1: _ClassVar[AssociateLevel]
    LEVEL_2: _ClassVar[AssociateLevel]
    LEVEL_3: _ClassVar[AssociateLevel]
    LEVEL_4: _ClassVar[AssociateLevel]
    LEVEL_5: _ClassVar[AssociateLevel]

class AssociateDepartment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCOUNTING: _ClassVar[AssociateDepartment]
    HUMAN_RESOURCE: _ClassVar[AssociateDepartment]
    INFORMATION_TECHNOLOGY: _ClassVar[AssociateDepartment]
    LOGISTICS: _ClassVar[AssociateDepartment]
    MARKETING: _ClassVar[AssociateDepartment]
    PRODUCTION: _ClassVar[AssociateDepartment]
    SALES: _ClassVar[AssociateDepartment]
    WORKS: _ClassVar[AssociateDepartment]
LEVEL_0: AssociateLevel
LEVEL_1: AssociateLevel
LEVEL_2: AssociateLevel
LEVEL_3: AssociateLevel
LEVEL_4: AssociateLevel
LEVEL_5: AssociateLevel
ACCOUNTING: AssociateDepartment
HUMAN_RESOURCE: AssociateDepartment
INFORMATION_TECHNOLOGY: AssociateDepartment
LOGISTICS: AssociateDepartment
MARKETING: AssociateDepartment
PRODUCTION: AssociateDepartment
SALES: AssociateDepartment
WORKS: AssociateDepartment

class Associate(_message.Message):
    __slots__ = ("associated_account", "associated_organisation", "associate_id", "associate_level", "associate_department", "associate_designation", "reports_to_associate_id", "associated_at")
    ASSOCIATED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_ORGANISATION_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATE_DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATE_DESIGNATION_FIELD_NUMBER: _ClassVar[int]
    REPORTS_TO_ASSOCIATE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_AT_FIELD_NUMBER: _ClassVar[int]
    associated_account: _account_pb2.Account
    associated_organisation: _organisation_pb2.Organisation
    associate_id: int
    associate_level: AssociateLevel
    associate_department: AssociateDepartment
    associate_designation: str
    reports_to_associate_id: int
    associated_at: _timestamp_pb2_1_1.Timestamp
    def __init__(self, associated_account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., associated_organisation: _Optional[_Union[_organisation_pb2.Organisation, _Mapping]] = ..., associate_id: _Optional[int] = ..., associate_level: _Optional[_Union[AssociateLevel, str]] = ..., associate_department: _Optional[_Union[AssociateDepartment, str]] = ..., associate_designation: _Optional[str] = ..., reports_to_associate_id: _Optional[int] = ..., associated_at: _Optional[_Union[_timestamp_pb2_1_1.Timestamp, _Mapping]] = ...) -> None: ...
