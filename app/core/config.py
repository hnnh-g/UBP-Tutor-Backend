from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "mysql+pymysql://app_user:app_password@localhost:3307/app_db"
    keycloak_url: str = "http://localhost:8080"
    keycloak_realm: str = "ubp-tutor"
    keycloak_admin_user: str = "admin"
    keycloak_admin_password: str = "admin"

    vllm_text_tutor_url: str = "http://localhost:8200/v1"
    vllm_model_generation_url: str = "http://localhost:8201/v1"
    vllm_model_evaluation_url: str = "http://localhost:8202/v1"
    vllm_embedding_url: str = "http://localhost:8203/v1"

    model_config = {"env_file": ".env", "extra": "ignore"}
    active_model: str = "not configured"

    # chroma DB
    chroma_host: str = "localhost"
    chroma_port: int = 8000


settings = Settings()
