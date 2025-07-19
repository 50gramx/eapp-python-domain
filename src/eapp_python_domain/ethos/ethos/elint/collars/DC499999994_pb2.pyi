from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ethos.elint.entities import space_knowledge_domain_pb2 as _space_knowledge_domain_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2_1
from ethos.elint.entities import space_knowledge_domain_file_pb2 as _space_knowledge_domain_file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DC499999994(_message.Message):
    __slots__ = ("id", "name", "description", "skincare_product", "created_at", "updated_at", "product_images_domain")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKINCARE_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_IMAGES_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    skincare_product: SkincareProduct
    created_at: _timestamp_pb2_1.Timestamp
    updated_at: _timestamp_pb2_1.Timestamp
    product_images_domain: _space_knowledge_domain_pb2.SpaceKnowledgeDomain
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., skincare_product: _Optional[_Union[SkincareProduct, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2_1.Timestamp, _Mapping]] = ..., product_images_domain: _Optional[_Union[_space_knowledge_domain_pb2.SpaceKnowledgeDomain, _Mapping]] = ...) -> None: ...

class SkincareProduct(_message.Message):
    __slots__ = ("id", "name", "brand_id", "category_id", "sub_category_id", "price", "mrp", "is_in_stock", "stock_quantity", "seller_locations", "batch_number", "expiry_date", "country_of_origin", "description", "ingredients", "compatibility", "target_audience", "logistics", "certifications", "marketing", "images", "reviews", "related_products")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BRAND_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    MRP_FIELD_NUMBER: _ClassVar[int]
    IS_IN_STOCK_FIELD_NUMBER: _ClassVar[int]
    STOCK_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SELLER_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    BATCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_DATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    LOGISTICS_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    MARKETING_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    REVIEWS_FIELD_NUMBER: _ClassVar[int]
    RELATED_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    brand_id: str
    category_id: str
    sub_category_id: str
    price: float
    mrp: float
    is_in_stock: bool
    stock_quantity: int
    seller_locations: _containers.RepeatedScalarFieldContainer[str]
    batch_number: str
    expiry_date: str
    country_of_origin: str
    description: DetailedDescription
    ingredients: Ingredients
    compatibility: SkinCompatibility
    target_audience: TargetAudience
    logistics: PackagingAndLogistics
    certifications: _containers.RepeatedScalarFieldContainer[str]
    marketing: SeoAndMarketing
    images: ProductImages
    reviews: Reviews
    related_products: RelatedProducts
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., brand_id: _Optional[str] = ..., category_id: _Optional[str] = ..., sub_category_id: _Optional[str] = ..., price: _Optional[float] = ..., mrp: _Optional[float] = ..., is_in_stock: bool = ..., stock_quantity: _Optional[int] = ..., seller_locations: _Optional[_Iterable[str]] = ..., batch_number: _Optional[str] = ..., expiry_date: _Optional[str] = ..., country_of_origin: _Optional[str] = ..., description: _Optional[_Union[DetailedDescription, _Mapping]] = ..., ingredients: _Optional[_Union[Ingredients, _Mapping]] = ..., compatibility: _Optional[_Union[SkinCompatibility, _Mapping]] = ..., target_audience: _Optional[_Union[TargetAudience, _Mapping]] = ..., logistics: _Optional[_Union[PackagingAndLogistics, _Mapping]] = ..., certifications: _Optional[_Iterable[str]] = ..., marketing: _Optional[_Union[SeoAndMarketing, _Mapping]] = ..., images: _Optional[_Union[ProductImages, _Mapping]] = ..., reviews: _Optional[_Union[Reviews, _Mapping]] = ..., related_products: _Optional[_Union[RelatedProducts, _Mapping]] = ...) -> None: ...

class DetailedDescription(_message.Message):
    __slots__ = ("id", "product_id", "overview", "key_claims", "clinical_tests", "consumer_feedback")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    KEY_CLAIMS_FIELD_NUMBER: _ClassVar[int]
    CLINICAL_TESTS_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_id: str
    overview: str
    key_claims: str
    clinical_tests: str
    consumer_feedback: str
    def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., overview: _Optional[str] = ..., key_claims: _Optional[str] = ..., clinical_tests: _Optional[str] = ..., consumer_feedback: _Optional[str] = ...) -> None: ...

class Ingredients(_message.Message):
    __slots__ = ("id", "product_id", "active_ingredients", "inactive_ingredients", "allergens", "ingredient_details", "safety_parameters")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    ALLERGENS_FIELD_NUMBER: _ClassVar[int]
    INGREDIENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SAFETY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_id: str
    active_ingredients: _containers.RepeatedScalarFieldContainer[str]
    inactive_ingredients: _containers.RepeatedScalarFieldContainer[str]
    allergens: _containers.RepeatedScalarFieldContainer[str]
    ingredient_details: _containers.RepeatedCompositeFieldContainer[IngredientDetail]
    safety_parameters: SafetyParameters
    def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., active_ingredients: _Optional[_Iterable[str]] = ..., inactive_ingredients: _Optional[_Iterable[str]] = ..., allergens: _Optional[_Iterable[str]] = ..., ingredient_details: _Optional[_Iterable[_Union[IngredientDetail, _Mapping]]] = ..., safety_parameters: _Optional[_Union[SafetyParameters, _Mapping]] = ...) -> None: ...

