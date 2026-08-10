from locust import TaskSet, SequentialTaskSet
from clients.grpc.gateway.users.client import build_users_gateway_locust_grpc_client, UsersGatewayGrpcClient
from clients.grpc.gateway.cards.client import build_cards_gateway_locust_grpc_client, CardsGatewayGrpcClient
from clients.grpc.gateway.accounts.client import build_accounts_gateway_locust_grpc_client, AccountsGatewayGrpcClient
from clients.grpc.gateway.operations.client import build_operations_gateway_locust_grpc_client, OperationsGatewayGrpcClient
from clients.grpc.gateway.documents.client import build_documents_gateway_locust_grpc_client, DocumentsGatewayGrpcClient


class GatewayGrpcTaskSet(TaskSet):
    users_gateway_client: UsersGatewayGrpcClient
    accounts_gateway_client: AccountsGatewayGrpcClient
    operations_gateway_client: OperationsGatewayGrpcClient
    documents_gateway_client: DocumentsGatewayGrpcClient
    cards_gateway_client: CardsGatewayGrpcClient

    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_grpc_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_grpc_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_grpc_client(self.user.environment)


class GatewayGrpcSequentialTaskSet(SequentialTaskSet):
    users_gateway_client: UsersGatewayGrpcClient
    accounts_gateway_client: AccountsGatewayGrpcClient
    operations_gateway_client: OperationsGatewayGrpcClient
    documents_gateway_client: DocumentsGatewayGrpcClient
    cards_gateway_client: CardsGatewayGrpcClient

    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_grpc_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_grpc_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_grpc_client(self.user.environment)
