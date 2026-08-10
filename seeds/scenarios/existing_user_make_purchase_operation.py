from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedPlanSchema, SeedUsersPlan, SeedAccountsPlan, SeedCardsPlan


class ExistingUserMakePurchaseOperationSeedsScenario(SeedsScenario):
    @property
    def plan(self) -> SeedPlanSchema:
        return SeedPlanSchema(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    physical_cards=SeedCardsPlan(
                        count=1
                    )
                )
            )
        )

    @property
    def scenario(self) -> str:
        return "existing_user_make_purchase_operation"


if __name__ == "__main__":
    seeds_scenario = ExistingUserMakePurchaseOperationSeedsScenario()
    seeds_scenario.build()
