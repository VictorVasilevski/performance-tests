from grpc import Channel
from locust.env import Environment

from clients.grpc.client import GrpcClient
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest, GetUserResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from tools.fakers import fake

from clients.grpc.gateway.client import build_gateway_grpc_client, build_gateway_locust_grpc_client


class UsersGatewayGrpcClient(GrpcClient):
    def __init__(self, channel: Channel):
        super().__init__(channel)
        self.stub = UsersGatewayServiceStub(self.channel)

    def get_user_api(self, request: GetUserRequest) -> GetUserResponse:
        return self.stub.GetUser(request)

    def create_user_api(self, request: CreateUserRequest) -> CreateUserResponse:
        return self.stub.CreateUser(request)

    def get_user(self, user_id: str) -> GetUserResponse:
        request = GetUserRequest(id=user_id)
        return self.get_user_api(request)

    def create_user(self) -> CreateUserResponse:
        request = CreateUserRequest(
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            middle_name=fake.middle_name(),
            phone_number=fake.phone_number()
        )
        return self.create_user_api(request)


def build_users_gateway_grpc_client() -> UsersGatewayGrpcClient:
    return UsersGatewayGrpcClient(channel=build_gateway_grpc_client())


def build_users_gateway_locust_grpc_client(environment: Environment) -> UsersGatewayGrpcClient:
    return UsersGatewayGrpcClient(channel=build_gateway_locust_grpc_client(environment))
