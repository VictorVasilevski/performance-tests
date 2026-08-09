from grpc import Channel
from locust.env import Environment

from clients.grpc.client import GrpcClient
from clients.grpc.gateway.client import build_gateway_grpc_client, build_gateway_locust_grpc_client

from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import GetContractDocumentRequest, GetContractDocumentResponse
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import GetTariffDocumentRequest, GetTariffDocumentResponse


class DocumentsGatewayGrpcClient(GrpcClient):
    def __init__(self, channel: Channel):
        super().__init__(channel)
        self.stub = DocumentsGatewayServiceStub(self.channel)

    def get_tariff_document_api(self, request: GetTariffDocumentRequest) -> GetTariffDocumentResponse:
        return self.stub.GetTariffDocument(request)

    def get_contract_document_api(self, request: GetContractDocumentRequest) -> GetContractDocumentResponse:
        return self.stub.GetContractDocument(request)

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponse:
        request = GetTariffDocumentRequest(account_id=account_id)
        return self.get_tariff_document_api(request)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponse:
        request = GetContractDocumentRequest(account_id=account_id)
        return self.get_contract_document_api(request)


def build_documents_gateway_grpc_client() -> DocumentsGatewayGrpcClient:
    return DocumentsGatewayGrpcClient(channel=build_gateway_grpc_client())


def build_documents_gateway_locust_grpc_client(environment: Environment) -> DocumentsGatewayGrpcClient:
    return DocumentsGatewayGrpcClient(channel=build_gateway_locust_grpc_client(environment))
