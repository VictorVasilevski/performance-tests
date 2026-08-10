from seeds.builder import build_grpc_seeds_builder
from seeds.dumps import save_seeds_result
from seeds.schema.plan import SeedPlanSchema, SeedUsersPlan, SeedAccountsPlan, SeedCardsPlan

builder = build_grpc_seeds_builder()
result = builder.build(
    plan=SeedPlanSchema(
        users=SeedUsersPlan(
            count=100,
            credit_card_accounts=SeedAccountsPlan(
                count=1,
                physical_cards=SeedCardsPlan(
                    count=1
                )
            )
        )
    )
)

save_seeds_result(result=result, scenario="test-scenario")
