from locust import task, events
from locust.env import Environment

from clients.http.gateway.locust import GatewayHttpTaskSet
from clients.http.gateway.operations.client import MakeTopUpOperationResponseDict
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser
from seeds.scenarios.existing_user_make_purchase_operation import ExistingUserMakePurchaseOperationSeedsScenario


# Runs automatically at the beginning of scenario, once globally
@events.init.add_listener
def init(environment: Environment, **kwargs):
    seed_scenario = ExistingUserMakePurchaseOperationSeedsScenario()
    seed_scenario.build()

    environment.seeds = seed_scenario.load()  # Used to transfer seeds results into task set


class ExistingUserMakePurchaseOperationTaskSet(GatewayHttpTaskSet):
    make_top_up_operation_response: MakeTopUpOperationResponseDict | None = None
    seed_user: SeedUserResult

    def on_start(self) -> None:
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(1)
    def make_top_up_operation(self):
        self.make_top_up_operation_response = self.operations_gateway_client.make_top_up_operation(
            card_id=self.seed_user.credit_accounts[0].physical_cards[0].card_id,
            account_id=self.seed_user.credit_accounts[0].account_id
        )

    @task(2)
    def get_accounts(self):
        self.accounts_gateway_client.get_accounts(
            user_id=self.seed_user.user_id
        )

    @task(2)
    def get_operations(self):
        self.operations_gateway_client.get_operations(
            account_id=self.seed_user.credit_accounts[0].account_id
        )

    @task(2)
    def get_operations_summary(self):
        self.operations_gateway_client.get_operations_summary(
            account_id=self.seed_user.credit_accounts[0].account_id
        )


class MakePurchaseOperationUser(LocustBaseUser):
    tasks = [ExistingUserMakePurchaseOperationTaskSet]