class IngredientDetail(_message.Message):
    __slots__ = ("id", "ingredient_id", "name", "function", "source", "concentration", "safety_rating")
    ID_FIELD_NUMBER: _ClassVar[int]
    INGREDIENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATION_FIELD_NUMBER: _ClassVar[int]
    SAFETY_RATING_FIELD_NUMBER: _ClassVar[int]
    id: str
    ingredient_id: str
    name: str
    function: str
    source: str
    concentration: str
    safety_rating: str
    def __init__(self, id: _Optional[str] = ..., ingredient_id: _Optional[str] = ..., name: _Optional[str] = ..., function: _Optional[str] = ..., source: _Optional[str] = ..., concentration: _Optional[str] = ..., safety_rating: _Optional[str] = ...) -> None: ...

class SafetyParameters(_message.Message):
    __slots__ = ("id", "ingredient_id", "global_safety_standards", "indian_safety_standards")
    ID_FIELD_NUMBER: _ClassVar[int]
    INGREDIENT_ID_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_SAFETY_STANDARDS_FIELD_NUMBER: _ClassVar[int]
    INDIAN_SAFETY_STANDARDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    ingredient_id: str
    global_safety_standards: _containers.RepeatedScalarFieldContainer[str]
    indian_safety_standards: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., ingredient_id: _Optional[str] = ..., global_safety_standards: _Optional[_Iterable[str]] = ..., indian_safety_standards: _Optional[_Iterable[str]] = ...) -> None: ...

class SkinCompatibility(_message.Message):
    __slots__ = ("id", "ingredient_id", "dermatology_approval", "suitable_skin_types", "unsuitable_conditions", "supported_scientific_studies", "environmental_factors")
    ID_FIELD_NUMBER: _ClassVar[int]
    INGREDIENT_ID_FIELD_NUMBER: _ClassVar[int]
    DERMATOLOGY_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    SUITABLE_SKIN_TYPES_FIELD_NUMBER: _ClassVar[int]
    UNSUITABLE_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_SCIENTIFIC_STUDIES_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTAL_FACTORS_FIELD_NUMBER: _ClassVar[int]
    id: str
    ingredient_id: str
    dermatology_approval: str
    suitable_skin_types: _containers.RepeatedScalarFieldContainer[str]
    unsuitable_conditions: _containers.RepeatedScalarFieldContainer[str]
    supported_scientific_studies: _containers.RepeatedScalarFieldContainer[str]
    environmental_factors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., ingredient_id: _Optional[str] = ..., dermatology_approval: _Optional[str] = ..., suitable_skin_types: _Optional[_Iterable[str]] = ..., unsuitable_conditions: _Optional[_Iterable[str]] = ..., supported_scientific_studies: _Optional[_Iterable[str]] = ..., environmental_factors: _Optional[_Iterable[str]] = ...) -> None: ...

class TargetAudience(_message.Message):
    __slots__ = ("id", "product_id", "demographic", "use_case", "lifestyle", "concerns", "application_guide")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    DEMOGRAPHIC_FIELD_NUMBER: _ClassVar[int]
    USE_CASE_FIELD_NUMBER: _ClassVar[int]
    LIFESTYLE_FIELD_NUMBER: _ClassVar[int]
    CONCERNS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_GUIDE_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_id: str
    demographic: str
    use_case: str
    lifestyle: str
    concerns: str
    application_guide: str
    def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., demographic: _Optional[str] = ..., use_case: _Optional[str] = ..., lifestyle: _Optional[str] = ..., concerns: _Optional[str] = ..., application_guide: _Optional[str] = ...) -> None: ...

class PackagingAndLogistics(_message.Message):
    __slots__ = ("id", "product_id", "packaging_type", "weight_in_grams", "dimensions", "storage_instructions", "recyclable_packaging", "logistics_partner", "shipping_weight", "return_policy", "shelf_life_days")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGING_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_IN_GRAMS_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    RECYCLABLE_PACKAGING_FIELD_NUMBER: _ClassVar[int]
    LOGISTICS_PARTNER_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    RETURN_POLICY_FIELD_NUMBER: _ClassVar[int]
    SHELF_LIFE_DAYS_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_id: str
    packaging_type: str
    weight_in_grams: float
    dimensions: str
    storage_instructions: str
    recyclable_packaging: bool
    logistics_partner: str
    shipping_weight: float
    return_policy: str
    shelf_life_days: int
    def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., packaging_type: _Optional[str] = ..., weight_in_grams: _Optional[float] = ..., dimensions: _Optional[str] = ..., storage_instructions: _Optional[str] = ..., recyclable_packaging: bool = ..., logistics_partner: _Optional[str] = ..., shipping_weight: _Optional[float] = ..., return_policy: _Optional[str] = ..., shelf_life_days: _Optional[int] = ...) -> None: ...

