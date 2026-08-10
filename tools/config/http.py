from pydantic import BaseModel, HttpUrl


class HttpClientConfig(BaseModel):
    base_url: HttpUrl
    timeout: float = 100.0

    @property
    def client_url(self) -> str:
        return str(self.base_url)
    