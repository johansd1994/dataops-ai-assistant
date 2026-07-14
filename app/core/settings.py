
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application configuration.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        validate_default=True,
        frozen=True,
    )

    # ==========================================================
    # APPLICATION
    # ==========================================================

    APP_NAME: str = Field(default="DataOps AI Assistant")
    APP_VERSION: str = Field(default="1.0.0")

    ENVIRONMENT: str = Field(default="development")

    DEBUG: bool = Field(default=True)

    # ==========================================================
    # LOGGING
    # ==========================================================

    LOG_LEVEL: str = Field(default="INFO")

    # ==========================================================
    # AWS
    # ==========================================================

    AWS_REGION: str = Field(default="us-east-1")
    
    AWS_PROFILE: str = Field(default="default")

    # ==========================================================
    # BEDROCK
    # ==========================================================

    BEDROCK_INFERENCE_PROFILE_ID: str = Field(default="")

    BEDROCK_CHAT_MODEL: str

    BEDROCK_ROUTER_MODEL: str

    BEDROCK_EMBEDDING_MODEL: str

    # ==========================================================
    # S3
    # ==========================================================

    S3_BUCKET_NAME: str = Field(default="dataops-ai-assistant")

    # =====================================================
    # ATHENA
    # =====================================================

    ATHENA_DATABASE: str = Field(default="dataops_ai")

    ATHENA_WORKGROUP: str = Field(default="primary")

    ATHENA_OUTPUT_LOCATION: str = Field(default="")

    # ==========================================================
    # OPENSEARCH
    # ==========================================================

    OPENSEARCH_HOST: str = ""

    OPENSEARCH_PORT: int = 443

    OPENSEARCH_INDEX: str

    # ==========================================================
    # DYNAMODB
    # ==========================================================

    DYNAMODB_TABLE: str

    # ==========================================================
    # RAG
    # ==========================================================

    TOP_K_RESULTS: int = 5

    CHUNK_SIZE: int = 1000

    CHUNK_OVERLAP: int = 200

    # ==========================================================
    # OBSERVABILITY
    # ==========================================================

    ENABLE_TRACING: bool = True

    ENABLE_METRICS: bool = True


@lru_cache
def get_settings() -> Settings:
    """
    Returns a singleton instance of the application settings.
    """
    return Settings()


settings = get_settings()