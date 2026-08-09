from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedPlanSchema, SeedUsersPlan, SeedAccountsPlan


class ExistingUserGetDocumentsSeedsScenario(SeedsScenario):
    @property
    def plan(self) -> SeedPlanSchema:
        return SeedPlanSchema(
            users=SeedUsersPlan(
                count=100,
                savings_account=SeedAccountsPlan(count=1),
                deposit_accounts=SeedAccountsPlan(count=1)
            )
        )

    @property
    def scenario(self) -> str:
        return "existing_user_get_documents"


if __name__ == "__main__":
    seeds_scenario = ExistingUserGetDocumentsSeedsScenario()
    seeds_scenario.build()
