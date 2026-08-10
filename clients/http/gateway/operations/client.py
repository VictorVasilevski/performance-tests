from typing import TypedDict

from clients.http.client import HttpClient, HttpClientExtensions
from locust.env import Environment

from httpx import QueryParams, Response

from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client


class OperationDict(TypedDict):
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]


class ReceiptDict(TypedDict):
    url: str
    document: str


class GetOperationReceiptResponseDict(TypedDict):
    receipt: ReceiptDict


class GetOperationResponseDict(TypedDict):
    operation: OperationDict


class OperationsSummaryDict(TypedDict):
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummaryDict


class MakeFeeOperationRequestDict(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeTopUpOperationRequestDict(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationResponseDict(TypedDict):
    operation: OperationDict


class OperationHttpClient(HttpClient):
    def get_operations_api(self, account_id: str | None = None) -> Response:
        params = QueryParams(accountId=account_id) if account_id else None
        return self.get("/api/v1/operations", params=params)

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        return self.get(
            f"/api/v1/operations/operation-receipt/{operation_id}",
            extensions=HttpClientExtensions(route="/api/v1/operations/operation-receipt/{operation_id}")
        )

    def get_operation_api(self, operation_id: str) -> Response:
        return self.get(
            f"/api/v1/operations/{operation_id}",
            extensions=HttpClientExtensions(route="/api/v1/operations/{operation_id}")
        )

    def get_operations_summary_api(self, account_id: str | None = None) -> Response:
        params = QueryParams(accountId=account_id) if account_id else None
        return self.get(
            "/api/v1/operations/operations-summary",
            params=params,
            extensions=HttpClientExtensions(route="/api/v1/operations/operations-summary")
        )

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        return self.post("/api/v1/operations/make-fee-operation", body=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        return self.post("/api/v1/operations/make-top-up-operation", body=request)

    def make_cashback_operation_api(self):...
    def make_transfer_operation_api(self):...
    def make_purchase_operation_api(self):...
    def make_bill_payment_operation_api(self):...
    def make_cash_withdrawal_operation_api(self):...


    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        response = self.get_operations_api(account_id)
        return response.json()
    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()
    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operations_summary(self, account_id: str | None = None) -> GetOperationsSummaryResponseDict:
        response = self.get_operations_summary_api(account_id)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self):...
    def make_transfer_operation(self):...
    def make_purchase_operation(self):...
    def make_bill_payment_operation(self):...
    def make_cash_withdrawal_operation(self):...


def build_operations_gateway_http_client():
    return OperationHttpClient(client=build_gateway_http_client())


def build_operations_gateway_locust_http_client(environment: Environment) -> OperationHttpClient:
    return OperationHttpClient(client=build_gateway_locust_http_client(environment))
