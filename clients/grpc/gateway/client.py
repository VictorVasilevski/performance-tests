from grpc import Channel, insecure_channel, intercept_channel
from locust.env import Environment

from clients.grpc.interceptors.locust_interceptor import LocustInterceptor


def build_gateway_grpc_client() -> Channel:
    return insecure_channel('192.168.56.2:9003')


def build_gateway_locust_grpc_client(environment: Environment) -> Channel:
    channel = insecure_channel('192.168.56.2:9003')
    return intercept_channel(channel, LocustInterceptor(environment))
