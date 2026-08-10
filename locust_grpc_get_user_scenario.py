from locust import User, task, between
from clients.grpc.gateway.users.client import build_users_gateway_locust_grpc_client, UsersGatewayGrpcClient
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserResponse


class GetUserScenarioUser(User):
    host = "localhost"  # просто мокаем, т.к. используем base_url внутри клиента
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayGrpcClient
    create_user_response: GetUserResponse

    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def get_user(self):
        self.users_gateway_client.get_user(self.create_user_response.user.id)
