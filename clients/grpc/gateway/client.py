from grpc import Channel, insecure_channel, intercept_channel
from locust.env import Environment

from clients.grpc.interceptors.locust_interceptor import LocustInterceptor
from config import settings


def build_gateway_grpc_client() -> Channel:
    return insecure_channel(settings.gateway_grpc_client.client_url)


def build_gateway_locust_grpc_client(environment: Environment) -> Channel:
    channel = insecure_channel(settings.gateway_grpc_client.client_url)
    return intercept_channel(channel, LocustInterceptor(environment))
