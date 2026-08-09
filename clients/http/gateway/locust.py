from locust import TaskSet, SequentialTaskSet
from clients.http.gateway.users.client import build_users_gateway_locust_http_client, UsersGatewayHttpClient
from clients.http.gateway.cards.client import build_cards_gateway_locust_http_client, CardsGatewayHTTPClient
from clients.http.gateway.accounts.client import build_accounts_gateway_locust_http_client, AccountsGatewayHttpClient
from clients.http.gateway.operations.client import build_operations_gateway_locust_http_client, OperationHttpClient
from clients.http.gateway.documents.client import build_documents_gateway_locust_http_client, DocumentsGatewayHttpClient


class GatewayHttpTaskSet(TaskSet):
    users_gateway_client: UsersGatewayHttpClient
    accounts_gateway_client: AccountsGatewayHttpClient
    operations_gateway_client: OperationHttpClient
    documents_gateway_client: DocumentsGatewayHttpClient
    cards_gateway_client: CardsGatewayHTTPClient

    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_http_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_http_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_http_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_http_client(self.user.environment)


class GatewayHttpSequentialTaskSet(SequentialTaskSet):
    users_gateway_client: UsersGatewayHttpClient
    accounts_gateway_client: AccountsGatewayHttpClient
    operations_gateway_client: OperationHttpClient
    documents_gateway_client: DocumentsGatewayHttpClient
    cards_gateway_client: CardsGatewayHTTPClient

    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_http_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_http_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_http_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_http_client(self.user.environment)
