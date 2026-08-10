from clients.http.client import HttpClient, QueryParams, HttpClientExtensions
from httpx import Response
from locust.env import Environment

from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from clients.http.gateway.accounts.schema import (
    GetAccountsQuerySchema,
    OpenCreditAccountRequestSchema,
    OpenCreditAccountResponseSchema,
    OpenDebitAccountRequestSchema,
    OpenDebitAccountResponseSchema,
    OpenDepositAccountRequestSchema,
    OpenDepositAccountResponseSchema,
    OpenSavingsAccountRequestSchema,
    OpenSavingsAccountResponseSchema,
    GetAccountsResponseSchema
)


class AccountsGatewayHttpClient(HttpClient):
    def get_accounts_api(self, query: GetAccountsQuerySchema) -> Response:
        return self.get(
            "/api/v1/accounts",
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HttpClientExtensions(route="/api/v1/accounts")
        )

    def open_deposit_account_api(self, request: OpenDepositAccountRequestSchema) -> Response:
        return self.post("/api/v1/accounts/open-deposit-account", body=request.model_dump(by_alias=True))

    def open_savings_account_api(self, request: OpenSavingsAccountRequestSchema) -> Response:
        return self.post("/api/v1/accounts/open-savings-account", body=request.model_dump(by_alias=True))

    def open_debit_account_api(self, request: OpenDebitAccountRequestSchema) -> Response:
        return self.post("/api/v1/accounts/open-debit-card-account", body=request.model_dump(by_alias=True))

    def open_credit_account_api(self, request: OpenCreditAccountRequestSchema) -> Response:
        return self.post("/api/v1/accounts/open-credit-card-account", body=request.model_dump(by_alias=True))

    def get_accounts(self, user_id: str) -> GetAccountsResponseSchema:
        query = GetAccountsQuerySchema(user_id=user_id)
        response = self.get_accounts_api(query)
        return GetAccountsResponseSchema.model_validate_json(response.text)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseSchema:
        request = OpenDepositAccountRequestSchema(user_id=user_id)
        response = self.open_deposit_account_api(request)
        return OpenDepositAccountResponseSchema.model_validate_json(response.text)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseSchema:
        request = OpenSavingsAccountRequestSchema(user_id=user_id)
        response = self.open_savings_account_api(request)
        return OpenSavingsAccountResponseSchema.model_validate_json(response.text)

    def open_debit_account(self, user_id: str) -> OpenDebitAccountResponseSchema:
        request = OpenDebitAccountRequestSchema(user_id=user_id)
        response = self.open_debit_account_api(request)
        return OpenDebitAccountResponseSchema.model_validate_json(response.text)

    def open_credit_account(self, user_id: str) -> OpenCreditAccountResponseSchema:
        request = OpenCreditAccountRequestSchema(user_id=user_id)
        response = self.open_credit_account_api(request)
        return OpenCreditAccountResponseSchema.model_validate_json(response.text)


def build_accounts_gateway_http_client() -> AccountsGatewayHttpClient:
    return AccountsGatewayHttpClient(client=build_gateway_http_client())


def build_accounts_gateway_locust_http_client(environment: Environment) -> AccountsGatewayHttpClient:
    return AccountsGatewayHttpClient(client=build_gateway_locust_http_client(environment))
