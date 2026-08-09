from locust import task

from clients.grpc.gateway.locust import GatewayGrpcSequentialTaskSet
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import OpenSavingsAccountResponse
from tools.locust.user import LocustBaseUser


class GetDocumentsSequentialTaskSet(GatewayGrpcSequentialTaskSet):
    create_user_response: CreateUserResponse | None = None
    open_savings_account_response: OpenSavingsAccountResponse | None = None

    @task
    def create_user(self):
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_savings_account(self):
        if not self.create_user_response:
            return

        self.open_savings_account_response = self.accounts_gateway_client.open_savings_account(
            user_id=self.create_user_response.user.id
        )

    @task
    def get_documents(self):
        if not self.open_savings_account_response:
            return

        self.documents_gateway_client.get_tariff_document(
            account_id=self.open_savings_account_response.account.id
        )
        self.documents_gateway_client.get_contract_document(
            account_id=self.open_savings_account_response.account.id
        )


class GetDocumentsUser(LocustBaseUser):
    tasks = [GetDocumentsSequentialTaskSet]
