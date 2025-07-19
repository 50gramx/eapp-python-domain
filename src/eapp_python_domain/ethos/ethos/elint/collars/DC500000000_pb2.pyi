from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.protobuf.timestamp_pb2 import Timestamp as Timestamp

DESCRIPTOR: _descriptor.FileDescriptor

class DC500000000(_message.Message):
    __slots__ = ("id", "name", "description", "appearance", "personality_traits", "communication_style", "expertise", "capabilities", "usps", "use_cases", "learning_data", "interaction_history", "personalization_data", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    PERSONALITY_TRAITS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_STYLE_FIELD_NUMBER: _ClassVar[int]
    EXPERTISE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    USPS_FIELD_NUMBER: _ClassVar[int]
    USE_CASES_FIELD_NUMBER: _ClassVar[int]
    LEARNING_DATA_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_HISTORY_FIELD_NUMBER: _ClassVar[int]
    PERSONALIZATION_DATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    appearance: Appearance
    personality_traits: PersonalityTraits
    communication_style: CommunicationStyle
    expertise: Expertise
    capabilities: Capabilities
    usps: UniqueSellingPoints
    use_cases: UseCases
    learning_data: LearningData
    interaction_history: InteractionHistory
    personalization_data: PersonalizationData
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., appearance: _Optional[_Union[Appearance, _Mapping]] = ..., personality_traits: _Optional[_Union[PersonalityTraits, _Mapping]] = ..., communication_style: _Optional[_Union[CommunicationStyle, _Mapping]] = ..., expertise: _Optional[_Union[Expertise, _Mapping]] = ..., capabilities: _Optional[_Union[Capabilities, _Mapping]] = ..., usps: _Optional[_Union[UniqueSellingPoints, _Mapping]] = ..., use_cases: _Optional[_Union[UseCases, _Mapping]] = ..., learning_data: _Optional[_Union[LearningData, _Mapping]] = ..., interaction_history: _Optional[_Union[InteractionHistory, _Mapping]] = ..., personalization_data: _Optional[_Union[PersonalizationData, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Appearance(_message.Message):
    __slots__ = ("avatar",)
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    avatar: str
    def __init__(self, avatar: _Optional[str] = ...) -> None: ...

class PersonalityTraits(_message.Message):
    __slots__ = ("traits",)
    TRAITS_FIELD_NUMBER: _ClassVar[int]
    traits: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, traits: _Optional[_Iterable[str]] = ...) -> None: ...

class CommunicationStyle(_message.Message):
    __slots__ = ("style",)
    STYLE_FIELD_NUMBER: _ClassVar[int]
    style: str
    def __init__(self, style: _Optional[str] = ...) -> None: ...

class Expertise(_message.Message):
    __slots__ = ("domain", "skills")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    skills: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain: _Optional[str] = ..., skills: _Optional[_Iterable[str]] = ...) -> None: ...

class Capabilities(_message.Message):
    __slots__ = ("key_functions",)
    KEY_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    key_functions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key_functions: _Optional[_Iterable[str]] = ...) -> None: ...

class UniqueSellingPoints(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, points: _Optional[_Iterable[str]] = ...) -> None: ...

class UseCases(_message.Message):
    __slots__ = ("cases",)
    CASES_FIELD_NUMBER: _ClassVar[int]
    cases: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cases: _Optional[_Iterable[str]] = ...) -> None: ...

class LearningData(_message.Message):
    __slots__ = ("skill_proficiency", "interaction_patterns", "goals")
    class SkillProficiencyEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    SKILL_PROFICIENCY_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    GOALS_FIELD_NUMBER: _ClassVar[int]
    skill_proficiency: _containers.ScalarMap[str, float]
    interaction_patterns: _containers.RepeatedCompositeFieldContainer[InteractionPatterns]
    goals: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, skill_proficiency: _Optional[_Mapping[str, float]] = ..., interaction_patterns: _Optional[_Iterable[_Union[InteractionPatterns, _Mapping]]] = ..., goals: _Optional[_Iterable[str]] = ...) -> None: ...

class InteractionHistory(_message.Message):
    __slots__ = ("interactions",)
    class Interaction(_message.Message):
        __slots__ = ("type", "content", "timestamp", "outcome")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        OUTCOME_FIELD_NUMBER: _ClassVar[int]
        type: str
        content: str
        timestamp: _timestamp_pb2.Timestamp
        outcome: str
        def __init__(self, type: _Optional[str] = ..., content: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., outcome: _Optional[str] = ...) -> None: ...
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    interactions: _containers.RepeatedCompositeFieldContainer[InteractionHistory.Interaction]
    def __init__(self, interactions: _Optional[_Iterable[_Union[InteractionHistory.Interaction, _Mapping]]] = ...) -> None: ...

class PersonalizationData(_message.Message):
    __slots__ = ("preferences", "context", "current_task", "preferred_communication_mode")
    class PreferencesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TASK_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_COMMUNICATION_MODE_FIELD_NUMBER: _ClassVar[int]
    preferences: _containers.ScalarMap[str, str]
    context: _containers.ScalarMap[str, str]
    current_task: str
    preferred_communication_mode: str
    def __init__(self, preferences: _Optional[_Mapping[str, str]] = ..., context: _Optional[_Mapping[str, str]] = ..., current_task: _Optional[str] = ..., preferred_communication_mode: _Optional[str] = ...) -> None: ...

class InteractionPatterns(_message.Message):
    __slots__ = ("pattern", "frequency")
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    frequency: int
    def __init__(self, pattern: _Optional[str] = ..., frequency: _Optional[int] = ...) -> None: ...
