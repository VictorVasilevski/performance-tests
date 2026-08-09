from pydantic_settings import BaseSettings, SettingsConfigDict

from tools.config.grpc import GrpcClientConfig
from tools.config.http import HttpClientConfig
from tools.config.locust import LocustUserConfig


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    locust_user: LocustUserConfig
    gateway_http_client: HttpClientConfig
    gateway_grpc_client: GrpcClientConfig


settings = Settings()
