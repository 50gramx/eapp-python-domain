from ethos.elint.services.product.identity.account_assistant import access_account_assistant_pb2 as _access_account_assistant_pb2
from ethos.elint.entities import generic_pb2 as _generic_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_pb2 as _space_knowledge_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AskQuestionRequest(_message.Message):
    __slots__ = ("access_auth_details", "message", "ask_particular_domain", "space_knowledge_domain")
    ACCESS_AUTH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASK_PARTICULAR_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SPACE_KNOWLEDGE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    access_auth_details: _access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails
    message: str
    ask_particular_domain: bool
    space_knowledge_domain: _space_knowledge_domain_pb2.SpaceKnowledgeDomain
    def __init__(self, access_auth_details: _Optional[_Union[_access_account_assistant_pb2.AccountAssistantServicesAccessAuthDetails, _Mapping]] = ..., message: _Optional[str] = ..., ask_particular_domain: bool = ..., space_knowledge_domain: _Optional[_Union[_space_knowledge_domain_pb2.SpaceKnowledgeDomain, _Mapping]] = ...) -> None: ...

class AskQuestionResponse(_message.Message):
    __slots__ = ("domains_ranked_answers", "response_meta")
    DOMAINS_RANKED_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    domains_ranked_answers: _containers.RepeatedCompositeFieldContainer[DomainRankedAnswers]
    response_meta: _generic_pb2.ResponseMeta
    def __init__(self, domains_ranked_answers: _Optional[_Iterable[_Union[DomainRankedAnswers, _Mapping]]] = ..., response_meta: _Optional[_Union[_generic_pb2.ResponseMeta, _Mapping]] = ...) -> None: ...

class DomainRankedAnswers(_message.Message):
    __slots__ = ("space_knowledge_domain", "ranked_answers")
    SPACE_KNOWLEDGE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    RANKED_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    space_knowledge_domain: _space_knowledge_domain_pb2.SpaceKnowledgeDomain
    ranked_answers: _containers.RepeatedCompositeFieldContainer[_space_knowledge_domain_pb2.RankedAnswer]
    def __init__(self, space_knowledge_domain: _Optional[_Union[_space_knowledge_domain_pb2.SpaceKnowledgeDomain, _Mapping]] = ..., ranked_answers: _Optional[_Iterable[_Union[_space_knowledge_domain_pb2.RankedAnswer, _Mapping]]] = ...) -> None: ...
