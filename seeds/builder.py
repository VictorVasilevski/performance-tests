from clients.http.gateway.users.client import UsersGatewayHttpClient, build_users_gateway_http_client
from clients.http.gateway.accounts.client import AccountsGatewayHttpClient, build_accounts_gateway_http_client
from clients.http.gateway.operations.client import OperationHttpClient, build_operations_gateway_http_client
from clients.http.gateway.cards.client import CardsGatewayHTTPClient, build_cards_gateway_http_client
from clients.grpc.gateway.users.client import UsersGatewayGrpcClient, build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import AccountsGatewayGrpcClient, build_accounts_gateway_grpc_client
from clients.grpc.gateway.operations.client import OperationsGatewayGrpcClient, build_operations_gateway_grpc_client
from clients.grpc.gateway.cards.client import CardsGatewayGrpcClient, build_cards_gateway_grpc_client
from seeds.schema.plan import SeedAccountsPlan, SeedUsersPlan, SeedPlanSchema
from seeds.schema.result import SeedAccountResult, SeedOperationResult, SeedUserResult, SeedCardResult, SeedsResultSchema


class SeedsBuilder:
    def __init__(
            self,
            users_gateway_client: UsersGatewayHttpClient | UsersGatewayGrpcClient,
            cards_gateway_client: CardsGatewayHTTPClient | CardsGatewayGrpcClient,
            accounts_gateway_client: AccountsGatewayHttpClient | AccountsGatewayGrpcClient,
            operations_gateway_client: OperationHttpClient | OperationsGatewayGrpcClient,
    ):
        self.users_gateway_client = users_gateway_client
        self.cards_gateway_client = cards_gateway_client
        self.accounts_gateway_client = accounts_gateway_client
        self.operations_gateway_client = operations_gateway_client

    def build_physical_card(self, user_id: str, account_id: str) -> SeedCardResult:
        response = self.cards_gateway_client.issue_physical_card(user_id=user_id, account_id=account_id)
        return SeedCardResult(card_id=response.card.id)

    def build_top_up_operation(self, card_id: str, account_id: str) -> SeedOperationResult:
        response = self.operations_gateway_client.make_top_up_operation(card_id, account_id)
        return SeedOperationResult(operation_id=response.operation.id)

    def build_purchase_operation(self) -> SeedOperationResult:
        response = self.operations_gateway_client.make_purchase_operation()
        return SeedOperationResult(operation_id=response.operation.id)

    def build_deposit_account(self, user_id: str) -> SeedAccountResult:
        response = self.accounts_gateway_client.open_deposit_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_savings_account(self, user_id: str) -> SeedAccountResult:
        response = self.accounts_gateway_client.open_savings_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_debit_account(self, user_id: str, plan: SeedAccountsPlan) -> SeedAccountResult:
        response = self.accounts_gateway_client.open_debit_account(user_id=user_id)
        account_id = response.account.id
        card_id = response.account.cards[0].id
        return SeedAccountResult(
            account_id=account_id,
            physical_cards=[self.build_physical_card(user_id, account_id) for _ in range(plan.physical_cards.count)],
            top_up_operations=[self.build_top_up_operation(card_id, account_id) for _ in range(plan.top_up_operations.count)],
            purchase_operations=[]
        )

    def build_credit_account(self, user_id: str, plan: SeedAccountsPlan) -> SeedAccountResult:
        response = self.accounts_gateway_client.open_credit_account(user_id=user_id)
        account_id = response.account.id
        card_id = response.account.cards[0].id
        return SeedAccountResult(
            account_id=account_id,
            physical_cards=[self.build_physical_card(user_id, account_id) for _ in range(plan.physical_cards.count)],
            top_up_operations=[self.build_top_up_operation(card_id, account_id) for _ in
                               range(plan.top_up_operations.count)],
            purchase_operations=[]
        )

    def build_user(self, plan: SeedUsersPlan) -> SeedUserResult:
        response = self.users_gateway_client.create_user()
        user_id = response.user.id
        return SeedUserResult(
            user_id=response.user.id,
            deposit_accounts=[self.build_deposit_account(user_id) for _ in range(plan.deposit_accounts.count)],
            savings_accounts=[self.build_savings_account(user_id) for _ in range(plan.savings_account.count)],
            debit_accounts=[self.build_debit_account(user_id, plan.debit_cards_accounts) for _ in range(plan.debit_cards_accounts.count)],
            credit_accounts=[self.build_credit_account(user_id, plan.credit_card_accounts) for _ in range(plan.credit_card_accounts.count)]
        )

    def build(self, plan: SeedPlanSchema) -> SeedsResultSchema:
        return SeedsResultSchema(users=[self.build_user(plan.users) for _ in range(plan.users.count)])


def build_grpc_seeds_builder() -> SeedsBuilder:
    return SeedsBuilder(
        users_gateway_client=build_users_gateway_grpc_client(),
        cards_gateway_client=build_cards_gateway_grpc_client(),
        accounts_gateway_client=build_accounts_gateway_grpc_client(),
        operations_gateway_client=build_operations_gateway_grpc_client(),
    )


def build_http_seeds_builder() -> SeedsBuilder:
    return SeedsBuilder(
        users_gateway_client=build_users_gateway_http_client(),
        cards_gateway_client=build_cards_gateway_http_client(),
        accounts_gateway_client=build_accounts_gateway_http_client(),
        operations_gateway_client=build_operations_gateway_http_client(),
    )
