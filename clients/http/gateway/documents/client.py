from typing import TypedDict

from clients.http.client import HttpClient, HttpClientExtensions
from httpx import Response
from locust.env import Environment

from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client


class GetAccountsQueryDict(TypedDict):
    userId: str


class TariffDict(TypedDict):
    url: str
    document: str


class GetTariffDocumentResponseDict(TypedDict):
    tariff: TariffDict


class GetContractDocumentResponseDict(TypedDict):
    tariff: TariffDict


class DocumentsGatewayHttpClient(HttpClient):
    def get_tariff_document_api(self, account_id: str) -> Response:
        return self.get(
            f"/api/v1/documents/tariff-document/{account_id}",
            extensions=HttpClientExtensions(route="/api/v1/documents/tariff-document/{account_id}")
        )

    def get_contract_document_api(self, account_id: str) -> Response:
        return self.get(
            f"/api/v1/documents/contract-document/{account_id}",
            extensions=HttpClientExtensions(route="/api/v1/documents/contract-document/{account_id}")
        )

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        response = self.get_contract_document_api(account_id)
        return response.json()


def build_documents_gateway_http_client() -> DocumentsGatewayHttpClient:
    return DocumentsGatewayHttpClient(client=build_gateway_http_client())


def build_documents_gateway_locust_http_client(environment: Environment) -> DocumentsGatewayHttpClient:
    return DocumentsGatewayHttpClient(client=build_gateway_locust_http_client(environment))
