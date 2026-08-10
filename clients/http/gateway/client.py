from httpx import Client
from locust.env import Environment
import logging

from clients.http.event_hooks.locust_event_hooks import locust_response_event_hook, locust_request_event_hook
from config import settings


def build_gateway_http_client() -> Client:
    return Client(timeout=settings.gateway_http_client.timeout, base_url=settings.gateway_http_client.client_url)


def build_gateway_locust_http_client(environment: Environment) -> Client:
    logging.getLogger("httpx").setLevel(logging.WARNING)  # Disable httpx logging to eliminate client's cpu usage overhead
    return Client(
        timeout=settings.gateway_http_client.timeout,
        base_url=settings.gateway_http_client.client_url,
        event_hooks={
            "request": [locust_request_event_hook],
            "response": [locust_response_event_hook(environment)]
        }
    )



