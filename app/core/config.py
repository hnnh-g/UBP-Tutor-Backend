from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "mysql+pymysql://app_user:app_password@localhost:3307/app_db"
    keycloak_url: str = "http://localhost:8080"
    keycloak_realm: str = "ubp-tutor"

    model_config = {"env_file": ".env"}


settings = Settings()