class SeoAndMarketing(_message.Message):
    __slots__ = ("id", "product_id", "promotional_video_url", "social_media_handles", "keywords", "taglines")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PROMOTIONAL_VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_MEDIA_HANDLES_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    TAGLINES_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_id: str
    promotional_video_url: str
    social_media_handles: str
    keywords: _containers.RepeatedCompositeFieldContainer[Keyword]
    taglines: _containers.RepeatedCompositeFieldContainer[Tagline]
    def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., promotional_video_url: _Optional[str] = ..., social_media_handles: _Optional[str] = ..., keywords: _Optional[_Iterable[_Union[Keyword, _Mapping]]] = ..., taglines: _Optional[_Iterable[_Union[Tagline, _Mapping]]] = ...) -> None: ...

class Keyword(_message.Message):
    __slots__ = ("id", "sam_id", "term", "priority")
    ID_FIELD_NUMBER: _ClassVar[int]
    SAM_ID_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    sam_id: str
    term: str
    priority: int
    def __init__(self, id: _Optional[str] = ..., sam_id: _Optional[str] = ..., term: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...

class Tagline(_message.Message):
    __slots__ = ("id", "sam_id", "content", "priority")
    ID_FIELD_NUMBER: _ClassVar[int]
    SAM_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    sam_id: str
    content: str
    priority: int
    def __init__(self, id: _Optional[str] = ..., sam_id: _Optional[str] = ..., content: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...

class ProductImages(_message.Message):
    __slots__ = ("id", "product_id", "primary_image_id", "packaging_image_id", "logistics_image_id", "application_image_ids", "ingredient_image_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGING_IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    LOGISTICS_IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_IMAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    INGREDIENT_IMAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_id: str
    primary_image_id: str
    packaging_image_id: str
    logistics_image_id: str
    application_image_ids: _containers.RepeatedScalarFieldContainer[str]
    ingredient_image_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., primary_image_id: _Optional[str] = ..., packaging_image_id: _Optional[str] = ..., logistics_image_id: _Optional[str] = ..., application_image_ids: _Optional[_Iterable[str]] = ..., ingredient_image_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class Reviews(_message.Message):
    __slots__ = ("id", "product_id", "average_rating", "number_of_reviews", "detailed_reviews")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_RATING_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_REVIEWS_FIELD_NUMBER: _ClassVar[int]
    DETAILED_REVIEWS_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_id: str
    average_rating: float
    number_of_reviews: int
    detailed_reviews: _containers.RepeatedCompositeFieldContainer[Review]
    def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., average_rating: _Optional[float] = ..., number_of_reviews: _Optional[int] = ..., detailed_reviews: _Optional[_Iterable[_Union[Review, _Mapping]]] = ...) -> None: ...

class Review(_message.Message):
    __slots__ = ("id", "reviews_id", "user_id", "user_name", "title", "content", "rating", "timestamp", "is_verified_purchase", "images")
    ID_FIELD_NUMBER: _ClassVar[int]
    REVIEWS_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IS_VERIFIED_PURCHASE_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    id: str
    reviews_id: str
    user_id: str
    user_name: str
    title: str
    content: str
    rating: float
    timestamp: str
    is_verified_purchase: bool
    images: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., reviews_id: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., rating: _Optional[float] = ..., timestamp: _Optional[str] = ..., is_verified_purchase: bool = ..., images: _Optional[_Iterable[str]] = ...) -> None: ...

class RelatedProducts(_message.Message):
    __slots__ = ("id", "product_id", "pre_related_products", "post_related_products")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_RELATED_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    POST_RELATED_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_id: str
    pre_related_products: _containers.RepeatedCompositeFieldContainer[RelatedProduct]
    post_related_products: _containers.RepeatedCompositeFieldContainer[RelatedProduct]
    def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., pre_related_products: _Optional[_Iterable[_Union[RelatedProduct, _Mapping]]] = ..., post_related_products: _Optional[_Iterable[_Union[RelatedProduct, _Mapping]]] = ...) -> None: ...

class RelatedProduct(_message.Message):
    __slots__ = ("id", "rps_id", "product_id", "name", "relation_type", "usage_context", "image_url", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    RPS_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RELATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    USAGE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    rps_id: str
    product_id: str
    name: str
    relation_type: str
    usage_context: str
    image_url: str
    description: str
    def __init__(self, id: _Optional[str] = ..., rps_id: _Optional[str] = ..., product_id: _Optional[str] = ..., name: _Optional[str] = ..., relation_type: _Optional[str] = ..., usage_context: _Optional[str] = ..., image_url: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
